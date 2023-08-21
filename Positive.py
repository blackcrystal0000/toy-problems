def two_are_positive(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
        
    if b > 0:
        positive_count += 1
        
    if c > 0:
        positive_count += 1
        
    return positive_count == 2

print(two_are_positive(-1, 2, -4))  # Output: True
print(two_are_positive(-1, 2, 3))  # Output: False