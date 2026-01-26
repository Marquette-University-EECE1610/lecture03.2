def clamp(x: float, low: float = 0, high: float = 1) -> float:
    if x < low:
        return low
    if x > high:
        return high
    return x


print(clamp(1.7))
print(clamp(1.7, high=10))
