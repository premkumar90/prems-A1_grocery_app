apples_tuple = ("apples", 0.50,5)
bananas_tuple = ("bananas", 0.25, 10)
peaches_tuple = ("peaches",0.8,15)

grocery_list = [apples_tuple, bananas_tuple, peaches_tuple]
print(grocery_list)
print(grocery_list[1])
total_cost = grocery_list[1][1] * grocery_list[1][2]
print(f"Total cost of apples: ${total_cost}")

#EXERCISE 2: Working with Dictionaries

apple_dict = {"name":"apple","price":0.50,"quantity":5}
banana_dict = {"name":"banana","price":0.25,"quantity":10}
peach_dict = {"name":"peach","price":0.8,"quantity":15}

total_cost_apple = apple_dict["price"]* apple_dict["quantity"]
print(f"Total cost of apples: ${total_cost_apple}")

#EXERCISE 3: SLICING AND SORTING A LIST
num_list = [16,47,1,3,5,9,15,2]
print(num_list[1:])
print(num_list[:3])
print(num_list[-6:])
num_list.sort()
print(len(num_list))

#EXERCISE 4: SETS OPERATIONS
dairy_products = {"milk","butter","cream","yogurt","cheese"}
desserts = {"jello","chocolate","candy","cookie","muffins"}
dairy_products.add("ice cream")
desserts.add("ice cream")


dairy_products.discard("yogurt")
desserts.remove("candy")
# print(dairy_products)
# print(desserts)
print(dairy_products.intersection(desserts))

#EXERCISE 5:UPDATING THE CHANGELOG









