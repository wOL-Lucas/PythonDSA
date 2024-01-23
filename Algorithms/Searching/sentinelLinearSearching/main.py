class Array:
    def __init__(self) -> None:
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        self.elements.pop()
    
    def search(self, elementToFind):
        n = len(self.elements) - 1
        originalLastItem = self.elements[n]

        i = 0
        while(i != (n + 1) and self.elements[i] != elementToFind):
            i += 1


        self.elements[n] = originalLastItem

        if((i < n) or (self.elements[n] == elementToFind)):
            return i
        else:
            return -1
        


if __name__ == "__main__":
    array = Array()
    array.push(0)
    array.push(1)
    array.push(2)
    array.push(3)
    array.push(5)

    print(array.search(5))