import http.client
import gzip 

conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()

raw_data = response.read()

try:
    text = gzip.decompress(raw_data).decode('UTF-8')
except:
    text = raw_data.decode('UTF-8')

print(text)
conn.close()

"""
import http.client

conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()
text = response.read().decode('UTF-8')
print(text)
conn.close()
"""