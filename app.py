import gradio as gr
from rag_chatbot_project import run_app

app = gr.Interface(
    fn = run_app,
    inputs = [gr.File(label="Upload PDF documents.",
                       file_types=[".pdf"],
                       file_count="multiple",
                       type="filepath"),
             gr.Textbox(label="Provide your question! Write 'Quit' to end the conversation.", 
                        placeholder="Type your question here...")],
    outputs = gr.Textbox(label="Bot Response.", lines = 10),
    title = "PDF RAG ChatBot",
    description = "Upload one or more PDFs and ask questions",
    api_name = "rag_app"
    )


if __name__ == "__main__":
    app.launch(share=True)
