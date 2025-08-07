List = [1,2,3,4,5,6,7,8,9,10]
print("Original list: ", List)
a=List[0:5]
a.reverse()
print("Extracted first five elements: ", List[:5])
print("Reversed extracted elements: ", a)
