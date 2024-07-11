string = 'A man, a plan, a canal: Panamae'
string = string.lower()
string_arr = [char for char in string if char.isalnum()]
print(string_arr)
s = set()