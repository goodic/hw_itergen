
class FlatIterator:

    def __init__(self, mylist):
        self.mylist = mylist

    def __iter__(self):
        self.cursor_x = 0
        self.cursor_y = 0
        self.end_x = len(self.mylist)
        self.end_y = len(self.mylist[self.cursor_x])
        return self

    def __next__(self):
        self.cursor_y += 1
        if self.cursor_y > self.end_y:
            self.cursor_x += 1
            if self.cursor_x == self.end_x:
                raise StopIteration
            self.cursor_y = 1
            self.end_y = len(self.mylist[self.cursor_x])
        return self.mylist[self.cursor_x][self.cursor_y - 1]


def flat_generator(mylist):
    for item in mylist:
        if isinstance(item, list):
            for nested_item in flat_generator(item):
                yield nested_item
        else:
            yield item



if __name__ == '__main__':
    nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
    print('FlatIterator 1.1')
    for item in FlatIterator(nested_list):
        print(item)

    print('FlatIterator 1.2')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('FlatGenerator 4(2)')
    for item in flat_generator(nested_list):
        print(item)