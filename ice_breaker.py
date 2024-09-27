from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """Morgan Freeman[2] (born June 1, 1937) is an American actor, producer, and narrator. Throughout a career spanning five decades, he has received numerous accolades, including an Academy Award, a Golden Globe Award, and a Screen Actors Guild Award as well as a nomination for a Tony Award. He was honored with the Kennedy Center Honor in 2008, an AFI Life Achievement Award in 2011, the Cecil B. DeMille Award in 2012, and Screen Actors Guild Life Achievement Award in 2018. He is widely regarded as one of the greatest actors of all time.[3][4]

Born in Memphis, Tennessee, Freeman was raised in Mississippi, where he began acting in school plays. He studied theater arts in Los Angeles and appeared in stage productions in his early career. He rose to fame in the 1970s for his role in the children's television series The Electric Company. Freeman then appeared in the Shakespearean plays Coriolanus and Julius Caesar, the former of which earned him an Obie Award. In 1978, he was nominated for the Tony Award for Best Featured Actor in a Play for his role as Zeke in the Richard Wesley play The Mighty Gents.

Freeman received the Academy Award for Best Supporting Actor for his role as a former boxer in Clint Eastwood's sports drama Million Dollar Baby (2004). He was Oscar-nominated for Street Smart (1987), Driving Miss Daisy (1989), The Shawshank Redemption (1994), and Invictus (2009). Other notable roles include in Glory (1989), Lean on Me (1989), Robin Hood: Prince of Thieves (1991), Unforgiven (1992), Se7en (1995), Amistad (1997), Gone Baby Gone (2007), and The Bucket List (2007). He also portrayed Lucius Fox in Christopher Nolan's The Dark Knight Trilogy (2005–2012) and starred in the action films Wanted (2008), Red (2010), Oblivion (2013), Now You See Me (2013), and Lucy (2014).

Known for his distinctive voice, he has narrated numerous documentary projects including The Long Way Home (1997), March of the Penguins (2005), Through the Wormhole (2010–2017), The Story of God with Morgan Freeman (2016–2019), Our Universe (2022) and Life on Our Planet (2023). He made his directorial debut with the drama Bopha! (1993). He founded film production company Revelations Entertainment with business partner Lori McCreary in 1996 where he produced numerous projects including CBS political drama Madam Secretary from 2014 to 2019."""

if __name__ == '__main__':
    summary_template =  """
        given the {information} from a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)