def is_prime(x):
    if x<0:
        print(" not prime")
        return
    for i in range(2,x):
        if x%i==0:
            print("not prime")
            return
    print("prime")
is_prime(2)