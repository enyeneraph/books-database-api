import requests, argparse

parser = argparse.ArgumentParser(description='Process an endpoint')
parser.add_argument('endpoint', metavar='N', type=str, help='and enpoint')

BASE_URL = 'http://127.0.0.1:5000/'
endpoint = parser.parse_args().endpoint
print(BASE_URL + endpoint)
response = requests.get(BASE_URL + endpoint).json()
print(response)


# create author 
{
    "name":"Peace Arthur",
    "location":"Uyo",
    "age":12,
    "gender":"M"
}

