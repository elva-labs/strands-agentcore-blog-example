# Strands & AWS Bedrock AgentCore example

This repo is an example repo used in the blog: <url>

## Requirements

- Python 3.13
- uv
- AWS Credentials
- (optional) docker or podman for local container building

## Getting started

1. Run `uv sync`
2. Activate venv via `source .venv/bin/activate`
3. Set your AWS Credentials as environment variables or similar
4. Run `un run main.py` to start the agent locally
5. Query the agent via curl or similar to get an streaming response:
   ```
   curl -X POST http://localhost:8080/invocations \
   -H "Content-Type: application/json" \
   -d '{"prompt": "Which tools do you have available?"}'
   ```
6. To skip the AgentCore framework, run the standalone.py directly to directly invoke the agent in your console. `uv run standalone.py`. Adjust the last line to play around with different questions like: `agent("What is the best color?")`

## Deployment

1. Adjust account in [.bedrock_agentcore.yaml](.bedrock_agentcore.yaml)
2. Make sure your AWS credentials is set and you are using a AgentCore supported region such as eu-west-1
3. run `uv run agentcore launch` to deploy the agent to AWS Bedrock AgentCore, after the deployment you can find your agent in the console
