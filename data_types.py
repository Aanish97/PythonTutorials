

def func():
    i: int = 5
    print(i)

    fl: float = 5
    print(fl)

    st: str = 'abc'
    print(st)

    bl: bool = True
    print(bl)

    ls: list = [1, 2, 4, 5, '14', True]
    # ordered, mutable, allows duplicates

    st: set = {1, 2, 4, 5, '14', True, 1, 1}
    # unordered, mutable, doesn't allows duplicates

    tp: tuple = (1, 2, 4, 5)
    # ordered, immutable, allows duplicates

    print(ls)
    print(st)
    print(tp)

    dc: dict = {'k': 'v', 'v': 'vv'}

    print(dc.keys())
    print(dc.values())
    print(dc.items())


if __name__ == '__main__':
    func()
