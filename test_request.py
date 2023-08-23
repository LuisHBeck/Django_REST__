import requests

headers = {'Authorization': 'Token 8822b738f4db5afa9fd75b11237cf0eab9457cec'}

base_ratings_url = 'http://127.0.0.1:8056/api/v2/ratings/'
base_courses_url = 'http://127.0.0.1:8056/api/v2/courses/'

result = requests.get(url=base_courses_url, headers=headers)

# testing if the endpoint is correct
assert result.status_code == 200
