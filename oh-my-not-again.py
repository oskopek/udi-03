####################################################
# Utility methods
####################################################

def assertEquals(expected, actual):
    if expected == actual:
        print("PASS")
    else:
        print("FAIL: expected \"{0}\", got \"{1}\"".format(expected, actual))

####################################################


def f(x):
    return x[-1] + f(x[:-1])

# Add your tests here

assertEquals("1", f("1"))

