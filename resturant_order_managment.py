
class Orders():
    def __init__(self):
        self.orders = []

    def enqueue(self,order_data):
        self.orders.append(order_data)

    def dequeue(self):
        try:
            return self.orders.pop(0)
        except IndexError:
            return "queue is empty!"    
    def is_empty(self):
        return len(self.orders) == 0
    
    def get_length(self):
        return len(self.orders)