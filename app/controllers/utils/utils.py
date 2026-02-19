def positive(n: int, size: int) -> int:
    if n < 0 :
        pos_n: int = n*(-1)
        res: int = size - (pos_n%size)
        return res
    else:
        return n
