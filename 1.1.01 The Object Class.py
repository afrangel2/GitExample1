class Circle:
    radius = 0;

    def circumfrence(self):
    	return 3.141 * 2 * self.radius

circleA = Circle()
circleA.radius = 15;
circleB = Circle()
circleB.radius = 11;

print("The difference in circumfrence between the two circles is:")

print(circleA.circumfrence() - circleB.circumfrence())


