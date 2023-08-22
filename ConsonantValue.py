def solve(s):
    vowels = "aeiou"
    current_string = ""
    consonant_values = []

    for char in s:
        if char not in vowels:
            current_string += char
        elif current_string:
            consonant_values.append(sum(ord(c) - 96 for c in current_string))
            current_string = ""

    if current_string:
        consonant_values.append(sum(ord(c) - 96 for c in current_string))

    return max(consonant_values) if consonant_values else 0
