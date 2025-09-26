The LangGraph agent

Weather MCP Server



# Dependencies:
```
pip install mcp
pip install langchain
pip install langgraph
pip install langchain-google-genai
pip install langchain-mcp-adapters
```

* __mcp__: This is the official Python SDK for the MCP, enabling our client to connect to the server.

* __langchain__: The core framework that provides the foundational components for building our LLM-powered application.

* __langgraph__: This library is used to construct our agent as a stateful graph, which is essential for managing tool invocation cycles.

* __langchain-google-genai__: This adapter package allows us to integrate and use Google’s generative AI models (like Gemini) as the brain for our agent.

* __langchain-mcp-adapters__: This library bridges LangChain with MCP, providing helper functions to load server tools directly into our agent.

# Best practices for project structure for MCP-enabled applications
While our simple file setup works for this example, adopting robust software engineering practices early is crucial for building scalable and maintainable agentic systems. Beyond the directory structure, we recommend the following practices:

* __Maintain separation of concerns:__ The server’s code should only contain logic related to its specific tool (e.g., calling the weather API). The client’s code should focus exclusively on agentic logic and orchestration. This clear division makes the system easier to debug, test, and extend.

* __Manage configuration and secrets:__ Avoid hardcoding sensitive information like API keys directly in the code. Instead, use environment variables (often managed with a .env file) to handle configuration. This is more secure and makes it easier to switch between development and production environments.

* __Write descriptive tool definitions:__ The function names and docstrings for your tools are critical. The @mcp.tool() decorator uses them to generate the schema and description that the agent’s LLM uses for tool selection. Clear and descriptive definitions lead to more reliable agent behavior.

* __Implement robust error handling:__ As highlight in our server, tools should contain their own error handling (e.g., try...except blocks). A tool should never crash the entire server process. Instead, it should catch exceptions and return a structured error message that the agent can potentially use or report to the user.