def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
inner_function()    # Вызвать не получится, ведь inner_function() в локальном пространстве test_function()