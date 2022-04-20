class Entry(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def showEntry(self):
        print(f'NAME:{self.name} VALUE: {self.value}')

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    
    def print_queue(self):
        for entry in self.queue:
            entry.showEntry()
    
    def isEmpty(self):
        return (len(self.queue) == 0)

    def insert(self, data):
        self.queue.append(data)

    def pop_min(self):
        # removes and returns Entry with least VALUE
        if(self.isEmpty()):
            return
        min_val = float('inf')
        for i in range(len(self.queue)):
            if self.queue[i].value < min_val:
                min_idx = i
                min_val = self.queue[min_idx].value
        minimum = self.queue[min_idx]
        del self.queue[min_idx]
        return minimum