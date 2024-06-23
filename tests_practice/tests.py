def format_name(first, last, middle=''):
    try:
        return f"Your name: {first.lower().title()} {middle.lower().title() + ' ' if middle != '' else ''}{last.lower().title()}"
    except Exception as e:
        return e

# is_active = True
# while is_active:
#     first = input("What is your first name? ")
#     if first == 'q':
#         is_active = False
#         break
#     last = input("What is your last name? ")
#     middle = input("What is your middle name? ")
#     if 'q' in [first, last, middle]:
#         is_active = False
#     else:
#         print(format_name(first, last, middle))