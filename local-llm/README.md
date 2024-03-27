# Running LLM Locally

## Ollama

- [Download and install Ollama](https://ollama.com/download/mac)
- Pull an image: `ollama pull gemma:2b`
- Run an image: `ollama run gemma:2b`

## Local AI

[LocalAI](https://localai.io/)

```shell
docker pull localai/localai:latest-aio-cpu
docker run -p 8080:8080 --name local-ai -ti localai/localai:latest-aio-cpu`
```
