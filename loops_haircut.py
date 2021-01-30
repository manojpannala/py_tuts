hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
total_price = 0

# Price and Cuts:
prices = [30, 25, 40, 20, 20, 35, 50, 35]

for price in prices:
  total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price:",average_price)

new_prices = [prices - 5 for prices in prices]
print(new_prices)

# Revenue
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue = prices[i] + last_week[i]
  print("Total Revenue:",total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1)]
print(cuts_under_30)