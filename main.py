import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# Uncomment this line to see what you got
# print(page.text)

#Create a BeautifulSoup object
soup = BeautifulSoup(page.content, "html.parser")

# Finding elements
job_titles = soup.find_all("h2", class_="title is-5")
company_names = soup.find_all("h3", class_="subtitle is-6 company")
jobs = []
companys = []

for title, company in zip(job_titles, company_names):
    jobs.append(title.text)
    companys.append(company.text)

# You can uncomment if you want to see the scraped content
# print(job_titles)
# print(company_names)
# print(jobs)
# print(companys)

print('Filter by class')
res1 = dict(zip(jobs, companys))
print('\n Dict with key job title and value company name:')
print(f'\n {res1}')

print('\n Filter by content')
res2 = soup.find_all("h2", string=lambda text: "python" in text.lower())
print('We got a (ResultSet), a set of Beautiful Soup objects corresponding to <h2> tags respectively')
print(f'\n {res2}')

# Convert Beautiful Soup objects to strings to create a new BeautifulSoup object
res2_strings = [str(tag) for tag in res2]

# Create the object
soup2 = BeautifulSoup(''.join(res2_strings), 'html.parser')

# Get the content of the filtered <h2> elements
h2_cont = []
for h2_tag in soup.find_all('h2', class_='title is-5'):
    h2_content = h2_tag.get_text(strip=True)
    h2_cont.append(h2_content)

print('\n Cleaning the data:')
print(f'\n {h2_cont}')
print('\n Filter by word content (e.g. python)')

# h2_tag_python is a list of Beautiful Soup objects
# that meet the criteria of containing the word "python"
h2_tag_python = [tag for tag in res2 if "python" in tag.get_text(strip=True).lower()]

# h2_cont_py is a list containing only the text of the <h2> elements
h2_cont_py = [tag.get_text(strip=True) for tag in h2_tag_python]
print(f'\n {h2_cont_py}')