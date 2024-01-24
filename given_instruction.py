def parse(input_str):
    result = []
    current_value = 0

    for char in input_str:
        if char == 'p':
            current_value += 1
        elif char == 'm':
            current_value -= 1
        elif char == 's':
            current_value **= 2
        elif char == 'o':
            result.append(current_value)

    return result

# Example
output = parse("ppppsmoso")
print(output)  # Output: [15, 225]


