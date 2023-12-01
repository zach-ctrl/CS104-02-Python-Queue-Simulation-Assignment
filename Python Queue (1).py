# Python program to  
# demonstrate queue implementation 
# using list 
  
# Initializing a queue 
queue = [] 
  
# Adding elements to the queue 
queue.append('a') 
queue.append('b') 
queue.append('c') 
  
print ("Queues are First-In First-Out (FIFO) data structures") 
print("\nInitial queue. Used queue.append(item) to enter elements into the queue") 
print(queue) 
  
# Removing elements from the queue 
print("\nElements dequeued from queue. Used queue.pop(0) to pop element in front") 
print(queue.pop(0)) 
print(queue.pop(0))
print("\nElement 'd' enqueued (appended)")
queue.append('d')
print (queue)
print("\nElements dequeued from queue") 
print(queue.pop(0)) 
print(queue.pop(0))
  
print("\nQueue after removing elements") 
print(queue) 
  
# Uncommenting print(queue.pop(0)) 
# will raise and IndexError 
# as the queue is now empty 
