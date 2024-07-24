import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_response(input):
    # Initialize the LLM
    llm = OpenAI(temperature=0.7)

    # Create a prompt template
    template = """
    You are a helpful AI assistant. Please respond to the following input:

    User Input: {user_input}

    Your response:
    """

    prompt = PromptTemplate(template=template, input_variables=["user_input"])

    # Create the LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(input)

    return response
    


