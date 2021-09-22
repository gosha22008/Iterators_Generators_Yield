from hashlib import md5

path = 'result_file'


def my_generarot(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            my_file = md5(line.encode())
            yield my_file.hexdigest()
            print(my_file.hexdigest())


for i in my_generarot(path):
    pass
