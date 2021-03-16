def snakecase_to_camelcase(underscore):
    s = underscore.split("_")
    camel_case = ""
    for i in range(1, len(s)):
        camel_case += (s[i][0].upper() + s[i][1:])
    camel_case = s[0] + camel_case
    return camel_case

cc3 = snakecase_to_camelcase("snake_case_to_camel_case")
print(cc3)