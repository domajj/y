import requests, re
from bs4 import BeautifulSoup

html = requests.get('https://itexamanswers.net/ccna-3-v7-modules-1-2-ospf-concepts-and-configuration-exam-answers.html')
soup = BeautifulSoup(html.text, "html.parser")

questions = soup.find_all('strong')

p = soup.select('p')[0]
print(p.find_all_next('strong'))

with open('result.txt', 'a', encoding='utf-8') as fs:
    for question in questions:
        
        readable_question = question.get_text().strip()
        
        if readable_question != 'Explanation:':
            fs.write('"' + readable_question + '"' + ',' + '\n')
            
        print(readable_question)