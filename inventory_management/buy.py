import json
from datetime import datetime
from prettytable import PrettyTable

# Read the products json file and store it in variable products as a dictionary
file=open('productlist.json','r')
readings=file.read()
file.close()
products=json.loads(readings)

# Read the logs json file and store it in variable readings as a dictionary
file=open('sale_log.json','r')
readings=file.read()
file.close()
sale_logs=json.loads(readings)
sale_logs['billNo'] += 1 
bill_no = sale_logs['billNo']

# List of all possible yes and no
YES = ['y','Y','yes','Yes','YES']
NO = ['n','N','no','No','NO']

# Variable to store transaction id
TRANSACTION_ID = 0

# Declaring cart 
cart = {}

# Checkout Function
def checkout():
  
  # Ask if the customer wants to checkout or continue shopping
  customer_decision = input('Type Y if you want to checkout or Type N if you want to continue shopping: ')
  if(customer_decision in YES):
    return True 
  elif(customer_decision in NO):
    return False
  else:
    print('Invalid selection')
    return checkout()

# Definig function bill that prints the bills
def bill(cart):
  total_amount = 0
  total_quantity = 0
  table = PrettyTable(['product_id','name','price','quantity','total price'])
  for item in cart:
    print(item)
    table.add_row([item,cart[item]['name'],'₹' + str(int(cart[item]['price']/cart[item]['qty'])),cart[item]['qty'],'₹' + str(cart[item]['price'])])
    total_amount += cart[item]['price']
    total_quantity += cart[item]['qty']
  print('**************************** FOOBAR Enterprise **************************')
  print('Bill no: ', bill_no)
  print(table)
  print('Total Quantity: ',total_quantity)
  print('Total cost: ₹', total_amount)     

# Defining bill print
def billprint():
  if(checkout()):

    # Adding log to the sale_log.json
    now = datetime.now()
    sale_logs['logs'][bill_no] = cart

    # Calling bill function with cart as the paramter to it
    bill(cart)

    sale_logs['logs'][bill_no]['datetime'] = now.strftime("%d/%m/%Y %H:%M:%S")
    sales=json.dumps(sale_logs)
    file=open('sale_log.json','w')
    file.write(sales)
    file.close()

    print('thank you, Vist again')
    return 0
  else:
    return buy()

# Defining update_products functions which updates the existing productlist file
def update_products(products):
  readings=json.dumps(products)
  file=open('productlist.json','w')
  file.write(readings)
  file.close()

 

# Defining buy function 
def buy():
  # Requesting for product from customer
  product_id = input('Enter Product ID:')

  # Validating if the product exists
  if product_id not in products.keys():
    print('invalid ID')
    return buy()

  # Validating if the stock of the product is present
  if products[product_id]['qty'] == 0:
    print('out of stock')
    return buy()

  # Iterating again to get the quantity the customer wants  
  while True:
    quantity = int(input('Enter quantity:'))
    if quantity < 1:
      break

    # Validating if quanity of the product is available for sale
    if products[product_id]['qty'] < quantity:
      print('Not enough Stock, only', products[product_id]['qty'], 'left')
      print('Pls enter a valid quantity')
    else:
      break
  
  # Adding the item into cart
  # checking if the products already in cart  
  
  if quantity > 0:
    if product_id not in cart.keys():
      cart[product_id] = {}
      cart[product_id]['name'] = products[product_id]['name']
      cart[product_id]['qty'] = quantity
      cart[product_id]['price'] = cart[product_id]['qty'] * products[product_id]['price']
    
    else:
      cart[product_id]['qty'] += quantity
      cart[product_id]['price'] = cart[product_id]['qty'] * products[product_id]['price']

    # Removing quantity amount of product form products
    products[product_id]['qty'] -= quantity
    update_products(products)

  # Calling Checkout function
  billprint()  

# Displaying all the products
table = PrettyTable(['Product ID', 'Name', 'price', 'quantity', 'Weight in grams'])
for product in products:
  table.add_row([product,products[product]['name'],'₹' + str(products[product]['price']),products[product]['qty'],products[product]['weight']])
print(table)  
# Calling buy function
buy()

      