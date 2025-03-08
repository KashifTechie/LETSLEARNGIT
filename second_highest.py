li = [3,0,2,6,4,-5,-1,7,9,-8]

first = float('-inf')
second = float('-inf')
for i in li:
    if i>first:
        second = first 
        first = i
    elif i>second and i != first:
        second = i
print("second highest number is", second)