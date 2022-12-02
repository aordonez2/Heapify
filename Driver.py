#import Heap
from heap import *
class Driver:
    try:
        fileName = input("\nEnter File Name:")
        
        with open(fileName) as f:
            content_list = f.readlines()

        # remove new line characters
        content_list = [x.strip() for x in content_list]
        print(content_list)#raw list of paths
        read_paths(content_list)#process the raw list
    except:
        print('\n\n\nYou have entered an invalid File Name.\n\n\n')