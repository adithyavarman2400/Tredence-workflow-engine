from fastapi import FastAPI
from uuid import uuid4

from .engine import GRAPHS, RUNS, WorkflowEngine
from .models import GraphDefinition, RunRequest

app = FastAPI(title="Tredence Workflow Engine")

@app.post("/graph/create")
def create_graph(graph: GraphDefinition):
    graph_id = str(uuid4())
    GRAPHS[graph_id] = graph.dict()
    return {"graph_id": graph_id}

@app.post("/graph/run")
def run_graph(req: RunRequest):
    final_state, log = WorkflowEngine.run_graph(req.graph_id, req.initial_state)
    run_id = str(uuid4())

    RUNS[run_id] = final_state

    return {
        "run_id": run_id,
        "final_state": final_state,
        "execution_log": log
    }

@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return RUNS.get(run_id, {"error": "run_id not found"})

@app.get("/")
def home():
    return {"message": "Workflow Engine Running 🚀"}

