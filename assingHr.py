def find_specific_sum(T, N, C=None):
    def generate_numbers(current_number, remaining_sum, remaining_digits):
        if remaining_digits == 0:
            return [current_number] if remaining_sum == 0 else []

        numbers = []
        for digit in range(current_number % 10, min(remaining_sum + 1, 10)):
            next_number = current_number * 10 + digit
            numbers += generate_numbers(next_number, remaining_sum - digit, remaining_digits - 1)

        return numbers

    numbers_list = []
    current_number = 0

    if C is None:
        while True:
            numbers = generate_numbers(current_number, T, N)
            if not numbers:
                break

            numbers_list.append(numbers)
            current_number = numbers[-1] + 1

    else:
        for _ in range(C):
            numbers = generate_numbers(current_number, T, N)
            if not numbers:
                break

            numbers_list.append(numbers)
            current_number = numbers[-1] + 1

    if not numbers_list:
        return []

    low_value = numbers_list[0][0]
    mid_index = len(numbers_list) // 2
    mid_value = numbers_list[mid_index][0] if mid_index < len(numbers_list) else low_value

    return [numbers_list, low_value, mid_value]

# Example
result = find_specific_sum(10, 3, 3)
print(result)  # Output: [[118, 127, 136], 118, 127]


