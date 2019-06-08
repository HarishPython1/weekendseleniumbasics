from A import A

class B(A):
    def __init__(self):
        #super().__init__()
        A.__init__(self)
        print("in B")
b = B()
