import math  # What is this for?


def area_circle(radius: float) -> float:
    return math.pi * radius * radius


def cost_of_pizza(radius: float, price_per_sq_in: float) -> float:
    return area_circle(radius) * price_per_sq_in


def main() -> None:
    small_pizza_cost = cost_of_pizza(6, 0.05)
    medium_pizza_cost = cost_of_pizza(8, 0.05)
    large_pizza_cost = cost_of_pizza(12, 0.05)

    print(f"Small pizza cost: ${small_pizza_cost:.2f}")
    print(f"Medium pizza cost: ${medium_pizza_cost:.2f}")
    print(f"Large pizza cost: ${large_pizza_cost:.2f}")


if __name__ == "__main__":
    main()
