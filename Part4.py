from bs4 import BeautifulSoup
import pandas as pd
import requests

content = requests.get('http://eduko.spikotech.com/Course').text

print(content)

soup = BeautifulSoup(content, 'lxml')
courses = soup.find_all('div')

for course in courses:
    course_name = course.find('h4', class_="card-title ")
    print(course_name)

