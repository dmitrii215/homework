def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    print(inner_function())
    pass
test_function()

# inner_function() Я не могу вызвать её вне функции test_function, т.к они в разных пространствах