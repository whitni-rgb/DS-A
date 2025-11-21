# 0 - 99
sortedList = list(range(0, 100))
other = [1,2,3,4,5]

'''
NOTES:

Binary search Big-O = logN
Search algorithm to find target of SORTED list.
Works by determining if current guess is higher or lower than the target and eliminates that side of the branch.

Sidenote: 

Should use
mid = (low + (high - low)) // 2
instead of 
mid = ((high + low)- 1) // 2

- Will prevent integer overflow for languages that specifically have a memory limit.
- Faster
 

Fixed index, need to figure out the comparison here use while low <= high 
'''

"Returns the index of the target" 
def binarySearch(numbers, target):
    low = 0
    high = len(numbers) - 1
    mid = (low + (high - low)) // 2
    print(low)
    print(high)
    print(mid)

    while low <= high:
        if target == numbers[mid]:
            print("found")

binarySearch(other, 2)