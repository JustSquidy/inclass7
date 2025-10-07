import requests
import os

# ORDER_Status = '123456654321'

ORDER_STATUS_KEY = os.environ.get('ORDER_STATUS_KEY')
print(ORDER_STATUS_KEY)
order_number = input('Enter your order number: ') # You can make up a number

url = f'https://mock-order-status.uc.r.appspot.com/orders/status/{order_number}?API_KEY={ORDER_STATUS_KEY}'
response = requests.get(url).json()
print(response)

status = response['status']
print(f'Order status: {status}')
