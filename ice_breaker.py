from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_url, mock=True)
    summary_template =  """
        given the linkedin information {information} from a person I want you to create:
        1. a short summary
        2. two interesting facts about them

        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables="information",
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    


    res = chain.invoke(input={"information": linkedin_data})
    print(res)


if __name__ == '__main__':
   ice_break_with("Gustavo Duarte Menezes Goiânia")