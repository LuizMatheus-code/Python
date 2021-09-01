while True:
    print('[M] male\n[F] female')
    gender = input("type: ").upper()
    if gender == "M" or gender == "F":
        break
    else:
        print("type one of the above")
print(f"the gender is {gender}")
