from roster import Roster
from student import student

print("Start roster:")

my_roster = Roster()
my_roster.load("data.csv")
print(my_roster)

while(1==1):
    print("(A)add new student")
    print("(O)pen file)")
    print("(S)ave file")
    print("(V)iew roster")
    print("(Q)uit program")
    choice = input("What would you like to do?\n")

if choice == "a":
    fn = input("First name: ")
    In = input("Last name: ")
    gr = int(input("Grade: "))
    my_roster.add_student_info(fn, ln, gr)
    print("Adding new student...")

elif choice == "o":
    file_name = input("Filename? ")
    print("Opening file... \n")

elif choice == "s":
    file_name = input("Filename? ")
    print("Saving to file", file_name)
    my_roster .save(file_name)

elif choice == "v":
    print("View roster...")
    print(my-roster)

elif choice == "q":
    print("Quiting program... \n")
    break
