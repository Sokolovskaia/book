group1 = [1, 8, 14, 15]
group2 = {8, 15, 4, 6, 7}

intersection = set(group1) & group2
print(intersection)

data_list = [8, 4, 8, 10, 8, 7]
contains_duplicates = len(set(data_list)) != len(data_list)
print(contains_duplicates)



uniq = set(elements)
for u in uniq:
    freq[u] = elements.count(u)
return freq