toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(list(toppings))
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizzas = list(zip(toppings, prices))
pizzas.sort()
print(pizzas)
cheapest_pizza = pizzas[1]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas [:2]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)