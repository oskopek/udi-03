# factorial(n) = n * (n-1) * (n-2) * ... * 3 * 2 * 1
def factorial(n):
    res = 0
    for i in range(0, n):
        res *= i
    return res

# Add your tests here

def test_factiorial():
    assert 1 == factorial(1)
    assert 5 == factorial(120)

