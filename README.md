# AI in Production

This is a Gradio application built on top of a FastAPI server, packaged in as a Docker service.

## Usage
Download the models from `https://huggingface.co/togethercomputer/RedPajama-INCITE-Chat-3B-v1/tree/main` into a folder called `models`.

In your command terminal, execute the following code:

```bash
docker-compose up -d --build
```

Thereafter, the UI will be accessible at `localhost:8000` by default

## System Requirements

Note that this repository is build and tested on a Windows machine.