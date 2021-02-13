import pandas as pd
import requests
from bs4 import BeautifulSoup

url ="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/" #url

list=[] #list to store the table row
major =[] #list to store the major
degree=[] #list to store the degree
early_career=[] #list to store the early career pay
mid_career=[] #list to store the mid career pay
high_meaning=[] #list to store the high meaning

#Extracts the data from the website's tables
for page in range(1, 35):
    response = requests.get(f"{url}{page}")
    response.raise_for_status()
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    major_element = soup.find_all(class_="csr-col--school-name")
    all_numbers = soup.find_all(class_="csr-col--right")
    list_one = soup.find_all('tr')

#Cleans the data
    for i in list_one:
        list.append(i.getText().replace("Rank:", "").replace("Major", "").replace("Degree Type", "")
                    .replace("Early Career Pay", "").replace('Mid-Career Pay', "").replace("High Meaning", "").
                    replace('Rank% ', ""))

    filtered_data = [x for x in list if x != ""]

#Split the data and appends them to the appropriate categories
for i in filtered_data:
    major.append(i.split(':')[1])
    degree.append(i.split(':')[2])
    early_career.append(i.split(':')[3])
    mid_career.append(i.split(':')[4])
    high_meaning.append(i.split(':')[5])


columns = ['Major', 'Degree', 'Early-Career Pay', 'Mid-Career Pay', '% High Meaning']
master_list = [major, degree, early_career, mid_career, high_meaning]

#Turn the data into a data frame, so it can be prep as a csv
df = pd.DataFrame({'Major': major, 'Degree': degree, 'Early-Career Pay': early_career, 'Mid-Career Pay': mid_career, '% High Meaning': high_meaning})

df.to_csv('major_data.csv', index=False)