# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:  W1985545
# Date: 20/4/2023

#variables 
progress=0
trailer=0
retriver=0
exclude=0
C=[0,20,40,60,80,100,120]
progress_data=[]
choice="y"
dict={} 

#To input progression data
while choice=="y":
    try:
        uow_no=str(input("Enter student uow number :"))
        while True:
            pass_credits=int(input("Please enter your credits at pass: "))
            if pass_credits in C:
                break
            else:
                print("Out of range.")
        while True:
            defer_credits=int(input("Please enter your credit at defer: "))
            if defer_credits in C:
                break
            else:
                print("Out of range.")
        while True:
            fail_credits=int(input("Please enter your credit at fail: "))
            if fail_credits in C:
                break
            else:
                print("Out of range.")

    except (ValueError):
        print("Integer required") 
        continue
    
    #Calculate and check the total credits  
    total_credit=pass_credits+defer_credits+fail_credits
    if total_credit !=120:
        print("Total incorrect.")
        continue

    #Determine progression outcomes   
    if pass_credits==120:
        print("Progress")
        progress+=1
        Progression="Progress"

    elif pass_credits==100:
        print("Progress(module trailer)")
        trailer+=1
        Progression="Progress (module trailer)"

    elif fail_credits >=80:
        print("Exclude")
        exclude+=1
        Progression="Exclude"

    else: 
        print("Module retriever ")
        retriver+=1
        Progression="Module retriever"

    progress_data.append([Progression, pass_credits, defer_credits, fail_credits])
    dict[uow_no]=Progression, pass_credits, defer_credits, fail_credits 

    print(" ")

    #Ask the user's decision
    choice=input("Would you like to enter another set of data?Enter 'y' for yes or 'q' to quit and view results: ")

    #Dictionary(part 4)
    print("Part 4:")
    for key,value in dict.items():
        print(f"{key}: {value[0]} - {value[1]}, {value[2]}, {value[3]} ",end=" ")
