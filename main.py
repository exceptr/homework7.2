import os


a = os.path.join(os.getcwd(), 'txt')
dict = {}
for i in os.listdir(a):
    with open(os.path.join(os.getcwd(), 'txt', i), encoding='utf-8') as read_list:
        dict[i] = read_list.readlines()


def get_key(value):
    for k, v in dict.items():
        if v == value:
            return k


with open('finished_file.txt', 'a', encoding='utf-8') as new_file:
    sorted_list = sorted(dict.values(), key=lambda x: len(x))
    for line in sorted_list:
        new_file.write(get_key(line))
        new_file.write('\n')
        new_file.write(str(len(line)))
        new_file.write('\n')
        new_file.write(str(''.join(line)))
        new_file.write('\n')