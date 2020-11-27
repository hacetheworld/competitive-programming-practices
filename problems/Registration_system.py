def Solution(name, names_dict):
    # Solution
    if name in names_dict:
        names_dict[name] += 1
        idx = names_dict.get(name)
        return name+str(idx)
    else:
        names_dict[name] = 0
        return 'OK'


names_dict = {}
for t in range(int(input())):
    name = input()
    print(Solution(name, names_dict))
