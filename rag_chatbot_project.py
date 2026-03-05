
import os
from dotenv import load_dotenv
from src.loader import load_and_split_pdf
from src.database import create_or_load_index
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import warnings
from operator import itemgetter

warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module="langchain"
)

# Tokenizer / model warnings (Nemotron)
warnings.filterwarnings(
    "ignore",
    message=".*get_num_tokens_from_messages.*"
)

load_dotenv()

def run_app(path, question):
    print(type(question), question)
    question = str(question)
    chunks = load_and_split_pdf(folder_path=path)
    vectordb = create_or_load_index(chunks)

    llm = ChatOpenAI(
        model="nvidia/nemotron-3-nano-30b-a3b",
        temperature=0.2,
        max_tokens=1000
        )

    # memory = ConversationSummaryBufferMemory(memory_key="chat_history", return_messages=True,
    #                                       output_key="answer", llm=llm)

    chat_history = InMemoryChatMessageHistory()

    prompt = ChatPromptTemplate.from_template("""
        You are a helpful assistant.

        Context:
        {context}

        Chat History:
        {chat_history}

        Question:
        {question}

        Answer short and correct.
        If you don't know, say: I don't have the answer.
        """)

#    qa_chain = ConversationalRetrievalChain.from_llm(
 #       llm=llm,
  #      retriever=vectordb.as_retriever(),
   #     return_source_documents=True,
    #    combine_docs_chain_kwargs={"prompt": prompt}
     #   )

    rag_chain = (
        {
            "context": itemgetter("question") | vectordb.as_retriever(),
            "question": itemgetter("question"),
            "chat_history": itemgetter("chat_history")
        }
        | prompt
        | llm
        | StrOutputParser()
        | (lambda x: {"answer": x})
    )


    qa_chain_with_history = RunnableWithMessageHistory(
        rag_chain,
        lambda session_id: chat_history,
        input_messages_key="question",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

    
    print("Chat started. Type 'quit' to exit.\n")
    while True:
        # question = input("You: ")

        if question.lower() == "quit":
            response = "Thank you!"
            break
        
        response = qa_chain_with_history.invoke(
            {"question": question},
            config={"configurable": {"session_id": "default_user"}}
        )

        print(response['answer'])
        return response['answer']

# if __name__ == "__main__":
#    run_app()
