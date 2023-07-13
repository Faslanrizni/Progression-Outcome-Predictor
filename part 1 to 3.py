# Author : Faslan Rizni
#20221323
#w1956103

total = 0
credit_defer = 0
credit_fail = 0
str_count = 0
keep_going = "y"
progress_count = 0
retriever_count = 0
exclude_count = 0
trailer_count = 0
progression_list = []


#The function repeatedly prompts the user to enter marks, and checks to see if the input is a valid integer

def int_input(message,error_message_1,error_message = "out of range"):
   while True:
      try:
         marks = int(input(message))
         
      except ValueError:
         print(error_message_1)
         continue
      if marks not in range(0,121,20):
         print(error_message)
         continue
      break
   return marks

while keep_going == "y":
# Prompt the user for the number of credit_pass, credit_defer, and credit_fail marks

    credit_pass = int_input("enter the credit_pass marks: ","invaid input re enter integer input",)
    credit_defer = int_input("enter the credit_defer marks: ","invaid input re enter integer input")
    credit_fail =int_input("enter the credit_fail marks: ","invaid input re enter integer input") 
    credit_list = [credit_pass,credit_defer,credit_fail]
    credit_marks = []
    credit_marks.append(credit_list)
    
# Creating a list of the credit marks and append it to the credit_marks list    
#getting the total of marks

    total = credit_pass + credit_defer + credit_fail 
    print(total)
    
    if total != 120:
        print("total is incorrect")
        continue
    else:
        str_count += 1
              
        if credit_pass == 120:
            progression = "progress"
            progress_count += 1

        elif credit_pass == 100:
            progression = "progress (module trailer"
            trailer_count += 1

        elif(credit_fail == 80 or credit_fail == 100 or credit_fail == 120):
            progression = "Exclude"
           
            exclude_count += 1

        else:
            progression = "Do not progress – module retriever"
            retriever_count += 1
        print(progression)
        credit_marks.append(progression)
    progression_list.append(credit_marks)
# append progression to credit_marks list
# and append credit_marks to progression_list to reuse in part 3
   
    

        
#histrogram part---------------------------------------------------------
    while True:
        keep_going = str(input("Do you need to add another set of data(enter y for yes)"))
        if keep_going == "q":
           print("-"*60)
           print("histogram")
           print("Exclude", exclude_count,"  ",":", exclude_count * "*")
           print("Retriever",retriever_count,"",":",retriever_count * "*")
           print("Trailer",trailer_count,"  ",    ":",trailer_count * "*")
           print("Progress",progress_count," ",  ":",progress_count * "*")
           print(str_count," outcomes in the total.")
#list part----------------------------------------------------------------
           print("-"*60)
           print("part 2:")

           for i in progression_list:     # for example i prints on this stage [[120, 0, 0], 'progress'] like this but to get that hopeful output we do following methord
              print(i[1], "-" ,end = '')
              x =str(i[0])               # converting list to srting because of 'list' object has no attribute 'replace' 
              x = x.replace(']','')
              x = x.replace('[','')
              print('',x)

# text file part----------------------------------------------------------             
           print("-"*60)
           #print('part 3 :')
           progression_file= open("progression_list.txt",'w')
           for i in progression_list:
              progression_file.write(i[1])
              progression_file.write("-")
              y =str(i[0])
              y = y.replace(']','')
              y = y.replace('[','') 
              progression_file.write(y)
              progression_file.write('\n')
           progression_file.close()


              

        elif keep_going == 'y':
           break
        else:
           print("enter 'q' or 'y'")
           continue
        break 
   



           

              
    


              



              




              


                     
        




  

         
     

  





