# Point 클래스 정의
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def show(self):
        print(f'Point({self.x}, {self.y})')


# Rectangle 클래스 정의
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)  # left-top
        self.rb = Point(x2, y2)  # right-bottom

    def show(self):
        print('Rectangle:')
        self.lt.show()
        self.rb.show()

  


# 테스트 함수 정의
def test():
    p1 = Point()
    p2 = Point(2, 3)
    p1.show()
    p1.set(10, 20)
    p1.show()
    p2.show()
    x, y = p2.get()
    print(f'x={x}, y={y}')

    # Rectangle 객체 생성 및 테스트
    rect = Rectangle(1, 2, 4, 6)
    rect.show()
    


# 주 프로그램부
if __name__ == '__main__':
    test()
