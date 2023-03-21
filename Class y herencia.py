#Class y herencia (Introducción).

class transport:
    def speed(self):
        print("Fast")

class Cars(transport):
    pass

class Bikkers(transport):
    pass

class Boat(transport):
    pass

ferrari=Cars()
yamaha=Bikkers()
yate=Boat()


ferrari.speed()
yamaha.speed()
yate.speed()



