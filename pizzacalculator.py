# calculator of pizza

number_of_pizza = eval(input("how many pizzas do you wants?\n"))

cost_per_pizza =eval(input("how much does pizza cost\n"))

subtotal = number_of_pizza * cost_per_pizza

tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = sales_tax + subtotal

print("the total coast is ", total)
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tax, "in sale tax") 

