# id name address phonenumber 

class Employe_Details:
    id=""
    name=""
    address=""
    phoneNumber=""
i=input("Enter the 1 for exit anything else to continue")

EmpDetails= Employe_Details()
Employe_Details_Dictionary=[]
while i!="1":
    EmpDetails.id=input("Enter Id of Employee ")
    EmpDetails.name= input("Enter Employee Name ")
    EmpDetails.address=input("Enter address ")
    EmpDetails.phoneNumber=input("Enter Phone Number ")

    Employe_Details_Dictionary.append({"id":EmpDetails.id, "name":EmpDetails.name, "address":EmpDetails.address, "Phone Number":EmpDetails.phoneNumber})
    print("Employee Details Updated")
    i = input("Enter 1 for exit anything else to continue")

deatails_ask=input("Enter 2 to view details of all employees and 3 view details by id ")

if deatails_ask=="2":
    for i in Employe_Details_Dictionary:
        print(f"Employe id {i['id']}\n Emplotee Name {i['name']}\n Employe Address {i['address']}\n Employee Phone Number {i['Phone Number']}")

if deatails_ask=="3":
    enterid=input("Enter id of employee you want to get detail")
    for i in Employe_Details_Dictionary:
        if i["id"]==enterid:
            print(f"Employe id {i['id']}\n Emplotee Name {i['name']}\n Employe Address {i['address']}\n Employee Phone Number {i['Phone Number']}")

            break
        else:
            print("Print a valid number ")

