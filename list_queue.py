# queue_example.py
# FIFO


#10
#20
#30

# Create an empty queue
queue = []

# ENQUEUE operations (insert at rear)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueues:", queue)

# PEEK (front element)
if queue:
    print("Front element:", queue[0])

# DEQUEUE operation (remove from front)
removed_item = queue.pop(0)
print("Removed item:", removed_item)

print("Queue after dequeue:", queue)

# Check if queue is empty
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")

# Remove all elements
while queue:
    print("Removing:", queue.pop(0))

print("Final queue:", queue)