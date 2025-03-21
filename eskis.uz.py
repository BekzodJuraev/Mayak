import requests

url = "https://notify.eskiz.uz/api/message/sms/send"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQzNzU3NDMsImlhdCI6MTc0MTc4Mzc0Mywicm9sZSI6InRlc3QiLCJzaWduIjoiYWY0MWI3Y2U0Yzg2MzY3YTJmNmIxMDI3OWEyNmRjODljNWJjYThhYjcxZjEwMjg2NTAwMGQ4M2UxYjE2Mjc4MCIsInN1YiI6IjEwMDkzIn0.tAlKryrsmqtk1BTl1d640a2LP1Lhh49uCTN8GqCrlbw"

payload = {
    'mobile_phone': '906566970',
    'message': 'как дела',
    'from': 'Mayak',
}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
