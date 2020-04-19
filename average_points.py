import numpy as np
from matplotlib import pyplot as plt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '{}, {}'.format(self.x, self.y)        


class Rect():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.avg_point = None
    
    def avg(self):
        avg_point_x = (self.a.x + self.b.x) / 2
        avg_point_y = (self.a.y + self.b.y) / 2
        
        # Creates new avg point
        self.avg_point = Point(avg_point_x, avg_point_y)

        return self.avg_point

    def plot(self):
        x_values = [self.a.x, self.avg_point.x]
        y_values = [self.a.y, self.avg_point.y]
        plt.plot(x_values, y_values, marker='o', color='b')

        x_values = [self.avg_point.x, self.b.x]
        y_values = [self.avg_point.y, self.b.y]
        plt.plot(x_values, y_values, marker='o', color='b')

        plt.title('Rect')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
    
    def __repr__(self):
        return '({})----({})'.format(self.a, self.b)


if __name__ == '__main__':
    import sys

    x1 = float(sys.argv[1])
    y1 = float(sys.argv[2])
    x2 = float(sys.argv[3])
    y2 = float(sys.argv[4])
    a = Point(x1, y1)
    b = Point(x2, y2)

    r = Rect(a, b)

    r_avg = r.avg()

    print(r)
    print(r.avg_point)
    r.plot()
