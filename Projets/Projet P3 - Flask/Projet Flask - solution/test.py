import requests
import json

url_quot = 'https://devapi.ai/api/v1/markets/quote'
url_srch = 'https://devapi.ai/api/v1/markets/search'
url_news = 'https://devapi.ai/api/v1/markets/news'
headers = {'Authorization': f'Bearer 348|DM49tvseqLVSdQRwr4JShRGRpjQkei8vTCettkaI'}
# 364|tMxOcJBN7iHOzd7pyXx9y3HaVW4LnyBY888Nzcu3
# 349|rCdDhONfV2yr9VV4ak9RahbONWlsyZEQBepOtH9Q
# 372|N1ypA5GwxENImOaQIKJNUruexgOnt1EHErEdXUN8

url = 'https://devapi.ai/api/v1/markets/quote'
params = {
  'ticker': 'AAPL',
}
headers = {
  'Authorization': 'Bearer 348|DM49tvseqLVSdQRwr4JShRGRpjQkei8vTCettkaI'
}

response = requests.request('GET', url, headers=headers, params=params)

print(response.json())