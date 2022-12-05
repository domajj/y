import requests, re
from bs4 import BeautifulSoup

html = requests.get('https://itexamanswers.net/ccna-2-v7-modules-10-13-l2-security-and-wlans-exam-answers.html')
soup = BeautifulSoup(html.text, "html.parser")

questions = soup.find_all('strong')

with open('result.txt', 'a', encoding='utf-8') as fs:
    for question in questions:
        
        readable_question = question.get_text().strip()
        
        if readable_question != 'Explanation:':
            fs.write('"' + readable_question + '"' + ',' + '\n')
            
        print(readable_question)