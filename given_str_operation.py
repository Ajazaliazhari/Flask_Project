def count_extra_characters(input_str):
    extra_count = 0

    for char in input_str:
        # Check if the character is outside the valid range (a-n, A-N)
        if not ('a' <= char <= 'n' or 'A' <= char <= 'N'):
            extra_count += 1

    return extra_count

# Examples
example1 = count_extra_characters("aaabdbnhaikjjm")
print(example1)  # Output: 0

example2 = count_extra_characters("abaxbdbbyyhwawiwjjjwem")
print(example2)  # Output: 8
