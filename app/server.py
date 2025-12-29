from mcp.server import Server
from app import tools

server = Server(
    name="simple mcp server",
    version="0.0.1"
)

@server.tool()
def add_numbers(a: int, b: int):
    return tools.add_numbers(a, b)

@server.tool()
def health_ckeck():
    return 
