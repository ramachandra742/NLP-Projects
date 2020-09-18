import requests

response=requests.post('http://localhost:5000/predict',files={'file':open('review.txt','r')})

print(response.text)
