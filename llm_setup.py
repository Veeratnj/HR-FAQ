from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

def setup_llm(model="deepseek-r1:7b"):
    llm = Ollama(model=model)
    

    ##temp prompt for summary
    prompt_template = """
            <|start_of_prompt|>
            You are an advanced AI assistant designed to help employees with HR-related queries.

            Use only the information provided in the context to answer the employee's question. Be polite, clear, and professional.

            Context:
            {context}

            Employee Question:
            {question}

            Instructions:
            - Provide a step-by-step answer if the process is available in the context.
            - If the answer is not found in the context, reply: "I'm sorry, I do not have that information at the moment. Please contact the HR department."
            AI Response:
"""
    
    prompt = PromptTemplate.from_template(prompt_template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    return llm_chain



