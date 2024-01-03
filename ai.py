# Import the os package
import os

# Import the openai package
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Set openai.api_key to the OPENAI environment variable
llm = OpenAI(openai_api_key = os.environ["OPENAI_API_KEY"])


template = """Based on my current wardrobe {clothesData}: Recommend me something for occassion {occassion}"""

prompt = PromptTemplate(template=template, input_variables=["clothesData","occassion"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

clothesData = {'red top, black pants'}
occassion = "formal"

print(llm_chain.run(clothesData, occassion))


# print(os.environ["OPENAI"])
