#While and For loops

#while loop
# x=0
# while (x<5):
#     print(x)
#     x=x+1


#For loop
# for x in range(5,10):
#     print(x)


#array
days = ["mon", "tue", "wed", "thur", "fir", "sat", "sun"]
for d in days:
    # if (d=="fir"):break
    if (d=="fir"):continue
    print(d)
