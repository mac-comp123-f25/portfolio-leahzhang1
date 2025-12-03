money = 732   #money in cents
print ("Making change for 732 cents:")
dollars = 732//100
print("Dollars:", dollars)
quarters = (money % 100) // 25
print("Quarters:", quarters)
dimes = (money % 100 - 25) // 10
print("Dimes:", dimes)
nickels = (money % 100 - 25) // 5
print("Nickels:", nickels)
pennies = money % 100 - 25 - 5
print("Pennies:", pennies)