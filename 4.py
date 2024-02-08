class Square:
    def getArea(self):
        return self.side * self.side

obj=Square()
obj.side=8
print(obj.side,obj.getArea())
