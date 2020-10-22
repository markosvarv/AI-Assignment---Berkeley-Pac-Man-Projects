import heapq
import itertools


class PriorityQueue:

    def __init__(self):
        self.heap = []  # our queue
        self.count = 0  # count items in queue
        self.entry_finder = {}  # mapping of items to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        # print('Priority Queue created!')

    def push(pq, item, priority):
        """Add a new item in priority queue"""
        if item in pq.entry_finder:
            #print("Item " + item + " already exists in queue. Please update to change priority")
            return False
        pq.count += 1
        entry = [priority, item]
        pq.entry_finder[item] = entry
        heapq.heappush(pq.heap, entry)

    def remove_item(pq, item):
        """Mark an existing task as REMOVED"""
        entry = pq.entry_finder.pop(item)
        entry[-1] = pq.REMOVED

    def pop(pq):
        """Remove and return the lowest priority task. Raise KeyError if empty"""
        while pq.heap:
            priority, item = heapq.heappop(pq.heap)
            if item is not pq.REMOVED:
                del pq.entry_finder[item]
                pq.count -= 1
                return item
        raise KeyError('pop from an empty priority queue')

    def update(pq, item, priority):
        """Update the priority of an existing task"""
        if item in pq.entry_finder:
            if pq.entry_finder[item][0] <= priority:
                return  # if priority is greater or equal, do nothing
            else:
                pq.remove_item(item)  # if priority is smaller, remove this item
                pq.count -= 1
        pq.push(item, priority)  # push this item anyway

    def isEmpty(pq):
        """Return true if pq is empty, else false"""
        return pq.count == 0

    @staticmethod
    def PQSort(given_list):
        """Gets a list and returns this list, sorted"""
        pq = PriorityQueue()
        sorted_list = []
        for number in given_list:
            try:  # ensure that all elements in given list are ints
                number = int(number)
            except ValueError:
                print  ("Try again using only integers in given list")
                return None
            pq.push(number, number)  # item and priority are the same number
        while not pq.isEmpty():
            sorted_list.append(pq.pop())
        return sorted_list

