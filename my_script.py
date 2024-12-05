#list
my_list = [1,2,"apple",4.5,"tomato",75]
# get an item from the list
get_item = my_list[2]
print(get_item)
#Slicing: Taking the first 3 items from the list
first_three = my_list[0:3]
print(first_three)

my_list_2 = [0,1,2,3,4,5]
print(my_list_2[1:4])
print(my_list_2[:4])
print(my_list_2[2:])
print(my_list_2[0:4:2])
print(my_list_2[-3:])
print(my_list_2[::-1])

my_shopping_list = ["milk","bread","eggs"]
my_shopping_list.append("banana")
my_shopping_list.remove("milk")
my_shopping_list.sort(reverse = True)

my_shopping_list.extend(["spinach","kale"])

my_shopping_list.insert(1,"oil")
print(my_shopping_list)
a_tuple = ("these","are","elements")
print(a_tuple[0])
#.pop()
pop_list = my_shopping_list.pop()
print(pop_list)
# .index()
index_list = my_shopping_list.index("eggs")
print(index_list)
# .count()
count_list = my_shopping_list.count("eggs")
print(count_list)
# .reverse()
reverse_list = my_shopping_list.reverse()
print(reverse_list)
# .clear()
clear_list = my_shopping_list.clear()
print(clear_list)
#Practice doc
my_list_3 = [1,'apple',3.5]
print(my_list_3[0]) # indexing
print(my_list_3[1:3]) #slicing
my_list_3.append('banana')
print(my_list_3) #append
my_list_3.remove('apple')
print(my_list_3) #remove
my_list_4 = [5,9,3,11]
my_list_4.sort()
print(my_list_4) #sort
list_a = [1,'apple',3.5]
list_b = ['banana','tomato']
list_a.extend(list_b)
print(list_a) #extend
my_list.insert(1,'banana')
print(my_list_3) # insert

#TUPLES
my_tuple = (10,20,'orange')
print(my_tuple[0])#indexing
print(my_tuple[0:2])#slicing
print(len(my_tuple))#length
my_tuple_concat = my_tuple + (30,40) #concatenation
print(my_tuple_concat)

#LISTS:PRACTICE EXERCISES
movies = ["Inception","Avatar","Matrix","Toy Story","The Godfather"]
movies.append("The Shawshank Redemption") #Append
print(movies)
movies.remove("Avatar") #Remove

numbers = [10,20,30,40,50]
print(numbers[3:])

colors = ['red','blue','green']
print(colors)
colors.insert(1,'yellow')
colors.append('purple')
print(colors)

#Tuples
dimensions = (10,5,15)
print(dimensions[1])

numbers_tuple = (0,1,2,3,4,5,6,7,8)
print(numbers_tuple[2:6])

#CONCATENATING TUPLES
fruits = ('apple','banana')
vegetables = ('carrot','lettuce')
groceries = fruits + vegetables
print(groceries)

dict_a = {"name":"milk","cost":6.5,"store":"save-on","amount":2}
print(dict_a["name"])
dict_a["cost"] = 5.75
print(dict_a)
dict_a["buy"] = True
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())
dict_a.pop("amount")
print(dict_a)

#DAY3: DICTIONARIES PRACTISE
my_dict = {'name':'John','age':25}
print(my_dict)
print(my_dict['name'])
my_dict['city'] = 'New York'
print(my_dict) #Adds a key-value pair
my_dict['age'] = 26 #Updates the value of age
print(my_dict)
my_dict.pop('age')
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#PRACTICE EXERCISES
#1
book = {'title':'1984','author':'George Orwell','year':1949}
print(book['author'])
#2
profile = {}
profile['name'] = 'Alice'
profile['age'] = 30
profile['city'] = 'Paris'
print(profile)
profile['city'] = 'London'
print(profile)
#3
student = {'name':'Emma','grade':'A','subject':'Math'}
student.pop('subject')
print(student)
dict_keys = student.keys()
print(dict_keys)    
dict_values = student.values()
print(dict_values)

my_set = {"apple","banana","chocolate","kombucha"}
my_set.add("noodles")
print(my_set)
my_set.add("apple")
print(my_set)
my_set.remove("banana")
print(my_set)
my_set.discard("apples")
set_1 = {"cheese","bread","deli meat"}
set_2 = {"milk","eggs","bread"}
union_set = set_1.union(set_2)
print(union_set)
inter_set = set_1.intersection(set_2)
print(inter_set)
diff_set = set_1.difference(set_2)
print(diff_set)
diff_set2 = set_2.difference(set_1)
print(diff_set2)

#DAY3:SETS
my_set = {'apple','banana','cherry'}
# my_set.add('orange')
# my_set.remove('banana')
my_set.discard('banana')
print(my_set)

set1 = {'apple','banana'}
set2 = {'banana','orange'}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

fruits = {'apple','banana','cherry'}
fruits.add('orange') #Adding orange to the set
print(fruits) #
fruits.remove('banana') #removing banana from the set
print(fruits) # printing out the desired result

set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a.union(set_b))
print(set_a.intersection(set_b))

#DIFFERENCE OPERATION
set_x = {'cat','dog','fish'}
set_y = {'dog','bird'}
print(set_x.difference(set_y)) #find the items that are in set_x but not in set_y.










