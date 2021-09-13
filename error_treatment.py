
try:
    1
except ValueError as error:
    print(f'fail. {error}')
except NameError as name:
    print(name)
except TypeError as typ:
    print(typ)
else:
    print()
finally:
    print("i happen everytime")
    try:
        2
    except:
        2
