class Circle:
    radius = 0
    color = ""
    position = 0

    def circumfrence(self):
    	return 3.141 * 2 * self.radius

circleA = Circle()
circleA.radius = 15
circleA.color = "red"
circleA.position = 1

circleB = Circle()
circleB.radius = 11
circleB.color = "blue"
circleB.position = 2

print("The color of circleA is:")

print(circleA.color)


