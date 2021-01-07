print("\n\nCovid 19 Diagnosis Test")

def yes_no(choice):
    if choice=='Y':
        return 1
    elif choice=='N':
        return 0

def check_choice(choice):
    if choice!='Y' and choice!='N':
        print("Kindly enter 'Y' or 'N' as your answer.")
        return 0
    else:
        return 1

def calculate_percent(count):
    percent=(count/21)*100

    if percent <= 34:
        print("We believe that you are at a LOW RISK OF INFECTION, and need not test for COVID 19 at the moment.",
              "\nKindly keep taking necessary precautions and you will be good to go!")

    elif percent <= 75:
        print("We believe that you are at a MODERATE RISK OF INFECTION, but we recommend being cautious.\nIf symptoms intensify, consult a physician.",
              "\nKindly keep taking necessary precautions and you will be good to go!")

    else:
        print("We believe that you are at HIGH RISK OF INFECTION, we recommend being cautious. \nAvoid physical contact",
              "\nKindly take all precautions and consult a physician for a COVID test.\n")   
    
symptoms=['Cough',
          'Fever or chills',
          'Shortness of breath or difficulty breathing',
          'Muscle or body aches',
          'Sore throat',
          'New loss of taste or smell',
          'Diarrhea',
          'Headache',
          'Nausea or vomiting',
          'New fatigue',
          'Congestion or runny nose',]


print ("\nHello, we'll be asking you some questions.")
print("\nChecking for symptoms. Please answer with 'Y' or 'N'")

count=0
for i in symptoms:
    print(i,"?")
    flag=0
    while flag == 0:
        choice1 = str(input("Enter Answer (Y/N): "))
        flag = check_choice(choice1.upper())
    count+=1*int(yes_no(choice1.upper()))

print('\n')

flag=0
while flag == 0:
    choice2 = str(input("Do you live in a crowded location (~more than 10,000 people/sq.km)? (Y/N): "))
    flag = check_choice(choice2.upper())
    
count+=3*int(yes_no(choice2.upper()))

print('\n')

flag=0
while flag == 0:
    choice3 = str(input("Do you go out often (Y/N): "))
    flag = check_choice(choice3.upper())
    
count+=3*int(yes_no(choice3.upper()))

print('\n')

flag=0
while flag == 0:
    choice4 = str(input("Have you had close contact with someone diagnosed with COVID-19 or been notified that you may have been exposed to it? (Y/N): "))
    flag = check_choice(choice4.upper())
    
count+=5*int(yes_no(choice4.upper()))
print('\n')
calculate_percent(count)


    


