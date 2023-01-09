# Example
# Define Bird Class
class Bird:
    def __init__(self):
        print("Bird is created")

    def showName(self):
        print("Bird")


class Owl(Bird):
    def __init__(self):
        print("owl class")


littleowl = Owl()
littleowl.showName()
