####################################################
# Utility methods
####################################################

def assertEquals(expected, actual):
    if expected == actual:
        print("PASS")
    else:
        print("FAIL: expected \"{0}\", got \"{1}\"".format(expected, actual))

####################################################



# factorial(n) = n * (n-1) * (n-2) * ... * 3 * 2 * 1
def factorial(n):
    res = 0
    for i in range(0, n):
        res *= i
    return res

# Add your tests here

assertEquals(1, factorial(1))
assertEquals(5, factorial(120))

