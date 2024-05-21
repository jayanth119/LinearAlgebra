class Heapers:
    def heapify(self,arr, n, index):
            lt = 2*index + 1
            rt = 2*index + 2
            largest = index
            if lt < n and arr[lt] > arr[largest]:
                largest = lt
            if rt < n and arr[rt] > arr[largest]:
                largest = rt
            if largest != index:
                arr[index],arr[largest] = arr[largest],arr[index]
                self.heapify(arr,n,largest)
        
    def buildHeap(self,arr,n):
            for i in range((n-2)//2,-1,-1):
                self.heapify(arr,n,i)       
    def HeapSort(self, arr, n):
            self.buildHeap(arr,n)
            for i in range(n-1,0,-1):
                arr[i],arr[0] = arr[0],arr[i]
                self.heapify(arr,i,0)
            print(arr) 
c = Heapers()
s = [12,3,42,1,42,25,1,51,5,1]
c.HeapSort(s, len(s))
