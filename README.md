**TREDENCE WORKFLOW ENGINE**

**How to Run**

**step-1:** Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

**step-2:** Install dependencies:

pip install -r requirements.txt

**step-3:** Start the FastAPI server:

uvicorn app.main:app --reload

**step-4:** Use the interactive API docs to create and post graphs:

http://127.0.0.1:8000/docs

**What the Workflow Engine Supports**

1. Creating workflows as graphs with nodes and edges.

2. Executing the graph step-by-step with a shared state.

3. Clean JSON-safe state conversion (handles pandas/numpy).

4. Execution logs showing the order of steps.

5. A sample end-to-end data quality pipeline containing:

   profile data
   detect anomalies
   generate rules
   apply rules

**What I Would Improve With More Time**

1. Add support for branching / conditional nodes.

2. Add async execution for nodes requiring external I/O.

3. Persist graphs and runs in a database instead of in-memory.

4. Better error handling, retries, and workflow recovery.

5. UI for workflow graph visualization.

6. modular support and parallelization for node execution.


