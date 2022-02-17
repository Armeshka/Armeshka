def main():
    x, y = 100, 100
    width, height = 200, 200

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Функция, рисует домик ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота от низа фундамента
    :return: None
    """
    print("рисую домик", x, y, width, height)
    foundation_heigh = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * width
    roof_height = height - foundation_heigh - walls_height

    draw_house_foundation(x, y, width, foundation_heigh)
    draw_house_walls(x, y - foundation_heigh, walls_width, walls_height)
    draw_house_roof(x, y - foundation_heigh - walls_height, width, roof_height)


def draw_house_foundation(x, y, width, height):
    """
    Функция, рисует фундамент ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины фуфндамента
    :param y: координата y низа фундамента
    :param width: полная ширина фундамент (фундамент или вылеты крыши включены)
    :param height: полная высота фундамента от низа фундамента
    :return: None
    """
    print(' рисую фундамент')
    pass


def draw_house_walls(x, y, width, height):
    """
        Функция, рисует стены ширины width и высоты height от опорной точки (x, y),
        которая находится в середине нижней точки фундамента.
        :param x: координата x середины стены
        :param y: координата y низа стены
        :param width: полная ширина стен
        :param height: полная высота стены от верхней точки фундамента
        :return: None
        """
    print(' рисую стены')
    pass


def draw_house_roof(x, y, width, height):
    """
        Функция, рисует крышу ширины width и высоты height от опорной точки (x, y),
        которая находится в середине нижней точки фундамента.
        :param x: координата x середины фуфндамента
        :param y: координата y низа фундамента
        :param width: полная ширина фундамент (фундамент или вылеты крыши включены)
        :param height: полная высота фундамента от низа фундамента
        :return: None
        """
    print(' рисую крышу')
    pass


main()

# задача
# нужна декомпозиция