def dupes(seq):
    lst = []
    for i in seq:
        if i not in lst:
            lst.append(i)
        else:
            print(f"В последовательности есть дубликат: {i}")
    if len(seq) == len(lst):
        print('В последовательности нет дубликатов')
