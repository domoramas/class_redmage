# practice02.py

# Problem 1
# def string_doubler(string_to_double):
#     new_string = ""
#     for i in string_to_double:
#         new_string += i + i
#     return new_string

# blah = "make this double"

# double_blah = string_doubler(blah)
# print(double_blah)

# Problem 2
# def missing_letter(string_to_wonkify):
#     new_list = []
#     out_list = []
#     for letter in string_to_wonkify:
#         new_list.append(letter)
#     for i in range(len(new_list)):
#         mid_list = new_list.copy()
#         mid_list.pop(i)
#         new_string = "".join(mid_list)
#         out_list.append(new_string)
#     return out_list

# not_wonky_string = "kitten"

# wonky_string = missing_letter(not_wonky_string)

# print(wonky_string)

# Problem 3
# def order_string(string_to_order):
#     new_list = []
#     for i in string_to_order:
#         new_list.append(i)
#     new_list.sort()
#     return new_list[-1]


# letters = "pneumonoultramicroscopicsilicovolcanoconiosis"

# last_letter = order_string(letters)

# print(last_letter)

# Problem 4
# def string_finder(big_string, string_to_find):
#     return big_string.count(string_to_find)

# bigstring = "hi hi hi hihihi hi hihihi"
# search_string = "hi"
# print(string_finder(bigstring, search_string))

# Problem 5
# def cat_dog_counter(catdog_string):
#     catcount = catdog_string.count("cat")
#     dogcount = catdog_string.count("dog")
#     if catcount == dogcount:
#         return True
#     else:
#         return False

# user_string = "catdogdogcatcatdog"
# print(cat_dog_counter(user_string))

# Problem 6

# def occurence_counter(string_to_search, string_to_find):
#     count = string_to_search.count(string_to_find)
#     return count

# Problem 7

def lower_strip(string):
    string = string.lower().strip()
    return string

test1 = "SUPER!"
test2 = "        NANNANANANA BATMAN        "

print(lower_strip(test1))
print(lower_strip(test2))