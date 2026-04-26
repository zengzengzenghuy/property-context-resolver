# property-context-resolver

<p align="center">
  <img src="./logo.png" alt="buena-context-buddy logo" width="50%" />
</p>

🌐 **语言：** [English](./README.md) · [Deutsch](./README-de.md) · **中文**

将物业管理中散落的资料 —— 邮件、扫描信件、供应商发票、银行对账单、主数据
CSV —— 整合为每栋物业、每个单元一份可审计的 `context.md`，并通过外科式的
增量更新在多次运行之间保留人工编辑。

演示物业为 `LIE-001`（柏林 Immanuelkirchstraße 26 号 WEG 业主共同体），
旗舰催收对象为租户 `MIE-001`。

## 为什么这对物业管理者重要

- **每栋物业一份可审计的档案。** 主数据（Stammdaten）、邮件、信件、发票、
  银行对账单 → 一份 `context.property.<ID>.md` + 每个单元一份
  `context.unit.<EH>.md`。身份（`Eigentümer` / `MietEig` / `Kontakt`）通过
  邮件、IBAN、单元号等强信号跨源解析。
- **外科式更新，不做整文件重生成。** Merger 只在 `<!-- auto:NAME -->`
  注释块内部写入 —— 您手工维护的笔记和业主大会决议（WEG-Beschlüsse）在每次
  运行之间均原样保留。
- **Signal-First，每行皆有据可查。** 每个分区由确定性的 Python 过滤器决定
  哪些事实送入 LLM；渲染后的每一行都附带可点击的 GitHub URL 引用。法律
  时效性由 TavilyOracle 保障（§ 247 BGB 基准利率、BGB 最新修订、柏林房租
  指数 Mietspiegel）。

## 它能做什么

流水线读取 `raw/` 目录，跨数据源解析身份，对事实进行去重和冲突检测，
将租户付款流水与租约对账，并在 `spine-v2-split` 模式下生成每栋物业 +
每个单元的 Markdown 档案。每条事实都带有指向源文件的引用（默认是 GitHub
blob URL，从 `git remote` 自动检测），因此 `context.md` 中的每一行都可
精确审计到字节。

第二步 —— LLM **Summarizer** —— 消费由确定性逻辑预过滤好的"信号"载荷
（异常项、冲突、含截止日期的事项），并在专用的 `<!-- auto:*.summary -->`
注释块内输出三句话的德语摘要。摘要遵循 **Signal-First 物业管理哲学**：
每条非空摘要包含恰好四个要素（事项、合同条款、法律义务、时间线），
并以分诊标签（`[Emergency]` / `[Routine]` / `[Administrative]`）开头。

## 架构

```
raw/                            extractor/                            out/
─────                           ──────────                            ─────
stammdaten/  ─┐                                                       events.jsonl
emails/      ─┤   SourceLoader → NoiseFilter → FactExtractor          facts.jsonl
briefe/      ─┼─►        │             │             │           ┌──► llm_cache/
rechnungen/  ─┤          ▼             ▼             ▼           │    summary.json
bank/        ─┘   (Event, [Fact])  (过滤规则)    (身份富化)         │
                                       │                         │
                                       ▼                         │
                                   FactStore                     │
                                   （append-only、                │
                                    JSONL 审计日志、               │  context.property.LIE-001.md
                                    冲突检测）                     │  context.unit.EH-XXX.md
                                       │                         │      ▲
                                       ▼                         │      │
                              DunningReconciler ─► ┐             │      │
                              PropertyAggregator ─►├─► dunning.* │      │
                                                   │   operations.*     │
                                       │           │   facts            │
                                       ▼                                │
                                PropertyMerger / UnitMerger ────────────┘
                                     │       （块注册表：blocks.py）
                                     ▼
                                Summarizer ◄── GEMINI_API_KEY（默认）
                                （Signal-First、缓存）│ ANTHROPIC_API_KEY（备用）
                                     │
                                     │  ◄── TavilyOracle（可选）
                                     │       实时欧洲央行基准利率 · § BGB
                                     │       法条修订提醒 · 房租指数
                                     │       新鲜度检查
                                     ▼
                                  Supabase（可选镜像，无密钥时 no-op）
```

### 组件

