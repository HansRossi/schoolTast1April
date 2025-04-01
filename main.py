school_list = ['Harvard', 'MIT', 'Yale', 'Stanford', 'Princeton']

def school_list_length():
    return len(school_list)

print(school_list_length())
for item in school_list:
    print(item)

new_item = input("Enter a new element")
school_list.append(new_item)
print(school_list)

school_list.remove("MIT")
print(school_list)

school_list.sort()
print(school_list)

school_list.reverse()
print(school_list)

