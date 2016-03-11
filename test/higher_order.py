#def annotated(f):
#    def new_f():
#        print("Won't call the callback")
#    return new_f

#@annotated
def callback():
    print("Inside the callback")

def higher_order(f):
    print("Inside the main function")
    f()

class MyAwesomeClass():
    def __init__(self, f):
        self.callback = f

    def run(self):
        print("Inside the class")
        self.callback()

#higher_order(callback)
MyAwesomeClass(callback).run()

#callback()
