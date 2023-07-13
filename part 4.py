#Author: Faslan Rizni
#20221323
#w1956103

#defining variables--------------- 
total = 0
keep_going = 'y'
outcome = {} # defining outcome dictionary
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
   id_no = str(input("enter the student_no :(no need to start with 'w')"))
   credit_pass = int_input("enter the credit_pass marks: ","invaid input re enter integer input",)
   credit_defer = int_input("enter the credit_defer marks: ","invaid input re enter integer input")
   credit_fail =int_input("enter the credit_fail marks: ","invaid input re enter integer input") 
   credit_list = [credit_pass,credit_defer,credit_fail]
    
   total = credit_pass + credit_defer + credit_fail 
   
 #updaation part  
   if id_no in outcome:
      print("the sduent id is already exists do you wish to update(yes/no): ")
      update = input("need to update??:")
      if update != "yes":
         continue

    
   if total != 120:
      print("total is incorrect")
   else:
      if credit_pass == 120:
         progression = "progress"
           
      elif credit_pass == 100:
         progression = "progress (module trailer"
              
      elif(credit_fail == 80 or credit_fail == 100 or credit_fail == 120):
         progression = "Exclude"
      
      else:
         progression = "Do not progress – module retriever"
        
      credit_list.append(progression)
      outcome[id_no] = credit_list#defining dictionary to value and key
                                 

   keep_going = str(input("Do you need to add another set of data(enter y for yes)"))
    
    
   if keep_going == 'q':
      for key,value in outcome.items():
         print(key,':',value[-1],'-' ,end= '')
         X =str(value[0:3])
         Z = X.replace('[',' ')
         W = Z.replace(']',' ')
         print(W)

   elif keep_going == 'y':
      continue
    

