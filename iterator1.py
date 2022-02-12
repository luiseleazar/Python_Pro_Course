class EvenNumbers:
    """Class that implements a iterator 
    of all even number or even number
    until a max value"""

    def __init__(self, max=None):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <=self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration