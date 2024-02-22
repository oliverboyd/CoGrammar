total_stock = 0
menu = ['croissant', 'bagel', 'sandwich', 'scone']
stock = {'croissant': 5,
         'bagel': 4,
         'sandwich': 10,
         'scone': 6}
price = {'croissant': 0.85,
         'bagel': 1.25,
         'sandwich': 1.50,
         'scone': 0.50}
for item in menu:
    total_stock += stock[item]*price[item]
print(total_stock)