amount = int(input("Enter the amount"))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(f"your amount is Rs.{amount}/-")


n2000 = amount // 2000
amount %= 2000

n1000 = amount // 1000
amount %= 1000

n500 = amount // 500
amount %= 500

n200 = amount // 200
amount %= 200

n100 = amount // 100
amount %= 100

n50 = amount // 50
amount %= 50

n20 = amount // 20
amount %= 20

n10 = amount // 10
amount %= 10

coins = amount


print(f"2000 x {n2000} = Rs. {2000*n2000}/-")
print(f"1000 x {n1000} = Rs. {1000*n1000}/-")
print(f"500 x {n500} = Rs. {500*n500}/-")
print(f"200 x {n200} = Rs. {200*n200}/-")
print(f"100 x {n100} = Rs. {100*n100}/-")
print(f"50 x {n50} = Rs. {50*n50}/-")
print(f"20 x {n20} = Rs. {20*n20}/-")
print(f"10 x {n10} = Rs. {10*n10}/-")
print(f"Coins = Rs. {coins}")