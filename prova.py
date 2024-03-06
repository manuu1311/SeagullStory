def printer():
    print("we")
    yield
    print("bro")
    yield
    print("come la va")

b=printer()
for _ in range(10):
    b.__next__()