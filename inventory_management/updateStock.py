import json

# Read the products json file and store it in variable products as a dictionary
file=open('productlist.json','r')
readings=file.read()
file.close()
products=json.loads(readings)

# Defining funciton register which appends the products
def register():
    # Taking product id and validating it 
    product_id = input('enter product id: ')
    if not product_id.isnumeric():
        print('enter valid product ID')
        register()

    # If product id already exists then just take quanitty and add it to previous value    
    if product_id in products.keys():
        while True:
            quantity = input('Enter quantity of product: ')
            if quantity.isnumeric():
                products[product_id]['qty'] += int(quantity)
                break
            else:
                print("Enter valid quantity")

    # Else take all attributes for that product and validate it accordingly        
    else:
        name = input('enter product name: ')
        while True: 
            price = input('enter product price: ')
            if price.isnumeric():
                price = int(price)
                break
            else:
                print("enter valid price")

        while True:        
            quantity = input('Enter quantity of product: ')
            if quantity.isnumeric():
                quantity = int(quantity)
                break
            else:
                print('enter valid quantity')

        while True:        
            weight = input('Enter weight of product in grams: ')
            if weight.isnumeric():
                weight = int(weight)
                break
            else:
                print("enter valid weight")
        products[product_id] = {}
        products[product_id]['name'] = name
        products[product_id]['price'] = price
        products[product_id]['qty'] = quantity
        products[product_id]['weight'] = weight

# Calling the register function 
register()

# Updating the productlist.json file
readings=json.dumps(products)
file=open('productlist.json','w')
file.write(readings)
file.close()
