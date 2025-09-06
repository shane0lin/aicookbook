import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Define server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    # Establish stdio client connection
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection (perform handshake)
            await session.initialize()

            rst_tool = await session.call_tool("multiply", {"a": 6, "b": 7})
            print(f"Result of multiply tool: {rst_tool.content[0].text}")

            rst_resource = await session.read_resource("resource://health")
            print(f"Health resource: {rst_resource.contents[0].text}")

            rst_prompt = await session.get_prompt("welcome_user", {"username": "Alice"})
            print(f"Prompt: {rst_prompt.messages[0].content.text}")

if __name__ == "__main__":
    asyncio.run(main())