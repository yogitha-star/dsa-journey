# buying and selling stock
prices=[7,1,5,3,6,4]
buy=prices[0]
max_profit=0
for i in range(len(prices)):
    if prices[i]<buy:
        buy=prices[i]
    profit= prices[i] - buy
    if profit>max_profit:
        max_profit=profit
print(max_profit)            
     