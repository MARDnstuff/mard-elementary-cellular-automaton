def positive(n: int, size: int) -> int:
    if n < 0 :
        pos_n: int = n*(-1)
        res: int = size - (pos_n%size)
        if res < 0:
            raise IndexError("Index is negative")
        return res
    else:
        return n
