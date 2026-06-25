def minimum(values):
    minimum = values[0]
    for value in values:
        if(minimum>value):
            minimum = value
    return minimum
#this is for sorting
def sorting(values):
    sorted_values=[]
    while(len(values)!=0):
        least = minimum(values)
        sorted_values.append(least)
        values.remove(least)
    return sorted_values

def search(search_element, sorted_values):
    low = 0
    high = len(sorted_values) - 1
    while(low <= high):
        mid = low + (high-low)//2
        if(sorted_values[mid]==search_element):
            print(f"Element Found!! at the index value {mid}")
            return
        elif(sorted_values[mid]<search_element):
            low = mid+1
            continue
        elif(sorted_values[mid]>search_element):
            high = mid-1
            continue
    else:
        print("Element Not Found!!")


values = []
should_continue = 'T'
while(should_continue=='T'):
    values.append(input("Enter a Value: "))
    should_continue = (input("Do you want to continue (T/F)? : ")).upper()
print("The list entered is: ",values)

sorted_values= sorting(values)

print("The sorted list is ",sorted_values)

search_element = input("Enter the element to be searched ")
search(search_element, sorted_values)

