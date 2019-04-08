
arr = [45,24,35,31,40,38];

def maxProfit(ar):
    array = [];
    index = 0;
    last = len(ar)-1;
    
    for i in range(len(ar)):
       array.append([i+1,ar[i]]);
    print(array);
    array.sort(key=lambda x:x[1])
    print(array);

    while True:
        if array[last][1] - array[index][1] <= 0:
            return -1
        
        if array[index][0] < array[last][0] and array[index][1] < array[last][1]:
            return("if you buy day " + str(array[index][0]) +" and sell day " + str(array[last][0]) + " you get $" +str(array[last][1] - array[index][1]));
        else:
            index = index + 1;
            if index == last:
                index = 0;
                last = last - 1;

        #print(str(index) + " " + str(last));
print(maxProfit(arr));

#print(str(array[index][1]) + " is smaller " + str(array[last][1]));