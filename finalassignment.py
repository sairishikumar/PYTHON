lists = ["Sub-fields in AI are:", "Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]

class SubfieldsInAI:
    
    def subfields():
        for temp in lists:
            print(temp)

class OddEven:
    
    def odd_even():
        num = int(input("Enter the number: "))
        if (num % 2) == 0:
            print(num, "is an even number")
        else:
            print(num, "is an odd number")

class EligibilityForMarriage:
   
    def eligible():
        gender = input("Enter your gender: ")
        age = int(input("Enter your age: "))
        if gender.lower() == "male":
            if age >= 21:
                print("Eligible")
            else:
                print("Not Eligible")
        elif gender.lower() == "female":
            if age >= 18:
                print("Eligible")
            else:
                print("Not Eligible")
        else:
            print("Invalid gender")

class FindPercent:
    
    def percentage():
        subject1=98
        subject2=87
        subject3=95
        subject4=95
        subject5=93
        add=subject1+subject2+subject3+subject4+subject5
        per=add/5
        print("Total:",add) 
        print("Percentage:",per)

class Triangle:
    
    def areaoftriangle():
        height=32
        Breadth=34
        area=height*Breadth/2
        print("area of triangle:",area)

    def Perimeteroftriangle1():
        height1=int(input("Enter the Height1:"))
        height2=int(input("Enter the height2:"))
        Breath=int(input("Enter the Breath:")) 
        Perimeter=height1+height2+Breath
        print("Perimeter of triangle:",Perimeter)

    def areaoftriangle1():
        height=int(input("Enter the Height"))
        Breadth=int(input("Enter the Breadth:"))           
        area=height*Breadth/2
        print("area of triangle:",area)
    



 
       











    