| #   | 模块                                                       | 角色                                                                                                                                                                                                                                                                                                                                     |
| --- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `extractor/sources/*`                                      | 每种源类型一个连接器（stammdaten / emails / briefe / rechnungen / bank）。产出 `(Event, [Fact])`。                                                                                                                                                                                                                                       |
| 2   | `extractor/identity.py`                                    | `IdentityResolver` —— 先按邮件 / IBAN / einheit_nr / 电话精确匹配，再用模糊姓名匹配（`difflib`，阈值 0.86）。                                                                                                                                                                                                                            |
| 3   | `extractor/engine.py::NoiseFilter`                         | 丢弃自动确认等非信号事件。当前为占位实现；待扩展引用回复剥离 / 签名剥离。                                                                                                                                                                                                                                                                |
| 4   | `extractor/engine.py::FactExtractor`                       | 对每条事实做身份富化。预留 LLM 富化钩子（暂未启用）。                                                                                                                                                                                                                                                                                    |
| 5   | `extractor/engine.py::FactStore`                           | 按 `(entity_id, key)` 分桶索引、append-only 去重、置信度门限 0.7 的冲突检测，决胜次序为 confidence > observed_at > 源优先级 > extracted_at。JSONL 双向序列化。                                                                                                                                                                           |
| 6   | `extractor/engine.py::DunningReconciler`                   | 对单个租户做付款流水与 `kaltmiete + nk_vorauszahlung` 的对账。产出 `dunning.*` 事实（mahnstufe、months_overdue、offener_betrag、verzugszinsen），锚定于 § 286 / § 288 BGB。                                                                                                                                                              |
| 7   | `extractor/aggregator.py`                                  | `PropertyAggregator` —— 从单元级状态在 `LIE-001` 上聚合 `operations.*` 事实（出租 / 空置 / 自用计数、活跃催收、待办交接）。详见 `engine.aggregation-rules.md` §5.1。                                                                                                                                                                     |
| 8   | `extractor/merger.py` + `blocks.py`                        | `PropertyMerger` / `UnitMerger` —— 对 `<!-- auto:NAME -->` 块做外科式更新。每个块是一个 `(store, ctx) -> str` 渲染函数，注册在 `PROPERTY_BLOCKS` / `UNIT_BLOCKS`。auto 块外的内容在多次运行之间保持不变。                                                                                                                                |
| 9   | `extractor/summarizer.py`                                  | `<!-- auto:*.summary -->` 块的 LLM 摘要。优先使用 Gemini（`GEMINI_API_KEY`），回退到 Anthropic Claude（`ANTHROPIC_API_KEY`）。系统提示采用 Signal-First 哲学；预过滤的信号载荷由 `blocks.py` 中的确定性逻辑构建。文件缓存于 `out/llm_cache/summary.json`。无密钥时优雅降级。                                                             |
| 10  | `extractor/section_summary.py` + `extractor/raw_loader.py` | `make_section_summary(filter, include_raw=...)` 工厂被大多数 `*.summary` 块复用；`raw_loader.gather_excerpts` 将 `source_ref` URL 还原为本地的有界摘录（`.eml` / `.pdf.txt` / 银行行 / 主数据片段），从而让 LLM 载荷包含真实内容而非仅有事实。                                                                                           |
| 11  | `extractor/tavily.py`                                      | `TavilyOracle` —— 可选的法律 / 时效事实核查层。已接入 `DunningReconciler`（实时欧洲央行基准利率覆盖硬编码的 3.5pp）、`Summarizer`（扫描输出中的 `§ BGB` 引用，在发现修订时追加 `[!WARNING] Tavily Legal Alert`）和 `PropertyAggregator`（在新版 Mietspiegel 出现时产出 `operations.context_outdated`）。无 `TAVILY_API_KEY` 时为 no-op。 |
| 12  | `extractor/sb.py`                                          | `SupabaseSink` —— 在 `spine-v2-split` 之下将渲染好的 Markdown 镜像至 Supabase。无密钥时 no-op。                                                                                                                                                                                                                                          |

### 关键设计抉择

- **用 JSONL 审计日志替代 Postgres。** Fact-Store 是 append-only 的；
  重新观测会追加新行。`latest()` 与 `conflicts()` 在从日志重建的内存索引
  上工作。无需数据库即可复现。
- **以 GitHub blob URL 作为 `source_ref`。** 从 `git remote` + 当前
  分支自动检测；在非 git 仓库下回退到本地绝对路径，确保流水线永不
  中断。可通过 `--source-ref-base` 或 `SOURCE_REF_BASE` 覆盖。
- **外科式 Markdown 更新。** Merger 仅在 `<!-- auto:NAME -->` ...
  `<!-- /auto:NAME -->` 之间写入。自由文本、人工笔记和 `## Human Notes`
  小节在多次运行之间保持原样。
- **PDF 经过预 OCR 缓存。** `scripts/preocr.py` 写入 `<file>.pdf.txt`
  同名文件；引擎优先读这些缓存，仅在必要时回退到运行时 `pdfminer.six`。
  缓存已签入 git，因此即便未安装 `pdfminer.six` 引擎也可复现。
