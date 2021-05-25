list1 = [1, 13, 21, 45]
list2 = [2, 88, 64, 18]
list1+=list2
for i in list1:
    list2 = i * 2
    print(type(i),i)
