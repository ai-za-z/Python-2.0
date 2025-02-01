word = str(input("Write the word for which you need to find the letter..."))
 
for i in word:
    # print(i)
    if i == "a" or "A":
        print("A or a chracter is found...")
        break
    else:
        print("A or a chrracter is not found")