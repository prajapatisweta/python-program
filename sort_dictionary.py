# date 17/09/21
# Write a Python script to list dictionary elements in ascending and descending order.
dict_1= {1:10, 3:30, 2:20, 4:40 , 6:60, 5:50}
print("Ascending order of keys (Default) : ", dict_1)

asc_val= sorted(dict_1.items(), key= lambda x:x[1])
print("Ascending order of Values : ", asc_val)

desc_val= sorted(dict_1.items(), key= lambda x:x[1], reverse= True)
print("Descending order of Values : ", desc_val)

desc_val= sorted(dict_1.items(), key= lambda x:x[0], reverse= True)
print("Descending order of Values : ", desc_val)