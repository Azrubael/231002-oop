class Point:
    color = 'red'
    circle = 2
    
    def __init__(self, x=0, y=0):
        print ("Call of __init__")
        self.x = x
        self.y = y
        
    def __del__(self):
    """This method is calling automatically at the end of the scrypt"""
        print("Deleting an instance: " + str(self))
    
    def set_coords(self, x, y):
        print("Call of set_coords")
        self.x = x
        self.y = y
        
    def get_coords(self):
        print("Call of get_coords")
        return self.x, self.y
        

pt1 = Point()
print(pt1.__dict__)
pt1.set_coords(10, 20)
print(pt1.__dict__)
print()

pt2 = Point(19, 37)
print(pt2.__dict__)