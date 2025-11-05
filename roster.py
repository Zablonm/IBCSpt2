from student import student 

class Roster:
    def__init__(self):
        self.students = []

    def __str__(self):
        s = ""
        for student in self.students:
            s += student.first_name + " " + student.last_name + " " + str(student.grade) + "\n"
        return s
    def load(self, filename):
        with open(filename, "r") as file_obj:
            for line in file_obj:
                line = line.strip
                parts = line.split(";")
                tmp = student(parts[0], parts[1], int(parts[2]))
                self.add(tmp)

        """

        #open file name for reading
        file_obj = open(filename, "r")
        #read all the lines
        lines = file_obj.readlines()
        for line in lines:
            line = line.strip()
            parts = line.split(";")
            #print(line)
            tmp = Student(parts[0], parts[1], int(parts[2]))
            self.add(tmp)
        """
    
    def save(self, filename):
        with open(filename, "w") as file_obj:
            for student in self.students:
                file_obj.write(student.first_name + "," + student.last_name + "," + str(student.grade) + "\n")
    
    def add(self, new_student):
        self.students.append(new_student)
    def add_student_info(self, fn, ln, gr):
        temp = Student(fn, ln, gr)
        self.add(temp)

test = Roster()
#test.add_student_info("Zablon", "Mulugetter", 12)
#test.add_student_info("Jackson", "Kwug", 12)
#s = Student("Angela", "Dignan", 12)
#test.add(s)
test.load("data.csv")
print(test)
