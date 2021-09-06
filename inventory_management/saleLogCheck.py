import json
from prettytable import PrettyTable

# Reading the log file onto variable logs
file=open('sale_log.json','r')
readings=file.read()
file.close()
sale_logs=json.loads(readings)
logs = sale_logs['logs']

# Defining function Bill similar to the one in buy.py
def bill(cart):
  total_amount = 0
  total_quantity = 0
  table = PrettyTable(['product_id','name','price','quantity','total price'])
  for item in cart:
    if item.isnumeric():  
        table.add_row([item,cart[item]['name'],'₹' + str(int(cart[item]['price']/cart[item]['qty'])),cart[item]['qty'],'₹' + str(cart[item]['price'])])
        total_amount += cart[item]['price']
        total_quantity += cart[item]['qty']
  print('**************************** FOOBAR Enterprise **************************')
  print('Bill no: ', bill_no)
  print('date and time: ', cart['datetime'])
  print(table)
  print('Total Quantity: ',total_quantity)
  print('Total cost: ₹', total_amount)

# Get bill number and validate it 
while True:
    bill_no = input("Enter the bill number for which you need to check the logs:")
    if bill_no in logs.keys():
        break
    else:
        print("Enter valid bill number")

# Call the bill function
bill(logs[bill_no])        
