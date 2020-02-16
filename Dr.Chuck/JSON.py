import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retriving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
json_data = json.loads(data)
comment_count = len(json_data['comments'])
print ('Count:',comment_count)
comment_sum = 0
for comment in json_data['comments']:
        comment_sum = comment_sum + int(comment['count'])
print ('Sum: ' + str(comment_sum) + '...')
