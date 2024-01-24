def sort(self):
    for i in range(len(self.elements)): 

        min_idx = i 
        for j in range(i+1, len(self.elements)): 
            if self.elements[min_idx] > self.elements[j]: 
                min_idx = j 
                
        
        self.elements[i], self.elements[min_idx] = self.elements[min_idx], self.elements[i]
    
    print ("Sorted array") 
    for i in range(len(self.elements)): 
        print("%d" %self.elements[i],end=", ")