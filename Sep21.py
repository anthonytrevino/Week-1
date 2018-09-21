#Program to remove duplicates from an array.
names =('Alex', 'Mary', 'Steve', 'John', 'Steve', 'John', 'Steve')
mylist=set()
for name in names:
    mylist.add(name)
print(mylist)



#Program that finds the largest element in an array.

list1 = [123, 300, 321, 132]
print(max(list1))


#Program that finds the smallest element in the array.

list2 = [1, 100, 3, 200, 321]
print(min(list2))


#Program that displays a pyramid of *.

rows = int(input("Enter how many rows you want: "))

for row in range(rows):

    stars = (row*2) +1
    spaces = rows - row -1
    print((' ')*spaces + ("*") * stars)
