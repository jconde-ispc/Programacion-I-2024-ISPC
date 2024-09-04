def intdiv(a: int, b: int) -> int:
    try:
        return a // b
    except:
        print('Please do not divide by zero...')

intdiv(3, 0)