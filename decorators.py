def outer_function():
    message='hi'
    def inner_function():
        print(message)
    return inner_function
outer_function()