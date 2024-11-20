a = [21,33,44,55,66]

a.insert(1,284) # O(n)

# The difference is that with append, you just add a new entry at the end of the list. With insert(position, new_entry)
# you can create a new entry exactly in the position you want.
a.remove(33) # O(n)

# In python list is dynamic array except when used in Numpy it can has static array.


##  -------------------------

# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses = []
expenses.append(2200)
expenses.append(2350)
expenses.append(2600)
expenses.append(2130)
expenses.append(2190)

extra_spent = expenses[1] - expenses[0]
print("extra spent in february compared to january", extra_spent)
total_expense = expenses[0] + expenses[1] + expenses[2]
print("total expense in first three quarter", total_expense)

excaxtly_2k_spent = False
for i in expenses:
    if i == 2000:
        print(f"in {expenses[i]} excatly 2000 was spent")
        excaxtly_2k_spent = True

if excaxtly_2k_spent == False:
    print("In no month exactly 2k was spent")

expenses.append(1980)
print("New list of expenses end of June", expenses)

expenses[3] = expenses[3] - 200
print("Updated list of expenses after refund", expenses)

print("********************************************")

# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']

print("Lenght of list heros", len(heros))
heros.append("Black Panther")
print("New heros list", heros)

heros.remove("Black Panther")
heros.insert(3,"Black Panther")
print("New heros list", heros)
heros[1:3]=['doctor strange']
print("Updated list", heros)
heros.sort()
print(heros)

print("********************************************")

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_number = int(input("Enter max Number: "))
max_number_list = []

for i in range(1,max_number):
    if i %2 != 0:
        max_number_list.append(i)

print("max odd number list", max_number_list)