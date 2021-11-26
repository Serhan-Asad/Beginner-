class Employee():
    count = 0
    def __init__(self):
        pass
    def set_description(self, first, last, contact, designation):
        self.first = first
        self.last = last
        self.contact = contact
        self.email = '{}.{}@email.com'.format(self.first, self.last)
        self.designation = designation
        Employee.count += 1

    def storing_to_file(self):
        f = open('test.dat', 'a')
        f.write('{},{} {},{},{},{}\n'.format(Employee.count, self.first, self.last, self.contact, self.email, self.designation))
        f.close()

    def reading_from_file(self):
        f = open('test.dat', 'r')
        details = f.read()
        details_list = details.split("\n")
        contents = details_list[View_name - 1]
        final_list = contents.split(",")
        for x in final_list:
            print(x)
        
while True:
    person = input("Do you want to add a person or view details of a person(Add/View) ")
    if person == "Add":
        while True:
            person_first = str(input("enter first name "))
            person_last = str(input("enter last name "))
            person_contact = str(input("enter contact "))
            person_designation = str(input("enter designation "))
            person = Employee()
            person.set_description(person_first, person_last, person_contact, person_designation)
            person.storing_to_file()
            new_person = input("Do you want to add more person(y/n): ")
            if new_person == "n":
                break
    elif person == "View":
         while True:
             View_name = int(input("enter number "))
             person = Employee()
             person.reading_from_file()
             View_more = input("Do you want to view more person(y/n): ")
             if View_more == "n":
                break
        
        
    else:
        break
    

    

        
    
                    

        




