import gradio as gr
from rag_chatbot_project import run_app

# Store chat history
chat_history = []

def chat(files, message, history):

    if history is None:
        history = []

    if message.strip() == "":
        return history, "", ""

    response = run_app(files, message)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})

    sources = "No source available"

    return history, "", sources


def clear_chat():
    return [], "", ""


with gr.Blocks(title="PDF RAG Chatbot") as demo:

    gr.Markdown("# 📄 Chat with your Documents")
    gr.Markdown(
        "Upload PDF files and ask questions. The assistant will answer using the document content."
    )

    with gr.Row():

        file_input = gr.File(
            label="Upload PDF files",
            file_types=[".pdf"],
            file_count="multiple",
            type="filepath"
        )

    chatbot = gr.Chatbot(
        label="messages",
        height=400
    )

    with gr.Row():

        msg = gr.Textbox(
            label="Ask a question",
            placeholder="Example: What is the notice period in the contract?"
        )

    with gr.Row():

        send_btn = gr.Button("Ask")
        clear_btn = gr.Button("Clear Chat")

    source_box = gr.Textbox(
        label="Source Documents",
        lines=4
    )

    send_btn.click(
        chat,
        inputs=[file_input, msg, chatbot],
        outputs=[chatbot, msg, source_box]
    )

    msg.submit(
        chat,
        inputs=[file_input, msg, chatbot],
        outputs=[chatbot, msg]
    )

    clear_btn.click(
        clear_chat,
        outputs=[chatbot, msg, source_box]
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )