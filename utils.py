def cm2_to_m2(area_cm2: float) -> float:
    return area_cm2 / 10000


def compare_areas(shape1, shape2) -> str:
    area1 = shape1.area()
    area2 = shape2.area()

    if area1 > area2:
        return "The first shape has a larger area."
    elif area1 < area2:
        return "The second shape has a larger area."
    else:
        return "Both shapes have the same area."
