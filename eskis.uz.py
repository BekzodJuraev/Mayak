import requests

url = "https://notify.eskiz.uz/api/message/sms/send"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQzNzU3NDMsImlhdCI6MTc0MTc4Mzc0Mywicm9sZSI6InRlc3QiLCJzaWduIjoiYWY0MWI3Y2U0Yzg2MzY3YTJmNmIxMDI3OWEyNmRjODljNWJjYThhYjcxZjEwMjg2NTAwMGQ4M2UxYjE2Mjc4MCIsInN1YiI6IjEwMDkzIn0.tAlKryrsmqtk1BTl1d640a2LP1Lhh49uCTN8GqCrlbw"
name="Anton"
payload = {
    'mobile_phone': '+906566970',
    'message': f'Уважаемый {name}, ваш заказ принят. Для уточнения деталей и завершения оформления просим вас связаться с нами по телефонам +998 77 232 44 88, +998 91 313 11 14 в период с 09:00 до 20:00. Спасибо за ваш выбор!',
    'from': 'Mayak',
}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
