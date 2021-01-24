class Queue:
    def __init__(self, *args):
        self.arr = list(args)

    def push(self, element):
        self.arr.append(element)
