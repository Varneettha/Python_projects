is_hot = True
is_cold = True
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a nice day")
print("enjoy")

#activity
#Price of a house is 1M,if they have good credit, 10 percent down else 20 percent down,print down payment for the buyeer with good credit

house_price = 1000000
has_goodcredit = False
if has_goodcredit:
    down_payment=0.1*house_price
    print(f"Downpayment is 10 percent of 1M which is ${int(down_payment)}")
else:
    down_payment=0.2*house_price
    print(f"Downpayment is 20 percent of 1M which is ${int(down_payment)}")