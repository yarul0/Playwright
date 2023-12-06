try:
    a, b = map(int, input().split())
    result = a / b
except ZeroDivisionError:
    print('Division to zero')
except ArithmeticError:
    print('Any arithmetic error')
except Exception:
    print('All exceptions')


