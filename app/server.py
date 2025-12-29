from mcp.server import Server
from app import resources, tools, prompt

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

@server.read_resource("info://project")
def project_info():
    return resources.project_info()

@server.get_prompt("system")
def system_prompt():
    return prompt.system_prompt()


def main():
    server.run()



