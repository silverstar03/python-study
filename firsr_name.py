def exclude_first_name(names_string):
    names = names_string.split(",");
    print(names)
    first_names = []
    for n in names:
        first_names.append(n[1:])


    return first_names
first_names = exclude_first_name("황광희,이효리,김지훈,이지은,고수")
print(first_names)
