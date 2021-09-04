storage = list()
counter = 0
while True:
    adding = int(input("type a number: "))
    if adding not in storage:
        storage.append(adding)
        counter += 1
    else:
        print("duplicated values cannot be added")
    print('[0] continue\n[1] stop')
    continue_question = int(input('type: '))
    if continue_question == 1:
        break
print(f'total of elements {counter}')
print(storage)
storage.sort(reverse=True)
print(storage)
print(storage.index(5))
