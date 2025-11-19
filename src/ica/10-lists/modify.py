def change_start (item):
    item[0]="X"
    return item

t_list = ['a', 'b', 'c', 'd', 'e', 'f']
change_start(t_list)
print(t_list)