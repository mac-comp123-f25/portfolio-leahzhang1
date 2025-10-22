def remove_all (rep,value):
    while value in rep:
        rep.remove(value)
    return rep

t_list = ['b', 'a', 'n', 'a', 'n', 'a']
remove_all(t_list, 'a')
print(t_list)