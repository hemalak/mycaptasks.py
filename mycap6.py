import csv
def write_csv(information_list):
    csv_file=open("student_info.csv","a",newline='')
    writer=csv.writer(csv_file)
    if csv_file.tell()==0:
        writer.writerow(["NAME","DOB","DEPT","CONTACT_NUMBER","E-MAIL_ID"])
    writer.writerow(information_list)
if __name__ =='__main__':
    condition=True
    student=1
    while(condition):
        student_information=input("Enter student #{} information  in the format ( Name , dob, dept, Contact_Number , E-mail ID): ".format(student))
        student_information_list=student_information.split(' ')
        print("STUDENT INFORMATION is : \nNAME: {},\nDOB:{},\nDEPT:{} \nCONTACT_NUMBER:{},\nE-MAIL_ID:{}"
              .format(student_information_list[0],student_information_list[1],student_information_list[2],student_information_list[3],student_information_list[4]))
        check_again=input("Is the entered information correct ? (yes/no) :")
        if check_again=='yes':
              write_csv(student_information_list)
              checking_condition=input("Enter if you want to enter information for another student (yes/no): ")
              if checking_condition=='yes':
                  condition=True
                  student=student+1
              elif checking_condition=='no':
                  condition=False
        elif check_again=='no':
             print("\n PLEASE RE-ENTER AGAIN !")

        else:
            print("Re-enter again")
    

