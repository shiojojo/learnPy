class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__stk = []

    def put(self, elem):
        self.__stk.insert(0,elem)


    def get(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        # I don' know how to do it other than "self._Queue__stk"
        if len(self._Queue__stk) == 0:
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
