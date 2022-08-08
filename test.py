import requests
from bs4 import BeautifulSoup
 
test_subject = "mythology"

query = test_subject
 
url = 'https://en.wikipedia.org/w/api.php'
params = {
            'action':'query',
            'format':'json',
            'list':'search',
            'utf8':1,
            'srsearch':query
        }
 
data = requests.get(url, params=params).json()
 
for i in data['query']['search']:
    print(i['title'], ' - Word count: ', i['wordcount'])


 
subject = test_subject
 
url = 'https://en.wikipedia.org/w/api.php'
params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
            'prop':'text',
            'redirects':''
        }
 
response = requests.get(url, params=params)
data = response.json()
 
raw_html = data['parse']['text']['*']
soup = BeautifulSoup(raw_html,'html.parser')
soup.find_all('p')
text = ''
 
for p in soup.find_all('p'):
    text += p.text
 
print(text[:58])
print('Text length: ', len(text))

query = test_subject
db_q = query.replace(' ', '_')
db = 'http://dbpedia.org'
url = db + f'/data/{db_q}.json'
data = requests.get(url).json()
data