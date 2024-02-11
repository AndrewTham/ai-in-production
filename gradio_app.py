import gradio as gr

from predict import predict


def gradio_predict(question: str):
    return predict(question)


gradio_app = gr.Interface(
    fn=gradio_predict,
    inputs=gr.Textbox(label="Ask a question", placeholder="Whatsup?"),
    outputs=[gr.Textbox(label="Answer")],
    allow_flagging="never",
)
