class Queue:
    def __init__(self,cap):
        self.cap=cap
        self.queue=[None]*cap
        self.front=0
        self.rear=-1
        self.size=0

    def emp(self):
        return self.size==0
    def full(self):
        return self.size==self.cap
    def enqueue(self,car):
        if self.full():
            print("Queue is full")
            return
        self.rear=self.rear+1
        self.queue[self.rear]=car
        self.size+=1
        print(f"car'{car}' added to queue")
    def dequeue(self):
        if self.emp():
            print("Queue is empty nothing to remove")
            return None
        car=self.queue[self.front]
        self.queue[self.front]=None
        self.front=self.front+1
        self.size-=1
        print(f"Car'{car}'removed")

    def disp(self):
             if self.emp():
                 print("Queue is empty nothing to display")
                 return None
             for i in range(self.size):
                print(f"-{self.queue[self.front+i]}")

if __name__=="__main__":
    Q=Queue(cap=5)
    Q.enqueue("car1")
    Q.enqueue("car2")
    Q.enqueue("car3")
    Q.disp()
    Q.dequeue()
    Q.disp()
    
