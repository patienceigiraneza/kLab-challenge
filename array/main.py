items = [ {'name': 'Bike', 'price':100}, {'name': 'TV', 'price':200}, {'name': 'Album', 'price':10}, {'name': 'Book', 'price':5}, {'name': 'Phone', 'price':500}, {'name': 'Computer', 'price':1000}, ]


print("\n Answers of question 2:  ")
      # q2. cheapest
count = 0
cheap = 0
for item in items:
    if(item['price']<items[cheap]['price']):
        cheap = count
    count +=1
print(" A. The cheapest is: ", items[cheap]['name'])


# q2. Expensive
count = 0
exp = 0
for item in items:
    if(item['price'] > items[exp]['price']):
        cheap = count
    count += 1
print(" B. The most expensive is: ", items[exp]['name'])


# q3. Total
total = 0
for item in items:
    total = total + item['price']
print(" C. Total of all is: ", total)


# q3. Total
total = 0
for item in items:
    if(item['price']>=10):
        total = total + item['price']
print(" D. Total of all is (without price under 10) is : ", total)
