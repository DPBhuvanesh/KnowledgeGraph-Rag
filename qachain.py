from graph import *
from retrieval import *

from langchain.prompts import (
    PromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    ChatPromptTemplate
)

from langchain.chains import RetrievalQA


def chat_template():
 vector_chat_template = """
    You are a friendly and insightful data analyst chatbot specializing in video game sales and details. 
Use the provided context to answer user questions about games, including rank, publisher, description, global sales, and regional sales (NA for North America, EU for Europe, JP for Japan, Other for other regions).

If requested, help to:
- Calculate percentages (e.g., share of sales by region)
- Compare sales between games or regions
- Find sales balances or differences across regions

Present your answers using:
- **Bullet points** for key facts
- **Bold** or *highlight* important data (use markdown-style formatting)
- Good line spacing and clear structure for easy reading
- A rich vocabulary and friendly, conversational tone

Never repeat that information is missing or unavailable more than once; instead, pivot to sharing relevant context or insights.
    context = {context}
"""
 
 human_chat_template = """
    can you provide answer and detail on :{question}?
    """
 return human_chat_template,vector_chat_template

human_template,system_template=chat_template()

def prompt():
    system_prompt = SystemMessagePromptTemplate(
        prompt=PromptTemplate(
            template=system_template,
            input_variables=['context']
        )
    )

    human_system_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=human_template,
            input_variables=['question']
        )
    )

    messages = [system_prompt,human_system_prompt]

    qa_prompt = ChatPromptTemplate(
        messages=messages,
        input_variables=['context','question']
    )
    
    qa_chain =RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_base.as_retriever(),
    chain_type = 'stuff'
    )
    
    qa_chain.combine_documents_chain.llm_chain.prompt = qa_prompt

    return qa_chain
    
chain = prompt()

