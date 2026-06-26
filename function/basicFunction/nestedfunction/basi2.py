def outer():
    x=10
    def inner():
        print("value of ",x)
    inner()

outer()