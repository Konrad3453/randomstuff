import random
import time

def loadingbar():
    def load(iteration, total, prefix="", suffix="", decimals=1, length=100, fill="▯"):
        precent = ("{0:." + str(decimals) + "f}").format(100* (iteration/float(total)))
        filledLength = int(length* iteration//total)
        bar = fill * filledLength + "-" * (length - filledLength)
        print(f'\r{prefix} |{bar}| {precent}% {suffix}', end="\r")
        if iteration == total:
            print()

    items = list(range(0,50))
    l = len(items)

    load(0, l, prefix=" Progress:", suffix="Complete:", length=l)
    for i, item in enumerate(items):
        time.sleep(0.1)
        load(i+1, l, prefix=" Progress:", suffix="Complete:", length=l)









#add cmd input here, programs above 
option = int(input("""Select program:
Loading bar: 1
"""))
if option == 1:
    loadingbar()

