# date 17/09/21
# Write a Python script to concatenate following dictionaries to create a new one.
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}

dict_4 = {}
dict_4.update(dict_1)
dict_4.update(dict_2)
dict_4.update(dict_3)
print(f"Concatenated Dictionary: {dict_4}")