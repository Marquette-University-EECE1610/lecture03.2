x = 10


def change_x():
    x = 5
    print(f"Inside change_x function, x = {x}")


change_x()
print(f"Outside change_x function, x = {x}")


def change_x_again(x: int) -> None:
    print(f"Inside change_x_again function with parameter, x = {x}")
    x = 20
    print(f"Inside change_x_again function after  assigning a new value to x, x = {x}")


change_x_again(x)
print(f"Outside change_x_again function, x = {x}")
