# Import the os package
import os

# Import the openai package


from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Set openai.api_key to the OPENAI environment variable
 

llm = OpenAI(openai_api_key = os.environ["OPENAI_API_KEY"])


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.run(question))


# print(os.environ["OPENAI"])
print("end")
