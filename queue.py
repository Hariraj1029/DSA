from collections import deque
q = deque([1,2,3]) # initialize queue with some values

def enqueue(data): # insert at the end
    q.append(data)

def dequeue(): # delete at the beginning
    if len(q) == 0: # if the queue is empty
        print("Queue is empty")
    else: # if the queue is not empty
        print("Value removed from queue: ", q.popleft()) # delete at the beginning
        print(q)

def display(): # print the queue
    print(q)

display()
enqueue(10)
display()