def clamp(x: float, low: float = 0, high: float = 1) -> float:
    if x < low:
        return low
    if x > high:
        return high
    return x


def main():
    print("Testing clamp(1.7)... ", end="")
    assert clamp(1.7) == 1.0
    print("PASS")

    print("Testing clamp(1.7, high=10)... ", end="")
    assert clamp(1.7, high=10) == 1.7
    print("PASS")

    print("Testing clamp(-5, low=-10, high=0)... ", end="")
    assert clamp(-5, low=-10, high=0) == -5
    print("PASS")


if __name__ == "__main__":
    main()
