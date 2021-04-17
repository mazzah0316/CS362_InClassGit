import random
import string

def rand_password(n):
    password = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(n)))
    print("Your Password of ",n, "lenght: ",password)

rand_password(7)
rand_password(3)