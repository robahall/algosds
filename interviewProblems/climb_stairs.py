def cache(func):
    cache = {3:3, 2:2}
    def wrapper(floor):
        if floor in cache:
            return cache[floor]
        result = func(floor)
        cache[floor] = result
        return result
    return wrapper

@cache
def climb_stairs(n):
    return climb_stairs(n-1) + climb_stairs(n-2)

if __name__ == "__main__":
    print(climb_stairs(45))
