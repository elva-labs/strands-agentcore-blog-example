from strands import Agent
from strands_tools.browser import AgentCoreBrowser
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient
from bedrock_agentcore import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
aws_knowledge_mcp = MCPClient(
    lambda: streamablehttp_client("https://knowledge-mcp.global.api.aws")
)

browser_tool = AgentCoreBrowser(region="eu-west-1")


@app.entrypoint
async def agent_invocation(payload):
    """Handler for agent invocation"""
    user_message = payload.get(
        "prompt",
        "No prompt found in input, please guide customer to create a json payload with prompt key",
    )

    # Create an agent with MCP tools
    with aws_knowledge_mcp:
        # Get the tools from the MCP server
        aws_knowledge_tools = aws_knowledge_mcp.list_tools_sync()

        # Combine the browser tool with the MCP tools
        tools = [browser_tool.browser] + aws_knowledge_tools

        agent = Agent(tools=tools)
        stream = agent.stream_async(user_message)
        async for event in stream:
            yield (event)


if __name__ == "__main__":
    app.run()
