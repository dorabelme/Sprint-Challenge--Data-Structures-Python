import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Time: O(n log n), space: O(n), runtime: 0.1112

duplicates = []
bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# Time: O(n^2), space: O(n)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# Worst case time: O(n^2)
# Average case time: O(min(n, m))
# Runtime: 0.0016

start_time = time.time()

s1 = set(names_1)
s2 = set(names_2)
duplicates = s1 & s2

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# Worst case time: O(n)
# Average case time: O(n)
# Runtime: 0.00099
# Under one hundredth of a second

start_time = time.time()

s1 = set(names_1)
duplicates = [x for x in names_2 if x in s1]

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
