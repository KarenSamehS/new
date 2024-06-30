import random
import time
def SelectionSort(A, n):
   start_time = time.time() 
   for i in range(n - 1):
     iMin = i         
     for j in range(i + 1, n):
            if A[j] < A[iMin]:
                iMin = j
     if i != iMin:
            A[i], A[iMin] = A[iMin], A[i]
   end_time = time.time()  # Record the end time
   return (end_time - start_time)*1000 

def InsertionSort(A, n):
    start_time = time.time() 
    for i in range(n):
     key=A[i]
     j=i
     while (j > 0 and A[j - 1] > key) :
         A[j]=A[j-1]
         j=j-1
     A[j]=key   
    end_time = time.time()  # Record the end time
    return (end_time - start_time)*1000   

    
def partition(arr, start, end):
    randomNum = random.randint(start,end )
    (arr[start], arr[randomNum]) = (arr[randomNum], arr[start]) 
    pivotAddress = start
    i = start + 1
    for j in range (start +1, end+1 ):
        if arr[j] <= arr[pivotAddress]:
            (arr[i],arr[j]) = (arr[j],arr[i]) 
            i=i+1
    (arr[pivotAddress],arr[i-1]) =  (arr[i-1],arr[pivotAddress])
    pivotAddress = i-1
    return pivotAddress

def KLargestElement(arr, start, end, k):
    if k > 0 and k < len(arr) :
        pivotAddress = partition(arr, start, end)
        if ( len(arr) -  pivotAddress) == k:
            return arr[pivotAddress]
        if ( len(arr) -  pivotAddress) > k :
            return KLargestElement(arr,pivotAddress + 1,end,k)
        else: 
            return KLargestElement(arr,start,pivotAddress - 1,k)
    else: 
        print("Invalid number")
        return 

def quickSort(arr,start,end):
    if start < end:
        start_time = time.time() 
        pivotIndex = partition(arr,start,end)
        quickSort(arr,start,pivotIndex -1 )
        quickSort(arr,pivotIndex +1 ,end)
        end_time = time.time()  
        return (end_time - start_time) * 1000
def merge(arr, low, mid, high):
    n_left = mid - low + 1
    n_right = high - mid
    left_array = [0] * n_left
    right_array = [0] * n_right

    for i in range(n_left):
        left_array[i] = arr[low + i]

    for i in range(n_right):
        right_array[i] = arr[mid + 1 + i]

    i = 0
    j = 0
    k = low

    while i < n_left and j < n_right:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
            k += 1
        else:
            arr[k] = right_array[j]
            j += 1
            k += 1
            
    while i < n_left:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < n_right:
        arr[k] = right_array[j]
        j += 1
        k += 1

def mergesort (arr, low, high):
    start_time1 = time.time()
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(arr, low, mid, high)
    end_time1 = time.time()  # Record the end time
    return (end_time1 - start_time1)*1000 


def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def maxheapify (arr, i, heapsize):
    l = left(i)
    r = right(i)

    if l < heapsize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[largest] , arr[i] = arr[i] , arr[largest]
        maxheapify(arr, largest, heapsize)

def buildmaxheap (arr):
    heapsize = len(arr)
    for i in range((len(arr) -1)// 2, -1, -1) : #n/2 downto 0
        maxheapify(arr,i, heapsize)
    
def heapsort(arr):
    start_time2 = time.time()
    buildmaxheap(arr)
    heapsize = len(arr)

    for i in range(len(arr) -1, 0, -1): # n downto 1
        arr[i] , arr[0] = arr[0] , arr[i]
        heapsize -= 1
        maxheapify(arr,0, heapsize)
    
    end_time2 = time.time()  # Record the end time
    return (end_time2 - start_time2)*1000  

def hybridInsertionSort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def merge_sort(arr, low, high, threshold):
    if low < high:
        if high - low <= threshold:
            hybridInsertionSort(arr, low, high)
        else:
            mid = (low + high) // 2
            merge_sort(arr, low, mid, threshold)
            merge_sort(arr, mid+1, high, threshold)
            merge(arr, low, mid, high)
            

def hybrid_sort(arr, threshold):
    start_time = time.time()
    merge_sort(arr, 0, len(arr) - 1, threshold)
    end_time = time.time()
    return (end_time - start_time) * 1000


def generate_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

sizes = [1000, 25000, 50000, 100000] 
for size in sizes:
    arr = generate_array(size)
    k = int(input("Enter order of largest element = "))
    KLargest = KLargestElement(arr, 0, size-1,k)
    print(k, " largest element is ", KLargest )
    ArraySelection = arr.copy()
    ArrayInsertion = arr.copy()
    ArrayQuick = arr.copy()
    ArrayMerge = arr.copy()
    ArrayHeap = arr.copy()
    ArrayHybrid = arr.copy()
    Threshold = 6
    time_taken1=SelectionSort(ArraySelection,size)
    time_taken2 = InsertionSort(ArrayInsertion,size) 
    time_taken3 =  quickSort(ArrayQuick , 0,size - 1)
    time_taken4 = mergesort(ArrayMerge,0, size - 1)
    time_taken5 = heapsort(ArrayHeap) 
    time_taken6 = hybrid_sort(ArrayHybrid, Threshold)  
    
    print("\n Array (size:", size, ") \n")
    print("Time taken by Selection Sort: {:.6f} milliseconds \n".format(time_taken1) )
    print("Time taken by Insertion Sort: {:.6f} milliseconds \n".format(time_taken2) )
    print("Time taken by Quick Sort: {:.6f} milliseconds \n".format(time_taken3) )
    print("Time taken by Merge Sort: {:.6f} milliseconds \n".format(time_taken4) )
    print("Time taken by Heap Sort: {:.6f} milliseconds \n".format(time_taken5) )
    print("Time taken by Hybrid Sort: {:.6f} milliseconds \n".format(time_taken6) )

    print("----------------------------------------------------------")





   