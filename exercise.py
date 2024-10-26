  
#I Declared a variable that stores a value in a memory for salim to store his salary for the month 
salim_salary=float(input("Salim please enter your salary for the month : "))

#a variable called name_of_the_month  
name_of_the_month=input("please enter the name of the month which you want to store the salary for : ")

#a variable for salim saving
salim_saving=float(input("Salim Please Enter The Following Percentages for How Much You Saved : "))

#a variable for monthly rent 
salim_monthly_rent=float(input("Salim Please Enter The Following Percentages for How Much Is Your Rent Per Month : "))

#a variable for electricity consumtion 
salim_electricity_consumtion=float(input("Salim Please Enter The Following Percentages for How Much You Consume Your Electricity : "))
  
#calculate the percentage of savings based on his salary 
salim_total_saving=(salim_saving / 100) * salim_salary

#the percentage of rent based on the salary 
salim_total_rent=(salim_monthly_rent / 100) * salim_salary

#calculate the percentage of electricity based on the salary 
salim_total_electricity_consumtion=(salim_electricity_consumtion / 100) * salim_salary

#adding  total  consumtion 
salim_total_consumtion=salim_total_saving + salim_total_rent + salim_electricity_consumtion

#adding  yearly rent and electricty  multiplying by 12
salim_yearly_rent_and_electricity=(salim_total_rent + salim_electricity_consumtion) * 12

#salim_remainder_after_expensis  
salim_remainder_after_expensis=salim_salary / salim_total_consumtion

#salim salary doubled just for fun 
salim_total_salary_doubled=salim_salary ** 2

#salim additional amount assuming it is 50
salim_additional_amount=50

#calculating total additional amount 
salim_total_addtional_amount=salim_additional_amount / salim_total_saving

#print the salary of salim 
print("Salim salary is : " , salim_salary)

#print the name of the month 
print("the name of the month is : " , name_of_the_month)

#print the total saving
print("Salim total saving is : " , salim_total_saving)

#print the total rent
print("Salim total rent is : " , salim_total_rent)

#print the total electricity consumtion 
print("Salim total electricity consumtion : " , salim_total_electricity_consumtion)

#print the total  consumtion 
print("Salim total  : " , salim_total_consumtion)

#print the total electricity consumtion 
print("Salim yearly rent and electricity : " , salim_yearly_rent_and_electricity)

#print the total remainder after expensis 
print("Salim remainder after expensis  : " , salim_remainder_after_expensis)

#print the total salary doubled 
print("Salim total  : " , salim_total_salary_doubled)

#print the total additional amount 
print("Salim total  : " , salim_total_addtional_amount)

