def get_value():
    try:
        x, y = map(int, input().split())
        return x, y
    except ZeroDivisionError:
        print('Division to zero')
    except Exception as e:
        print(e)
        return 0,0
    finally:
        print('FINALLY works always')

x, y = get_value()
print(x, y)
