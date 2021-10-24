from math import prod


print("WELCOME TO THE TRIANGLE CALCULATOR")
pu_t = int(input("How many rows do you want? "))
pu_n = int(input("How many colums do you want? "))

def column_fucntion(width, height):
    for l in range(height):
        for i in range(width):
            print(".    ", end="")
        print()

column_fucntion(pu_t, pu_n)

Answer = input("Do you wanna see the answer? [Y/N]").lower()
if Answer == "y":
    product = int(pu_t*pu_n)
    # print(product)
    def fact(product):
 
        f = 1
     
        for i in range(2, product+1):
            f = f * i
         
        return f
    def nCr(product):
        print(fact(product) / (fact(3)*fact(product-3)))
    
    nCr(product)
else:
    print('welp')
