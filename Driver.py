class Driver:
    try:
        fielName = input("\nEnter Fiel Name:")
        
        with open(fielName) as f:
            content_list = f.readlines()

        # remove new line characters
        content_list = [x.strip() for x in content_list]
        print(content_list)
    except:
        print('\n\n\nYou have entered an invalid File Name.\n\n\n')
