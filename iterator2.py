import time


class Fibunacci():
    #__init__ ignored
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
            self.aux = self.a + self.b
            #self.a = self.b
            #self.b = self.aux
            self.a, self.b = self.b, self.aux #swapping
            self.counter += 1
            return self.aux


def run():
    fibu = Fibunacci() #Instancing a Fibunacci object
    for element in fibu:
        print(element)
        time.sleep(0.5) #sleep time for 0.5 seconds


if __name__ == '__main__':
    run()
        