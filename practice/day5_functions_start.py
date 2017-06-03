def parse_lists(some_list):
    str_list_items = []
    num_list_items = []

    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass

    return str_list_items, num_list_items

items = ["mic", "phone", 323.12, 31212.31, "Justin", "bag", 123, "Cliff Bars"]
print(parse_lists(items))

def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total
print(my_sum(items))

def count_nums(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += 1
    return total

def my_avg(my_num_list):
    the_sum = my_sum(my_num_list)
    num_of_items = count_nums(my_num_list)
    return the_sum / num_of_items

print(my_avg(items))
