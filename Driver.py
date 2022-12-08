import Heap
import sys

##obj = Heap.Heap()
##from Heap import read_paths

class Driver:

    def main():
        myHeap = Heap.Heap()
        myHeap.read_paths()
        myHeap.build_complete_tree(0, myHeap.tempPath[0], myHeap.tempPath)
        print (myHeap.ll)
        #myHeap.build_tempPath_helper(myHeap.tempPath, content_list) 
    if __name__=="__main__":
        main()
