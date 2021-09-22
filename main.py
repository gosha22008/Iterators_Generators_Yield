import json

with open('countries.json', 'r', encoding='utf-8') as f:
    file = json.load(f)


class WikiPage:

    def __init__(self):
        self.start = -1
        self.end = len(file)
        self.url = 'https://en.wikipedia.org/wiki/'

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        res = file[self.start]['name']['common'] + '---' + str(self.url + file[self.start]['name']['common']).replace(' ', '_') + '\n'
        with open('result_file', 'a', encoding='utf-8') as f:
            f.write(res)
        return res


for i in WikiPage():
    pass








