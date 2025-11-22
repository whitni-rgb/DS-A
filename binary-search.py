# 0 - 99
sortedList = list(range(0, 100))
other = [1,2,3,4,5]

'''
NOTES:

Binary search Big-O = logN
Search algorithm to find target of SORTED list.
Works by determining if current guess is higher or lower than the target and eliminates that side of the branch.

Will find the index of the target whether the target is in the array itself or not,
 to see where the index would be you can return low

Sidenote: 

Should use
mid = low + (high - low) // 2
instead of 
mid = (high + low) // 2

- Will prevent integer overflow for languages that specifically have a memory limit.
- Faster
'''

"Returns the index of the target" 
def binarySearch(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        guess = numbers[mid]
        if target == numbers[mid]:
            print(mid)
            break
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    print(low)

binarySearch(sortedList, 17)