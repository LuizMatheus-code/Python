def converting(number):
    #This function receives a number from 0 to 10 and returns a letter that represents the student's result
    
    try: 
        #This is to convert the number to a float if it's not already of that type
        number = float(number)
        
        #if it's between 0 and 1, they got E-
        if 0 <= number <= 1:
            return  "E-"
        
        #if it's between 1 and 2, they got E

        elif 1.1 <= number <= 2:
            return "E"
        
        #if it's between 2 and 3, they got D-
        elif 2.1 <= number <= 3:
            return "D-"
        
        #if it's between 3 and 4, they got D
        elif 3.1 <= number <= 4:
            return "D"
        
        #if it's between 4 and 5, they got C-
        elif 4.1 <= number <= 5:
            return "C-"
        
        #if it's between 5 and 6, they got C
        elif 5.1 <= number <= 6:
            return "C"
        
        #if it's between 6 and 7, they got B-
        elif 6.1 <= number <= 7:
            return "B-"
        
        #if it's between 7 and 8, they got B
        elif 7.1 <= number <= 8:
            return "B"
        
        #if it's between 8 and 9, they got A-
        elif 8.1 <= number <= 9:
            return "A-"
        
        #if it's between 9 and 10, they got A
        elif 9.1 <= number <= 10:
            return "A"
        
        else:
            #This block of code will only happen if the number isn't between 0 and 10
            print("invalid")
    except:
        #This block will only happen if the number can't be converted to float
        print("Invalid")

def age_group(age):
    #This function gets a number from 1 to 150 and returns the age group of the person

    try:
        #Here, the given parameter will be converted to an integer, if such a thing can't be done, the function will return "Invalid"
        age = int(age)

        #if the age is between 1 and 17, return "Minor age". Notice that there's a +1 on the range to make sure it reaches the 17
        if age in range(1, 17 + 1):
            return "Minor age"
        
        #if the age is between 18 and 64, return "Major age", once again, there's a +1 at the end for the range to reach 64
        elif age in range(18, 64 + 1):
            return "Major age"
        
        #if the age is between 65 and 99, return "Senior age"
        elif age in range(65, 99 + 1):
            return "Senior age"
        
        #if the age is between 100 and 150, return "Centenary age"
        elif age in range(100, 150 + 1):
            return "Centenary age"
        
        #This block of code will only happen if the number isn't between 1 and 150
        else:
            return "Invalid"

    #Here, the "Invalid" will only be returned if the given parameter can't be converted to a string
    except:
        return "Invalid"

if __name__ == "__main__":

    #Here, the user will be requested to type the student's result. It'll only work if the number is between 0 and 10
    student_result = input("Type here the student's result: ")

    #Here, the user will type the student's age, which will be converted to the group age afterwards
    student_age = input("Type here the student's age: ")

    #The number that was given before will be used on the function and a representative letter in form a string will be returned 
    conversion_of_result = converting(student_result)

    #Now, the student's age will be used in the function and a string will be returned representing the student's age group
    student_age_group = age_group(student_age)

    #Now, the script will show the user which letter the student got basend on the number from before
    print(f"The student who's in {student_age_group} got {conversion_of_result}")
