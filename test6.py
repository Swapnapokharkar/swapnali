def Selection():
	import sys
	A = [64, 25, 12, 22, 11]


	for i in range(len(A)):
		min_idx = i
		for j in range(i+1, len(A)):
		    if A[min_idx] > A[j]:
		        min_idx = j
		A[i], A[min_idx] = A[min_idx], A[i]
	print ("Sorted array")
	for i in range(len(A)):
		print("%d" %A[i],end=" ")

def Insertion():
	def insertionSort(arr):
		for i in range(1, len(arr)):
		    key = arr[i]
		    j = i-1
		    while j >=0 and key < arr[j] :
		            arr[j+1] = arr[j]
		            j -= 1
		    arr[j+1] = key
	arr = [12, 11, 13, 5, 6]
	insertionSort(arr)
	print ("Sorted array is:")
	for i in range(len(arr)):
		print ("%d" %arr[i])

def Merge():
	def merge(arr, l, m, r):
		n1 = m - l + 1
		n2 = r - m
		L = [0] * (n1)
		R = [0] * (n2)
		for i in range(0, n1):
		    L[i] = arr[l + i]
		for j in range(0, n2):
		    R[j] = arr[m + 1 + j]
		i = 0
		j = 0
		k = l
		while i < n1 and j < n2:
		    if L[i] <= R[j]:
		        arr[k] = L[i]
		        i += 1
		    else:
		        arr[k] = R[j]
		        j += 1
		    k += 1
		while i < n1:
		    arr[k] = L[i]
		    i += 1
		    k += 1
		while j < n2:
		    arr[k] = R[j]
		    j += 1
		    k += 1
	def mergeSort(arr, l, r):
		if l < r:
		    m = l+(r-l)//2
		    mergeSort(arr, l, m)
		    mergeSort(arr, m+1, r)
		    merge(arr, l, m, r)
	arr = [12, 11, 13, 5, 6, 7]
	n = len(arr)
	print("Given array is")
	for i in range(n):
		print("%d" % arr[i],end=" ")
	mergeSort(arr, 0, n-1)
	print("\n\nSorted array is")
	for i in range(n):
		print("%d" % arr[i],end=" ")

def Quick():
	def partition(arr, low, high):
		i = (low-1)
		pivot = arr[high]

		for j in range(low, high):
		    if arr[j] <= pivot:
		        i = i+1
		        arr[i], arr[j] = arr[j], arr[i]

		arr[i+1], arr[high] = arr[high], arr[i+1]
		return (i+1)
	def quickSort(arr, low, high):
		if len(arr) == 1:
		    return arr
		if low < high:
		    pi = partition(arr, low, high)
		    quickSort(arr, low, pi-1)
		    quickSort(arr, pi+1, high)
	arr = [10, 7, 8, 9, 1, 5]
	n = len(arr)
	quickSort(arr, 0, n-1)
	print("Sorted array is:")
	for i in range(n):
		print("%d" % arr[i])

def ex():
	exit(0)

def default():
    print("Wrong Choice Try again!")
a=0
while a==0:
	ch=int(input("\nEnter Choice: "))
	if ch==1:
	    Selection()
	elif ch==2:
		Insertion()
	elif ch==3:
		Merge()
	elif ch==4:
		Quick()
	elif ch==5:
		ex()
	else:
		default()