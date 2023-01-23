def func(a):
    print(a)
def func2(a):
    try:
        print(int(a)+10)
    except ValueError:
        print("error")