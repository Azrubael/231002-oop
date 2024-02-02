class QueueError(IndexError): # Choose base class for the new exception.
    pass
    

class Queue:
    def __init__(self):
        self.__qeue_list = []
        self.__count = 0

    def put(self, elem):
        self.__qeue_list.insert(0, elem)
        self.__count += 1

    def get(self):
        res = None
        if len(self.__qeue_list) > 0:
            res = self.__qeue_list[-1]
            self.__count -= 1
            del self.__qeue_list[-1]
        return res
        
    def get_count(self):
        return self.__count


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")