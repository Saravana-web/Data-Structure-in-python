class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Car {data} entered.")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Car {data} entered.")

    def dequeue(self):
        if self.is_empty():
            print("No cars .")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"{temp.data} left .")
        return temp.data

    def display(self):
        if self.is_empty():
            print("Parking is empty.")
            return
        current = self.front
        print("Cars currently in parking:")
        while current:
            print(current.data,end="-->")
            current = current.next
        print(None)

if __name__ == "__main__":
    q=Queue()
    q.enqueue("car1")
    q.enqueue("car2")
    q.enqueue("car3")
    q.display()
    q.dequeue()
    q.display()
    
