def clamp(x: float, low: float = 0, high: float = 1) -> float:
    if x < low:
        return low
    if x > high:
        return high
    return x


def main():
    print(clamp(1.7))
    print(clamp(1.7, high=10))


if __name__ == "__main__":
    main()
