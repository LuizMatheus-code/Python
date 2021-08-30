counter = 0
for number in range(0, 6):
    user = int(input(f"number {number}: "))
    if user % 2 == 0:
        counter += user
print(counter)
