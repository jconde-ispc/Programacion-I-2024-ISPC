def intdiv(a, b):
    try:
        result = a // b
    except TypeError:
        print('Check operands. Some of them seems strange...')
    except ZeroDivisionError:
        print('Please do not divide by zero...')
    except Exception:
        print('Ups. Something went wrong...')

intdiv(3, 0)

intdiv(3, '0')