- **LLM 写散文，不做过滤。** Summarizer 永远不会看到原始数据 ——
  `blocks.py` 中的显著性提取器（如 `_dunning_signal()`）按置信度门限、
  键白名单、近期性和异常状态预过滤。LLM 产出 ≤3 句德语，包含 Trifecta
  四要素（事项 / 合同 / 法律 / 时间线），并保留 `[(label)](url)` 引用。
- **单一物业范围。** `PROPERTY_ID = "LIE-001"` 在 `extractor/models.py`
  中硬编码。无多租户、无鉴权、无向量数据库。

## Tavily 集成

Tavily 作为"法律与时效预言机（Legal & Temporal Oracle）"接入，避免流水线
基于过时法律或硬编码金融常量给出建议。三个 hook 在 `TAVILY_API_KEY`
未设置时均静默 no-op。

### 1. `TavilyOracle` 客户端（`extractor/tavily.py`）

对 `tavily.TavilyClient` 的轻量封装，使用 `search_depth="advanced"` 与
`include_answer=True`，并附带进程内查询缓存。单例访问器：`get_oracle()`。

### 2. 动态欧洲央行基准利率（催收）

`DunningReconciler.__post_init__`（`extractor/engine.py:410`）调用
`oracle.get_ecb_base_rate()`，在拿到实时数值时覆盖硬编码的
`ECB_BASE_PP = 3.5`，使 `verzugszinsen_eur` 反映 § 247 BGB 的当前利率。

### 3. 法律引用修订提醒（Summarizer）

LLM 渲染完一个 `<!-- auto:*.summary -->` 块后，
`Summarizer.summarize()`（`extractor/summarizer.py:228`）扫描输出中的
`§ <n> <Gesetz>` 引用，并向 Tavily 询问其在过去 12 个月内是否有修订。
首个命中以 `> [!WARNING] **Tavily Legal Alert (§ N BGB):** ...` 形式
追加在摘要下方。

### 4. 上下文过期防护（Aggregator）

`PropertyAggregator.emit_for_property`（`extractor/aggregator.py:164`）
调用 `oracle.check_mietspiegel("Berlin", year-1)`，当存在更新版本的
Mietspiegel 时产出 `operations.context_outdated`，让物业仪表盘暴露
过时的本地引用。

## 构建

需要 Python 3.11+。可选系统依赖：`tesseract`（仅当需要对扫描 PDF 做 OCR
回退时；对于自带语料，预 OCR 缓存已足够，无需此项）。

```bash
# 1. 安装 Python 依赖
pip install -r requirements.txt

# 2. 在 .env 中提供密钥（所有条目均可选 —— 模块会优雅降级）
cat > .env <<'EOF'
GEMINI_API_KEY=...                      # summary 块的默认 LLM
ANTHROPIC_API_KEY=sk-ant-api03-...      # GEMINI_API_KEY 缺失时的备用 LLM
TAVILY_API_KEY=tvly-...                 # 启用实时欧洲央行利率 + 法律修订提醒
SUPABASE_URL=https://...supabase.co     # 启用 Supabase 镜像
SUPABASE_SERVICE_KEY=eyJhbGc...
EOF

# 3.（重新）构建 PDF 文本缓存 —— 仅当修改 PDF 集合时需要
python scripts/preocr.py raw/
```

`pdfminer.six` 是唯一必需的运行时依赖；其余（`pytesseract`、`pdf2image`、
`pypdf`、`supabase`、`python-dotenv`、`anthropic`）皆为可选 —— 依赖它们
的模块在导入失败或环境变量缺失时会优雅 no-op。

## 运行

端到端流水线：

```bash
# 默认 v1 运行 —— 仅档案，无增量 delta
python run.py raw/

# 固定参考日期，使法定截止日期（§ 288 BGB Verzugszinsen 等）
# 可确定性计算 —— 也会传入 LLM 摘要提示
python run.py raw/ --today 2026-04-25

# 第二次运行加上 delta 以演示外科式更新
# （先加载已存在的 out/facts.jsonl，使历史进入冲突检测）
python run.py raw/ --include-incremental --today 2026-04-25
```

输出：

```
out/
  events.jsonl                  每个源事件一行
  facts.jsonl                   完整的 append-only 事实日志
  llm_cache/summary.json        LLM 摘要输出的确定性缓存
  raw_bundle.txt                便于检查的原始文本拼接
context.property.LIE-001.md     物业级档案
context.unit.EH-XXX.md          单元级档案（每个单元一份）
```

首次运行会从 `context.property.template.md` / `context.unit.template.md`
脚手架出 Markdown 文件。后续运行只更新 auto 块的内容 —— 块外的所有内容
（包括手工维护的 `## Human Notes` 小节）都被保留。

