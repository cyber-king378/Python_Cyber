import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","age","Contact Number","Email"])
        writer.writerow(info_list)
        

if __name__ == '__main__':
    condition = True
    
    while(condition):
        student_info = input("Enter the student info in format (Name,Age,Contact_number,Email) :")
        #split
        student_info_list = student_info.split(" ")
        
        
        print("\nEntered Information\nName : {}\nAge : {}\nContact :{}\nEmail : {}\n".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Entered information is correct y/n : " )
        if choice_check == "y":
            write_into_csv(student_info_list)
            condition_check = input("Enter y/n to add or stop to enter info : ")
        
            if condition_check == "n":
                condition = False
         
        else:
            print("\nReenter the values!!!!!")
        