def count_upper_case(message):
    count = 0
    for character in message:
        if character.isupper():
            count += 1
    return count
    
assert count_upper_case("AAA") == 3, "3 upper cases"
assert count_upper_case("aaa") == 0, "3 lower cases"
assert count_upper_case("$%&#") == 0, "characters"
assert count_upper_case("AaAaAa") == 3, "3 upper and 3 lower cases"

print("All the tests passed")    