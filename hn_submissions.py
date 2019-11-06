import requests

from operator import itemgetter

#Call the API, Store the response
url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'
r = requests.get(url)
print('Status Code: ', r.status_code)

#Processing information from submissions
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids:
	url = (f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()

	submission_dict = {
		#'title': response_dict['title'],
		'link': 'http://news.ycombinator.com/item?id='+submission_id,
		#'comments': response_dict.get('descendants', 0),
		}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dict, key = itemgetter('comments'), reverse = True)

for submission_dict in submission_dicts:
	print('\nTitle:', submission_dict['title'])
	print('Discussion link:', submission_dict['link'])
	print('Comments:', submission_dict['comments'])