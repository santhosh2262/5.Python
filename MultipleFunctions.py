class multipleFunctions():

    def list_ai_subfields():
        ai_subfields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfield in ai_subfields:
            print(subfield)
            end=ai_subfields
        return end    
    def oddEven():
        number=int(input("Enter a number:"))
        if number%2==0:
            print(number,"is even number")
            end=number,"is even number"
        else:
            print(number,"is odd number")
            end=number,"is odd number"
        return end    
    def check_eligibility():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))

        if gender.lower() == "male" and age >= 18:
            print("Not Eligible")
            eligibility = "Not Eligible"
        else:
            print("Eligible")
            eligibility = "Eligible"
        return eligibility   
    def calculate_percentage():
        subject1=23
        subject2=45
        subject3=34
        subject4=23
        subject5=23
        total=subject1+subject2+subject3+subject4+subject5
        percentage=(total/500)*100
        print("Total:",total)
        end="Total:",total
        print("Percentage:",percentage)
        end="Percentage:",percentage
        return end
    def calculate_triangle():
        height=3
        breadth=4
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        end="Area of Triangle:",area
        height1=3
        height2=4
        breadth=45
        perimeter=height1+height2+breadth
        print("Perimeter of Triangle:",perimeter)
        end="Perimeter of Triangle:",perimeter
        return end