### 在首次运行后新增 auto 块

Merger 只在新文件中**脚手架**新块。如果在文件已渲染之后才把新块注册进
`PROPERTY_BLOCKS` / `UNIT_BLOCKS`，请删除受影响的文件，让其从模板重新
脚手架：

```bash
rm context.unit.*.md context.property.*.md
python run.py raw/ --today 2026-04-25
```

### 测试

```bash
python -m unittest tests.test_factstore -v       # 单模块，详细
python -m unittest discover tests                # 全部
```

标准库 `unittest`，无额外 runner。测试文件顶部有 `make_fact()` 辅助函数 ——
新增用例时复用该模式。

## 配置

| 变量                                    | 使用方                    | 未设置时的效果                                         |
| --------------------------------------- | ------------------------- | ------------------------------------------------------ |
| `GEMINI_API_KEY`                        | `extractor/summarizer.py` | 启用 Gemini 摘要；缺失时回退到 `ANTHROPIC_API_KEY`。   |
| `ANTHROPIC_API_KEY`                     | `extractor/summarizer.py` | 启用 Claude 摘要；当 `GEMINI_API_KEY` 缺失时使用。     |
| `TAVILY_API_KEY`                        | `extractor/tavily.py`     | 启用实时法律 / 时效核查；缺失时退回硬编码默认值。      |
| `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` | `extractor/sb.py`         | Supabase 镜像被跳过；本地 Markdown 仍会写入。          |
| `SOURCE_REF_BASE`                       | `extractor/source_ref.py` | 自动检测 `git remote` + 当前分支；回退到本地绝对路径。 |

`run.py` 的 CLI 参数：

| 参数                    | 默认         | 用途                                                       |
| ----------------------- | ------------ | ---------------------------------------------------------- |
| `raw`                   | （必填）     | `raw/` 语料的路径。                                        |
| `--out`                 | `out`        | `events.jsonl` / `facts.jsonl` / `llm_cache/` 的输出目录。 |
| `--repo-root`           | `cwd`        | `context.{property,unit}.*.md` 的写入位置。                |
| `--include-incremental` | 关闭         | 遍历 `raw/incremental/`（第二次运行的 fixture）。          |
| `--source-ref-base`     | （自动检测） | 覆盖引用所用的 GitHub blob 基址。                          |
| `--today`               | 系统日期     | 催收利息和 LLM 法定期限的参考日期。                        |

## 仓库布局

```
raw/                           不可变的输入语料
extractor/                     引擎本体
  models.py                    Event + Fact dataclass、JsonlWriter
  identity.py                  IdentityResolver
  source_ref.py                本地路径 → GitHub blob URL
  engine.py                    SourceLoader / NoiseFilter / FactExtractor
                               / FactStore / DunningReconciler / format_value
  aggregator.py                PropertyAggregator（engine.aggregation-rules.md §5.1）
  merger.py                    PropertyMerger + UnitMerger（外科式更新）
  blocks.py                    块渲染注册表（PROPERTY_BLOCKS / UNIT_BLOCKS）
  section_summary.py           通用 make_section_summary(...) 工厂
  raw_loader.py                source_ref → 本地有界摘录，用于 LLM 载荷
  summarizer.py                Gemini 默认 / Claude 备用的 LLM 封装，文件缓存
  tavily.py                    TavilyOracle —— 实时欧洲央行利率、§ BGB 修订提醒、
                               Mietspiegel 新鲜度检查（无 TAVILY_API_KEY 时 no-op）
  sb.py                        Supabase 镜像
  extract.py                   跨源连接器的 fan-out
  sources/                     每种源类型一个连接器（stammdaten / emails /
                               briefe / rechnungen / bank）
  cli.py                       `python -m extractor.cli ingest`
context.property.template.md   物业级 Markdown 骨架
context.unit.template.md       单元级 Markdown 骨架
engine.aggregation-rules.md    PropertyAggregator §5.1 规范
scripts/preocr.py              预 OCR 缓存构建器
scripts/upload_raw_bundle.py   将 out/raw_bundle.txt 上传至 Supabase
supabase/                      镜像所需的 schema + edge function 脚手架
run.py                         端到端驱动
tests/test_factstore.py        标准库 unittest —— FactStore + format_value
tests/test_dunning.py          DunningReconciler 利息 + 催收等级覆盖
tests/test_merger.py           PropertyMerger / UnitMerger 外科式更新覆盖
```

## 延伸阅读

- **`CLAUDE.md`** —— 操作笔记、约定与陷阱（即"如何做"）。
- **`engine.aggregation-rules.md`** —— `PropertyAggregator` §5.1 规范。
