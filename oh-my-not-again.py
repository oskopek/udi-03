def f(x):
    return x[-1] + f(x[:-1])

# Add your tests here
def test_f():
    assert "1" == f("1")

