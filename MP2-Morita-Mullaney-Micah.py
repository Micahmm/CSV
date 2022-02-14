import csv, mymod

##Part 1

##Below is a function that pulls from the inputs for a specfic election year and then put it into a nested list based from the csv file.

def nested_list(file_name, input_year):
    with open(file_name,"r") as csvfile:
        print('Loading...')
        year = csv.DictReader(csvfile)
        total_list = [row for row in year if row["YEAR"] == input_year]
        print(len(total_list),"rows loaded")
        print('Done!')
    return total_list
##Collecting input from user

while True:
    file_name = input("Input a file name:")
    if file_name == "1976-2016-president.csv":
        break
    else:
        print("File not found, please try again.")

##List to etablish years that are acceptable for input any year outside of these will not be accepted.
election_year = [1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]   

while True:
    input_year = input("Enter a year:")
    if int(input_year) not in election_year:
        print("Election year invalid, please try again.")
    else:
        break
    
##Nested lists of the slected data. This is just the raw data and is formated and structued later in the code.
pres_data = nested_list(file_name, input_year)

##Part 3

##For each problem I created a function as the user has to input which they function they want, inorder for the each problem not to run in order I just set them as functions to be called on later in the code.  Each function also calls from the mymod.py file for the fucntions located in there.

##Part 3 A

def fun_a():
    
    headers = ["Candidate Name","Votes"]

    mymod.tallied_data(pres_data,"CANDIDATE","VOTES") 


    mymod.table_print(headers, mymod.tallied_data(pres_data,"CANDIDATE","VOTES"), width=30)

##Part 3 B

def fun_b():
    headers = ["Party","Vote"]

    mymod.tallied_data(pres_data,"PARTY","VOTES") 


    mymod.table_print(headers, mymod.tallied_data(pres_data,"PARTY","VOTES"), width=30)

##Part 3 C

def fun_c():
    vote_count = 0
    for vote  in pres_data:
        if vote["WRITEIN"] == "TRUE":
            vote_count += int(vote["VOTES"])
    print(vote_count,"votes were write in's.")

##Part 3 D

def fun_d():
    winner = mymod.tallied_data(pres_data,"CANDIDATE","VOTES")
    print(winner[0][0],"won the popular vote with",winner[0][1],"votes")

##Takes input to select the proper function 

##List to establish the functions that are accepted from the user input.
option_list = ["A","B","C","D"]

while True:
    option_input = input("Which option would you like to use(Type 'Done' when finsihed):")
    if option_input != "Done":
        if option_input not in option_list:
            print("Not a function, please try again.")
        elif option_input == "A":
                    fun_a()
        elif option_input == "B":
                    fun_b()
        elif option_input == "C":
                    fun_c()
        elif option_input == "D":
                    fun_d()
    else:
        print("Thanks for using this program, have a nice day!")
        break






