
import time

class PriorityQueue(object):
    
    def __init__(self):
        self.queue_a = []
        self.queue_b = []
        
    def enqueue(self, this_string, priority_a, priority_b):
        current_time = time.clock()
        self.queue_a.append([this_string, priority_a, priority_b, current_time])
        self.queue_b.append([this_string, priority_a, priority_b, current_time])
        self.queue_a.sort(key=lambda item: item[1])
        self.queue_b.sort(key=lambda item: item[2])
    
    def dequeue_a(self):
        try:
            dequeue_this = sorted([x for x in self.queue_a if x[1] == self.queue_a[-1][1]], key=lambda item: item[3], reverse=True).pop()
            self.queue_a.remove(dequeue_this)
            self.queue_b.remove(dequeue_this)
            return dequeue_this
        except:
            raise Exception("Unable to dequeue item.")
            
    def dequeue_b(self):
        try:
            dequeue_this = sorted([x for x in self.queue_b if x[2] == self.queue_b[-1][2]], key=lambda item: item[3], reverse=True).pop()
            self.queue_b.remove(dequeue_this)
            self.queue_a.remove(dequeue_this)
            return dequeue_this
        except:
            raise Exception("Unable to dequeue item.")
            
    def count(self):
        return len(self.queue_a)
    
    def clear(self):
        self.queue = []
        return True
        
    def dequeue_last(self):
        try:
            dequeue_this = sorted(self.queue_a, key=lambda item: item[3], reverse=True).pop()
            self.queue_a.remove(dequeue_this)
            self.queue_b.remove(dequeue_this)
            return dequeue_this
        except:
            raise Exception("Unable to dequeue the last item in queue.")

# Example usage:
item_list = [["Hyperion Hypodermic Needle", 1.99, 3], ["SuperSaver Syringe", .89, 7], ["InjectXpress Platinum Plated Needle", 2.49, 2]]          
#item_list = [["Hyperion Hypodermic Needle", 1.99, 3] for i in range(1000)]
test_queue = PriorityQueue()

for i in range(len(item_list)):
    test_queue.enqueue(item_list[i][0], item_list[i][1], item_list[i][2])

print (test_queue.count())
print (test_queue.dequeue_b())
print (test_queue.dequeue_a())
print (test_queue.count())
print (test_queue.dequeue_last())
print (test_queue.count())