
class History():
    def __init__(self):
        self.history = []

    def add_page(self,page_data):
        self.history.append(page_data)

    def remove_page(self):
        return self.history.pop()
    
    def count_pages(self):
        return len(self.history)
    
    def is_empty(self):
        return len(self.history) == 0