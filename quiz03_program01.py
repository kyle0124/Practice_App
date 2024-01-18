import json
import requests

# https://developers.naver.com/main/

# Naver API

client_id = 'aBSAwM5EwSu1poHZ8arW'
client_secret = 'QaHkIGB4ET'

keyword = '경제'
display_amount = 100
start_pos = 1
url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={display_amount}&start={start_pos}'


headers = {'X-Naver-Client-Id': client_id , 
           'X-Naver-Client-Secret':client_secret}

################################################################################

response = requests.get(url, headers=headers)

print(response.status_code)

# parsing
text = json.loads(response.text)

# keys
print(text.keys())

# print items
count = 1
for x in text['items'] :
    if 'n.news.naver' in x.get('link') :
        print('Count : ', count)
        print('Title : ', x.get('title'))
        print('Link : ', x.get('link'))
        print('Description : ', x.get('description'))
        print()
        count += 1

























