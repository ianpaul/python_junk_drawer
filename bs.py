from bs4 import BeautifulSoup as bs
from requests import get
toot_limit = 3
url = 'https://mastodon.xyz/@ianpaul/'
response = get(url)
soup = bs(response.text, 'html.parser')

user_names = soup.find_all('span', class_= 'display-name__account')
name_list = []
for handle in user_names:
	raw_text = handle.text
	final = '@'.join(raw_text.split('@')[0:2])
	name_list.append(final)

# print(soup.prettify())

toot = soup.find_all('div', class_='status__content')
toot_list=[]
for i in toot:
	toot_list.append(i.text)

toot_print = 0
while toot_print != toot_limit:
	print(toot_list.pop(0).strip(), "by", name_list.pop(0).strip())
	toot_print += 1




#for toot, name in zip(toot_list, name_list):
#	print((toot), "by", (name))



