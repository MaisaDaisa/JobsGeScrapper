import requests
from bs4 import BeautifulSoup
from Website import Website
from WebsiteDB import WebsiteDB

database = WebsiteDB("websitedb.db")

url = 'https://www.jobs.ge/?page=1&q=&cid=6&lid=&jid=1'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

sites = soup.find('table', style='width:100%;').find_all("a", class_='vip')

for site in sites:

    jobsite = f"https://www.jobs.ge{site.get('href')}"
    jobsoup = BeautifulSoup(requests.get(jobsite).content, 'html.parser')
    dtitle = jobsoup.find_all('td', {'class': 'dtitle'})

    name = dtitle[0].b.text.strip()
    description = jobsoup.find('td', {'style': 'padding-top:30px; padding-bottom:40px;'}).text.strip()
    company = dtitle[1].b.text.strip()

    dates = dtitle[2].find_all('b')
    upload_date = dates[0].text.strip()
    last_date = dates[1].text.strip()

    has_salary = "ანაზღაურება" and ('ლარი' or 'დოლარი') in description

    hr_email = 'Null'
    if "hr@" in description:
        starting = int(description.find("hr@"))
        ending = int(description.find(".ge"))
        hr_email = f"{description[starting: ending]}.ge"

    website = Website(name, description, company, upload_date, last_date, has_salary, hr_email)
    database.add_website(website)
