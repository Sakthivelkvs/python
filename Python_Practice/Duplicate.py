arr=['Car','Bike', 'Car', 'Bus', 'Truck', 'Train', 'Plane','Bike']
length=len(arr)
print("Length of the array is:", length)

for i in range(0, length):
    for j in range(i+1, length):
        if arr[i]==arr[j]:
            print('Duplicate element found:', arr[i])

