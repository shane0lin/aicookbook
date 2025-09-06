from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="My Server",
    description="A simple MCP server with a multiplication tool, a health resource, and a welcome prompt."
)


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


@mcp.resource("resource://health", description="Returns the current health status of the server.")
def health_status() -> str:
    """Returns the current health status of the server."""
    return "Server is healthy"

@mcp.prompt()
def welcome(username):
    """Say hello to user"""
    return f"Hello, {username}"
    


if __name__ == "__main__":
    mcp.run(transport="stdio")