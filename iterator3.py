import time


class Fibunacci():
    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.counter = 0
        return self

    def __next__(self):
        
        
        if self.counter == 0:
            self.counter +=1
            return self.a
        elif self.counter == 1:
            self.counter +=1
            return self.b
        else:
            while (self.max > self.counter):
                self.aux = self.a + self.b
                self.a, self.b = self.b, self.aux #swapping
                self.counter += 1
                return self.aux
            else:
                raise StopIteration
        

def run():
    fibu = Fibunacci(10) #Instancing a Fibunacci object
    for element in fibu:
        print(element)
        time.sleep(0.5) #sleep time for 0.5 seconds


if __name__ == '__main__':
    run()