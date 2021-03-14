def createHeap(arr, heap):
    for v in arr:
        heap.append(v)
        upHeapify(heap, len(heap)-1)


def upHeapify(heap, i):
    if i == 0:
        return
    pi = (i-1)//2
    if heap[pi] < heap[i]:
        tmp = heap[pi]
        heap[pi] = heap[i]
        heap[i] = tmp
        upHeapify(heap, pi)
    else:
        return


def downHeapyfiy(heap, i):
    if i >= len(heap):
        return
    lChild = 2*i+1
    rChild = 2*i+2

    if (lChild < len(heap)) and heap[lChild] > heap[i] and heap[lChild] > heap[rChild]:
        tmp = heap[lChild]
        heap[lChild] = heap[i]
        heap[i] = tmp
        downHeapyfiy(heap, lChild)
    elif (rChild < len(heap)) and heap[rChild] > heap[i] and heap[rChild] > heap[lChild]:
        tmp = heap[rChild]
        heap[rChild] = heap[i]
        heap[i] = tmp
        downHeapyfiy(heap, rChild)
    else:
        return


def deleteFromHeap(heap):
    if len(heap) == 0:
        return
    item = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    print(item)
    downHeapyfiy(heap, 0)


arr = [1, 22, 3, 21, 12, 15, 24, 13]
heap = []
createHeap(arr, heap)
print(heap)

