import thread

def funt(no, a):
    while True:
        a= a+1
        print 'thread no %d = %d,' % (no, a)
        
def test():
    thread.start_new_thread(funt, (1,2))
    thread.start_new_thread(funt, (2,2))
    
if __name__ == '__main__':
    test()