import requests, re
from bs4 import BeautifulSoup

html = requests.get('https://itexamanswers.net/ccna-2-v7-modules-10-13-l2-security-and-wlans-test-online.html')
soup = BeautifulSoup(html.text, "html.parser")

questions = soup.find_all('div', {'class' : 'wpProQuiz_question_text'})

readable_questions = []

with open('result.txt', 'a', encoding='utf-8') as fs:
    for question in questions:
        
        after = question.next_sibling
        print(after)
        
        readable_question = question.get_text().strip()
        
        if readable_question != 'Explanation:':
            fs.write('"' + readable_question + '"' + ',' + '\n')
            
        #print(question)