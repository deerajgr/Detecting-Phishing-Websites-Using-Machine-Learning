import os
import requests  as re
from bs4 import BeautifulSoup
URL = "https://www.kaggle.com"
response = re.get(URL)
print("response -->", response, "\ntype -->", type(response))
print("text -->", response.text, "\ncontent -->",response.content,"\nstatus_code -->", response.status_code)

if response.status_code !=200:
    print("HTTP connection is not successful! Try again")
else:
    print("HTTP connection is successful!")

soup = BeautifulSoup(response.content, "html.parser")
print("Title with tags -->", soup.title, "\nTitle without tags -->",soup.title.text) 

for link in soup.find_all("link"):
    print(link.get("href"))

print(soup.get_text())

# 1 CREATE A FOLDER TO SAVE HTML FILES

folder = "mini_dataset"

if not os.path.exists(folder):
    os.mkdir(folder)

# 2 DEFINE A FUNCTION THAT SCRAPES AND RETURNS IT
def scrape_content(URL):
    response = re.get(URL)
    if response.status_code == 200:
        print("HTTP connection is successful! for the URL",URL)
        return response
    else:
        print("HTTP connection is NOT successful! for the URL:", URL)
        return None
    
# 3 DEFINE  FUNCTION TO SAVE A HTML FILE OF THE SCRAPED WEBPAGE IN A DIRECTORY
path = os.getcwd() + "/" + folder

def save_html(to_where, text, name):
    file_name = name + ".html"
    with open(os.path.join(to_where, file_name), "w", encoding="utf-8") as f:
        f.write(text)
test_text =response.text
save_html(path,test_text,"example")
# 4 DEFINE A URL LIST VARIABLE
URL_list = [
    "https://www.kaggle.com",
    "https://stackoverflow.com",
    "https://www.researchgate.net",
    "https://www.python.org",
    "https://www.w3schools.com",
    "https://wwwen.uni.lu",
    "https://github.com",
    "https://scholar.google.com",
    "https://www.mendeley.com",
    "https://www.overleaf.com"
]
# 5 DEFINE A FUNCTION WHICH TAKES THE URL LIST AND RUN STEP 2 AND STEP 3 FOR EACH URL
def create_mini_dataset(to_where, URL_list):
    for i in range(0, len(URL_list)):
        content = scrape_content(URL_list[i])
        if content is not None:
            save_html(to_where, content.text, str(i))
        else:
            pass
    print("Mini dataset is created!")


create_mini_dataset(path, URL_list)
# 6 CHECK IF YOU HAVE 10 DIFFERENT HTML FILES