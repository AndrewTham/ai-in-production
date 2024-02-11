import gradio as gr

from chatbot import predict


def gradio_predict(message, history):
    yield next(predict(message, history))


gradio_app = gr.ChatInterface(
    fn=predict,
    textbox=gr.Textbox(placeholder="Chat with me!", container=False, scale=7),
    title="Chat Pal",
    description="A local chatbot to kill your boredom",
    theme="soft",
)
