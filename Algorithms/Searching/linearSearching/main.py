class Array:
    def __init__(self) -> None:
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        self.elements.pop()
    
    def search(self, elementToFind):
        for index,element in enumerate(self.elements):
            if element == elementToFind:
                return index
        

if __name__ == "__main__":
    array = Array()
    array.push(0)
    array.push(1)
    array.push(2)
    array.push(4)

    print(array.search(3))
    print(array.search(4))