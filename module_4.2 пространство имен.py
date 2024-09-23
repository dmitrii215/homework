def test_function():
    def inner_function():
        nonlocal()
        print('я в области видимости test_function')
    inner_function()