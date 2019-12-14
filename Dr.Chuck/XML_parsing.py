import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


url = input('Enter location: ')
print('Retriving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
xml = ET.fromstring(data)
counts = xml.findall('.//count')
print ('Count: ', str(len(counts)))

sum = 0
for count in counts:
    sum = sum + int(count.text)
print ('Sum: %s', sum)
