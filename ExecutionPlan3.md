3. The 24-Hour Execution Timeline
   Phase 1: Scaffolding with Lovable & Supabase (Hours 1 - 3)
   Prompt Lovable: Have Lovable build a "Property Management Context Dashboard" with a sidebar for properties, a file uploader for raw data, and a large Markdown viewer. Connect it to Supabase.

Database Setup: Ensure Lovable/Supabase creates a Properties table with columns: id, name, and context_md (text).

Validation: Manually insert the Markdown template into the database and verify it renders perfectly in the Lovable UI.

Phase 2: The LLM Engine & Prompt Engineering (Hours 4 - 8)
Draft the Prompt: Write the core instruction set for the LLM.

Task: Read the old Markdown file and the new Raw Data. Update the YAML for hard facts, append new issues to the correct node, resolve old issues, and remove emotional noise.

Constraint: Output ONLY the pure, updated Markdown string.

Testing: Test the prompt extensively in an LLM playground before integrating it into the codebase.

Phase 3: Wiring the Edge Pipeline (Hours 9 - 16)
Create Edge Function: Set up a Supabase Edge Function (process-context-update).

The Logic: 1. Receive uploaded text and property_id. 2. Query the Properties table for the current context_md. 3. Send both strings to the LLM API using the engineered prompt. 4. Overwrite the context_md column in the database with the LLM's response.

Connect UI: Map the file upload button in the React frontend to trigger this Edge Function.

Phase 4: Real-Time UI & The Agent Demo (Hours 17 - 21)
Enable Real-Time: Turn on Supabase Realtime for the Properties table.

UI Subscription: Ensure the React frontend auto-updates the Markdown viewer when the database changes, without requiring a page refresh.

Junior Agent Chat (Bonus): Add a chat window where a user can ask questions. The app invisibly prepends the context_md to the user's prompt, allowing the AI to answer contextually.

Phase 5: Pitch Prep and Fallbacks (Hours 22 - 24)
Code Freeze: Stop coding new features. Fix bugs.

Fallbacks: Save perfect "Before" and "After" states locally in case of API rate limits or internet failure during the demo.

The Pitch: Emphasize business value: Moving from stateless, batch-processed noisy data to a real-time, event-driven, token-efficient state management system for AI agents.
