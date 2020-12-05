import requests

BASE_URL = 'https://galileoguzman.com/data/best_sellers.csv'

response = requests.get(BASE_URL)
response.raise_for_status()

response_content = response.content
filename = 'datasets/best_sellers.csv'

with open(filename, 'wb') as csv_file:
    csv_file.write(response_content)

print('File downloaded. :)')
