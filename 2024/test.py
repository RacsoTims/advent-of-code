coins = [1, 2, 5]
money = [0 for n in range(len(coins))]
total = sum([coins[n] * money[n] for n in range(len(money))])
target = 5
print(money)
count = 0
print(total)
for i in range(len(coins)):
    while money[i] < 3:
        money[i] += 1
        print(money)
    else:
        money[0:i+1] = [0 for x in money[0:i+1]]
