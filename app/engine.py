from typing import Dict, Any
from .workflows import NODES

GRAPHS = {}
RUNS = {}

class WorkflowEngine:

    @staticmethod
    def run_graph(graph_id: str, initial_state: Dict[str, Any]):
        graph = GRAPHS[graph_id]
        edges = graph["edges"]
        nodes = graph["nodes"]

        # execution log
        log = []

        all_nodes = set(nodes.keys())
        next_nodes = set(edges.values()) - {None}
        start_node = list(all_nodes - next_nodes)[0]

        state = initial_state
        current = start_node

        while current is not None:
            fn_name = nodes[current]
            node_fn = NODES[fn_name]

            state = node_fn(state)
            log.append(current)

            if current == "apply_rules" and state.get("anomaly_count", 0) > 5:
                current = "detect_anomalies"
            else:
                current = edges.get(current)

        def convert_state(state):
            state.pop("anomalies", None)
            state.pop("anomaly_count", None)


            clean = {}

            for key, value in state.items():

                if str(type(value)) == "<class 'pandas.core.frame.DataFrame'>":
                    clean[key] = value.to_dict(orient="list")

                elif "numpy" in str(type(value)):
                    clean[key] = value.item()

                elif isinstance(value, list):
                    clean[key] = [
                        v.item() if "numpy" in str(type(v)) else v
                        for v in value
                    ]

                else:
                    clean[key] = value

            return clean

        return convert_state(state), log




