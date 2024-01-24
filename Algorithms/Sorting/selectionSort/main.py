class Array:
    def __init__(self) -> None:
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        self.elements.pop()

    def sort(self):
        for i in range(len(self.elements)):
            min_index = i

            for j in range(i + 1, len(self.elements)):
                if self.elements[min_index] > self.elements[j]:
                    min_index = j

            self.elements[i], self.elements[min_index] = self.elements[min_index], self.elements[i]

    def to_string(self):
        return self.elements

if __name__ == "__main__":
    array = Array()
    array.elements = [11,32,33,34,1]
    array.sort()

    print(array.to_string())