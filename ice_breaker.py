
import sys
import os
sys.path.append(os.path.abspath('/home/gduartemenezes/gdm-software/ai/ice_breaker'))

from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    summary_template =  """
        given the linkedin information {information} from a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    
    linkedin_data = scrape_linkedin_profile("Gustavo Duarte")

    res = chain.invoke(input={"information": linkedin_data})

    print(res)