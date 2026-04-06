print(any([x > 0 for x in [1, 2, 3]]))  # Output: True
print(any([x > 3 for x in [1, 2, 3]]))  # Output: False
print(all([x > 0 for x in [1, 2, 3]]))  # Output: True
print(all([x > 1 for x in [1, 2, 3]]))  # Output: False

# | Function | Condition             | Result |
# | -------- | --------------------- | ------ |
# | `any()`  | At least 1 True       | True   |
# | `all()`  | All True hone chahiye | True   |

# Example with strings
list1 = [True, False, True]
print(any(list1))  # Output: True
print(all(list1))  # Output: False