# Bubble sort: repeatedly compares neighboring numbers and swaps them if needed.
#
# Desk test:
# len(mylist) is 8 because there are eight values, counted as items 1 through 8.
# Python indexes those items from 0 through 7. The length is a count, not an index.
#
# Each comparison looks at indexes j and j + 1. If the left value is larger,
# they swap. This moves the largest value still unsorted to the right on each pass.
# The inner range gets shorter because the rightmost values are already sorted.
#
# Pass 1, comparing positions (counting from 1):
# 1-2: 64 > 34, swap -> [34, 64, 25, 12, 22, 11, 90, 5]
# 2-3: 64 > 25, swap -> [34, 25, 64, 12, 22, 11, 90, 5]
# 3-4: 64 > 12, swap -> [34, 25, 12, 64, 22, 11, 90, 5]
# 4-5: 64 > 22, swap -> [34, 25, 12, 22, 64, 11, 90, 5]
# 5-6: 64 > 11, swap -> [34, 25, 12, 22, 11, 64, 90, 5]
# 6-7: 64 < 90, keep -> [34, 25, 12, 22, 11, 64, 90, 5]
# 7-8: 90 > 5, swap -> [34, 25, 12, 22, 11, 64, 5, 90]
# Passes 2-7, showing the list after each pass:
# Pass 2: [34, 25, 12, 22, 11, 64, 5, 90] -> [25, 12, 22, 11, 34, 5, 64, 90]
# Pass 3: [25, 12, 22, 11, 34, 5, 64, 90] -> [12, 22, 11, 25, 5, 34, 64, 90]
# Pass 4: [12, 22, 11, 25, 5, 34, 64, 90] -> [12, 11, 22, 5, 25, 34, 64, 90]
# Pass 5: [12, 11, 22, 5, 25, 34, 64, 90] -> [11, 12, 5, 22, 25, 34, 64, 90]
# Pass 6: [11, 12, 5, 22, 25, 34, 64, 90] -> [11, 5, 12, 22, 25, 34, 64, 90]
# Pass 7: [11, 5, 12, 22, 25, 34, 64, 90] -> [5, 11, 12, 22, 25, 34, 64, 90]
mylist = [64, 34, 25, 12, 22, 11, 90, 5]  # The list of numbers to sort.

n = len(mylist)  # n is 8: the number of items, not the last index.
for i in range(n - 1):  # Seven passes: i is 0..6, so the pass number is i + 1.
    for j in range(n - i - 1):  # Check the unsorted neighboring pairs.
        if mylist[j] > mylist[j + 1]:  # If this pair is in descending order...
            # Swap the pair so the smaller number comes first.
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

print(mylist)  # Display the sorted list.