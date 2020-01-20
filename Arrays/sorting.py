"""Given an array of sorted integers which represent box sizes and an
integer representing an item size
    You have to find best fit box for the item (-1 in case of no box found)
  For example:
    Given 10,20,30,40,50,60,70 and 45
     
      You have to print 50
    Given 10,20,30,40,50,60,70 and 75
      You have to print -1
      Given 10,20,30,40,50,60,70 and 50
    You have to print 50"""


boxes = input ('Enter the box sizes in comma seperated format: ').split(",")
item = input('enter the item to check for fit: ')
n = len(boxes)
if item <= boxes[n-1]:
    for i in range (0, n):
        if boxes[i] >= item:
            print (boxes[i])
            break
else:
    print('-1')
