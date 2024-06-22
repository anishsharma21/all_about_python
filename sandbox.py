def wontrun():
    name = input("What is your name? ")
    print(name.title())
    print(name.upper())
    print(name.lower())
    universe_age = 4_000_000_000
    print(universe_age)
    arr = [4, 2, 66, 3, 2342, 6]
    popped_value = arr.pop(2)
    print(popped_value)
    # import this command when the python interpreter is running
    long_list = list(range(1000001))
    print(sum(long_list))

    cubes = [value**3 for value in range(11)]
    print(cubes)

    arr = [4, 2, 4, 22, 1, 43, 46, 23, 12, 3]
    print(arr[::2])
    print(arr[::-1])
    arr[1:3] = (99, 95)
    print(arr)

    # tuples are an immutable list - a list of values that cannot change

    dict = {
        'anish': 'go',
        'jack': 'rust',
        'emily': 'python'
    }

    print(dict.get('anish'))
    print(dict.get('ron')) # will return None and not throw error
    # print(dict['ron']) this would throw a KeyError
    print(dict.get('ron', 'key not found')) # returns the second parameter if key not present

    dict_keys = list(dict.keys())
    print(dict_keys)

    # you can't sort a dictionary but you can sort the keys and get the values from there
    for key in sorted(dict_keys):
        print(dict[key]) # should be go, python then rust

    dict_values = dict.values()
    print(list(dict_values))

    # since values can be repeated, we can use set to get distinct values
    new_dict = {
        'jack': 'python',
        'will': 'python',
        'emily': 'rust',
        'tim': 'go',
        'mark': 'rust'
    }
    print(set(new_dict.values()))

    # set syntax uses curly brackets but no colons
    my_set = {'rust', 'g', 'python'}
    # sets do not have order unlike dictionaries and lists


    def multiple_arguments(*toppings):
        print(type(toppings)) # tuple
        print(toppings)

    arguments = multiple_arguments('mushroom', 'tomato', 'chilli')

    def multiple_arguments_many(size, *toppings):
        print(size)
        print(toppings)

    multiple_arguments_many('small', 'mushroom', 'jalapenos')
    
    def user_information(first, last, **user_info):
        print(f"{first.title()} {last.title()}")
        for info in user_info: #user_info is actually a dictionary so this prints keys
            print(info)
        for info in user_info.values(): #this prints values of the dictionary
            print(info)

    user_information('anish', 'sharma', age=20, location='australia')

    print("My list:\n\t-hi")