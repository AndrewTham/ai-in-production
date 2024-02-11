import gradio as gr

from fastapi_app import fastapi_app
from gradio_app import gradio_app

app = gr.mount_gradio_app(fastapi_app, gradio_app.queue(), path="/ui")
