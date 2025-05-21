def format_program01(number, format_type):
    result = format(number, format_type)
    return result

formatted_value = format_program01(145, 'o')
# The 'o' format specifier converts the number to octal representation.
print("Formatted result:", formatted_value)
# 145 in decimal is 221 in octal.