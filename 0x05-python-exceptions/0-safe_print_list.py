def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for item in my_list:
            if x>i:
                print("{}".format(item),end="")
                i += 1
        print("")
        return i
    except:
        print("ex")
        return i
