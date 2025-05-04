def digit_root(num):
    result = 0
    for digit in str(num):
        result += int(digit)

    if result > 9:
        return digit_root(result)
    else:
        return result
    

print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))