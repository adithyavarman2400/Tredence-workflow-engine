TOOLS = {}

def register_tool(name, fn):
    TOOLS[name] = fn

def get_tool(name):
    return TOOLS[name]

