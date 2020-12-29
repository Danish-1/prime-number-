def fn(x):
    # check from 2 to given number
    for i in range(2, x):
        # not prime condition
        b = x % i
        if b == 0:
            # return true for not prime
            return True


# take an integer from user
a = int(input("enter a number to check it is prime or not: "))
# if return is true print not prime otherwise prime
if fn(a):
    print("not prime")
else:
    print("prime")
