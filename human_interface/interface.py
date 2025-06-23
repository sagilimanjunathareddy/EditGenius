import gradio as gr
from human_interface.feedback_logger import log_feedback

def review_interface(text):
    log_feedback(text)
    return "Feedback saved."

def launch_ui():
    iface = gr.Interface(fn=review_interface, inputs="textbox", outputs="text")
    iface.launch()