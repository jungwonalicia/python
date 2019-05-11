import threading

def run(args):
    for x in range(0, 100):
        print(args, ": " , x)

run1 = threading.Thread(target=run, args=('★',))
run2 = threading.Thread(target=run, args=('☆',))
run3 = threading.Thread(target=run, args=('☎',))

run1.start()
run2.start()
run3.start()