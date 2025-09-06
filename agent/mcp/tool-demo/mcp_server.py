from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="My Server",
    description="A simple MCP server with a multiplication tool, a health resource, and a welcome prompt."
)


# Multiply tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


# Health status resource
@mcp.resource("resource://health", description="Returns the current health status of the server.")
def health_status() -> str:
    """Returns the current health status of the server."""
    return "Server is healthy"


# Welcome prompt
@mcp.prompt()
def welcome_user(username: str) -> str:
    """Generate a personalized welcome message for the given username."""
    return f"Welcome, {username}! We're glad to have you here."


if __name__ == "__main__":
    mcp.run(transport="stdio")