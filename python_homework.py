import math

def get_radius():
    radius = int(input("반지름을 입력하세요: "))
    return radius

def get_circle_area(radius):
    area = math.pi * radius ** 2
    return area

def main():
    radius = get_radius()
    area = get_circle_area(radius)
    print("반지름이", radius, "인 원의 넓이는:", area)

if __name__ == "__main__":
    main()

