class Queue:
    def __init__(self, *args):
        self.arr = list(args)

    def push(self, element):
        self.arr.append(element)

    def pop(self):
        self.arr.pop(-1)

    def get_list(self):
        return self.arr

    def __iter__(self):
        return iter(self.arr)

    def __add__(self, lst):
        self.arr.extend(lst)
