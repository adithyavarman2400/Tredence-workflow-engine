from pydantic import BaseModel
from typing import Dict, Any, Optional

class GraphDefinition(BaseModel):
    nodes: Dict[str, str]     
    edges: Dict[str, Optional[str]]  

class RunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]

