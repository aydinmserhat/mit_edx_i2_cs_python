class Coordinate(object):
    def __init__(self, x, y):
        """

        :rtype: object
        """
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x


    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y


    def __str__(self):
        return '<{0},{1}>'.format(str(self.getX()), str(self.getY))

    def __eq__(self, other):
        # First make sure `other` is of the same type
        """

        :type other: object
        """
        assert type(self) == type(other)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY == other.getY

    @property
    def __repr__(self):
        return 'Coordinate({0}, {1})'.format(str(self.getX()), str(self.getY))


c1 = Coordinate(3, 4)
c2 = Coordinate(4, 3)
print c1,c2
print c1==c2
