# Reading inputs for product 1
code1, quantity1, price1 = input().split()
code1 = int(code1)
quantity1 = int(quantity1)
price1 = float(price1)

# Reading inputs for product 2
code2, quantity2, price2 = input().split()
code2 = int(code2)
quantity2 = int(quantity2)
price2 = float(price2)

# Calculating the total amount
total = (quantity1 * price1) + (quantity2 * price2)

# Printing the result with formatting
print(f"VALOR A PAGAR: R$ {total:.2f}")
