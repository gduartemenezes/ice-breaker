import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn Profiles"""
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/gduartemenezes/18266f79e78a78fe18e25ab4af1d840d/raw/88f667ee1c069e11e210e8a2b51f81ce8bfc9132/profile.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else: 
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10
        )
    data = response.json()
    return data


if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/gduartemenezes",
            mock=True
        )
    )