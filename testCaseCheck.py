def camelCase(input_str, delimiter):
    words = input_str.split(delimiter)
    camel_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    result = ''.join(camel_words)

    return result

# Examples
example1 = camelCase("the-test-case", "-")
print(example1)  # Output: "theTestCase"

example2 = camelCase("The_First_Word_Capital", "_")
print(example2)  # Output: "TheFirstWordCapital"
