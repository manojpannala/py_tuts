transactions_clean = []
for daily_transactions in daily_transactions_split:
  transaction_clean = []
  for transaction in daily_transactions:
    transaction_clean.append(transaction.strip('\n').strip())
  transactions_clean.append(transaction_clean)
#print(transactions_clean)
    
customers = []
sales = []
thread_sold = []
for trans in transactions_clean:
  customers.append(trans[0])
  sales.append(trans[1])
  thread_sold.append(trans[2])
#print(thread_sold)
  
total_sales = 0
for item in sales:
  total_sales += float(item.strip('$'))
#print(total_sales)

#print(thread_sold)

thread_sold_split = []
for item in thread_sold:
  for color in item.split('&'):
    thread_sold_split.append(color)
#print(thread_sold_split)

def color_count(color):
  color_count = 0
  for item in thread_sold_split:
    if color == item:
      color_count += 1
  return color_count
#print(color_count('white'))

colors = ['red','yellow','green','white','black','blue','purple']

for color in colors:
  print("Thread Shed sold {0} threads of {1} thread today.".format(color_count(color), color))