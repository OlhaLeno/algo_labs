def min_eat_speed(piles, h):
    max_bananas = max(piles)
    left = 1
    right = max_bananas

    while left < right:
        mid = (left + right) // 2
        if can_eat_all_bananas(piles, h, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def can_eat_all_bananas(piles, h, k):
    hours = 0
    for bananas in piles:
        hours += (bananas + k - 1) // k

    return hours <= h


piles = [3, 6, 7, 11]
h = 8
print(min_eat_speed(piles, h))
