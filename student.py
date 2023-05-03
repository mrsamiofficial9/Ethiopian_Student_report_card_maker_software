# ----------------------IMPORT-------------------------------------

import math
import json
import os
import random
from datetime import datetime
from os.path import exists

#-------------------CONSTANTS--------------------------------------

FILE_PATH = "students.json"

#-----------------DATABASE-----------------------------------------

def get_data():
    if not exists(FILE_PATH):
        return {}
    f = open(FILE_PATH, "r")
    data = f.read()
    return json.loads(data)


def set_data(data):
    f = open(FILE_PATH, "w")
    json_data = json.dumps(data)
    f.write(json_data)


def get_students_as_list():
    result = []
    students = get_data()
    for student_id_number in students:
        student_data = students[student_id_number]
        student_data["id_number"] = student_id_number
        result.append(student_data)
    results_as_ll = list_to_linked_list(result)
    return results_as_ll


#------------------LINKED LIST------------------------------------------


class LinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def index(self, index):
        if index == 0:
            return self.value
        elif self.next is not None:
            return self.next.index(index - 1)
        else:
            return None

    def set_index(self, index, value):
        if index == 0:
            self.value = value
        elif self.next is not None:
            self.next.set_index(index - 1, value)

    def size(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.size()

    def append(self, value):
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.append(value)


def list_to_linked_list(arr):
    head = LinkedList()
    for i in range(len(arr) - 1, -1, -1):
        node = LinkedList(arr[i])
        node.next = head.next
        head.next = node
    return head.next

#-----------------HEAP SORT-----------------------------------------------------

def  heap_sort(input_list, field):
    range_start = int((input_list.size() - 2) / 2)
    for start in range(range_start, -1, -1):
                      sift_down(input_list, field, start, input_list.size()-1)
    range_start = int(input_list.size()-1)
    for end_index in range(range_start, 0, -1):
                      swap(input_list, end_index, 0)
                      sift_down(input_list, field, 0, end_index - 1)
    return input_list

def swap(input_list, a, b):
    a_value = input_list.index(a)
    b_value = input_list.index(b)
    input_list.set_index(a, b_value)
    input_list.set_index(b, a_value)


def sift_down(input_list, field, start_index, end_index):
    root_index = start_index
    while True:
        child = root_index * 2 + 1
        if child > end_index:
            break
        if child + 1 <= end_index and input_list.index(child)[field] < input_list.index(child):
            child += 1
        if input_list.index(root_index)[field] < input_list.index(child)[field]:
            swap(input_list, child, root_index)
            root_index = child
        else:
            break

#----------------------BINARY SEARCH--------------------------------------------

def text_binary_search(input_list, field, query):
    low = 0
    high = input_list.size() - 1
    query = make_text_searchable(query)
    while low <= high:
        mid = math.floor((low + high) / 2)
        if make_text_searchable(input_list.index(mid)[field]) > query:
            high = mid - 1
        elif make_text_searchable(input_list.index(mid)[field]) < query:
            low = mid +1
        else:
            return mid
    return -1


def make_text_searchable(text):
    return text.lower().replace(" ", "")

#---------------------ID NUMBER-------------------------------------------------

def generate_id_number():
    prefix = "00"
    result = ""
    for _ in range(0, 6):
        random_number = random.randint(1, 9)
        result += str(random_number)

    return prefix + result

#-----------------------UPDATE INFROMATION--------------------------------------

def update_information(id_number):
    students = get_data()
    print_horizontal_line()
    print("► 1 ∙ Full Name ")
    print_horizontal_line()
    print("► 2 ∙ Grade ")
    print_horizontal_line()
    print("► 3 ∙ Roll Number")
    print_horizontal_line()
    print("► 4 ∙ Section")
    print_horizontal_line()
    print("► 5 ∙ Gender")
    print_horizontal_line()
    print("\n\nSubject Point Out Of 100")
    print_horizontal_line()
    print("► 6 ∙ Physics Point")
    print_horizontal_line()
    print("► 7 ∙ Chemistry Point")
    print_horizontal_line()
    print("► 8 ∙ Biology Point")
    print_horizontal_line()
    print("► 9 ∙ Math Point")
    print_horizontal_line()
    print("► 10 ∙ English Point")
    print_horizontal_line()
    print("► 11 ∙ Ict Point")
    print_horizontal_line()
    print("► 12 ∙ Amharic Point")
    print_horizontal_line()
    print("► 13 ∙ Afaan Oromo Point")
    print_horizontal_line()
    print("► 14 ∙ Civic Point")
    print_horizontal_line()
    print("► 15 ∙ Hp Point")
    print_horizontal_line()
    print("► 16 ∙ Geography Point")
    print_horizontal_line()
    print("► 17 ∙ History Point")
    print_horizontal_line()
    print("► 18 ∙ Rank")
    print_horizontal_line()
    command = int(input("What to change? "))
    if command == 1:
        new_name = input("New Full Name: ")
        students[id_number]["full_name"] = new_name
    if command == 2:
        new_grade = input(int("New Grade: "))
        students[id_number]["grade"] = new_grade
    if command == 3:
        new_rollnumber = input(("New Roll Number: "))
        students[id_number]["rollnumber"] = new_rollnumber
    if command == 4:
        new_section = input("New Section: ")
        students[id_number]["section"] = new_section
    if command == 5:
        new_gender = input(str("New Gender: "))
        students[id_number]["gender"] = new_gender
    if command == 6:
        new_physics_point = float(input("New Physics Point: "))
        students[id_number]["physics_point"] = new_physics_point
    if command == 7:
        new_chemistry_point = float(input("New Chemistry Point: "))
        students[id_number]["chemistry_point"] = new_chemistry_point
    if command == 8:
        new_biology_point = float(input("New Biology Point: "))
        students[id_number]["biology_point"] = new_biology_point
    if command == 9:
        new_math_point = float(input("New Math Point: "))
        students[id_number]["math_point"] = new_math_point
    if command == 10:
        new_english_point = float(input("New English Point: "))
        students[id_number]["english_point"] = new_english_point
    if command == 11:
        new_ict_point = float(input("New Ict Point: "))
        students[id_number]["ict_point"] = new_ict_point
    if command == 12:
        new_amharic_point = float(input("New Amharic Point: "))
        students[id_number]["amharic_point"] = new_amharic_point
    if command == 13:
        new_afaanoromo_point = float(input("New Afaan Oromo Point: "))
        students[id_number]["afaanoromo_point"] = new_afaanoromo_point
    if command == 14:
        new_civic_point = float(input("New Civic Point: "))
        students[id_number]["civic_point"] = new_civic_point
    if command == 15:
        new_hp_point = float(input("New Hp Point: "))
        students[id_number]["hp_point"] = new_hp_point
    if command == 16:
        new_geography_point = float(input("New Geography Point: "))
        students[id_number]["geography_point"] = new_geography_point
    if command == 17:
        new_history_point = float(input("New History Point: "))
        students[id_number]["history_point"] = new_history_point
    if command == 18:
        new_rank = int(input("New Rank: "))
        students[id_number]["rank"] = new_rank

    set_data(students)
    clean_terminal_screen()
    display_id_information_by_given_id_number(id_number)


#-----------------------------CREATE A NEW STUDENT------------------------------

def create_new_student(full_name, grade, rollnumber, section, gender, physics_point, chemistry_point, biology_point, math_point, english_point,ict_point, amharic_point, afaanoromo_point, civic_point, hp_point, geography_point, history_point, total_average, rank):
    students = get_data()
    date = datetime.today().strftime('%Y-%m-%d')
    id_number = generate_id_number()
    students[id_number] = {
    "full_name": full_name,
    "grade": grade,
    "rollnumber": rollnumber,
    "section": section,
    "gender": gender,
    "physics_point": physics_point,
    "chemistry_point": chemistry_point,
    "biology_point": biology_point,
    "math_point": math_point,
    "english_point": english_point,
    "ict_point": ict_point,
    "amharic_point": amharic_point,
    "afaanoromo_point": afaanoromo_point,
    "civic_point": civic_point,
    "hp_point": hp_point,
    "geography_point": geography_point,
    "history_point": history_point,
    "total_average": total_average,
    "rank": rank
    }
    set_data(students)
    display_id_information_by_given_id_number(id_number)

#-----------------------SEARCH ID ----------------------------------------------

def search_id(field, query):
    students = get_students_as_list()
    students = heap_sort(students, field)
    index = text_binary_search(students, field, query)
    if index == -1:
        print("______________________ERROR______________________")
        print("Found no one as", query)
    else:
        student = students.index(index)
        display_student_object(student, student["id_number"])

#-----------------------DELETE AN ID--------------------------------------------

def delete_id(id_number):
    students = get_data()
    if id_number not in students:
        print("Did not found the Id with number: " + id_number)
        return
    del students[id_number]
    set_data(students)
    print("Id number", id_number, "Removed.")


#------------------------INTERFACE TOOLS----------------------------------------

def clean_terminal_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_horizontal_line():
    print("─────────────────────────────────────────────")


#-----------------------DISPLAY STUDENT OBJECT----------------------------------


def display_id_information_by_given_id_number(id_number):
    students = get_data()
    student = students[id_number]
    display_student_object(student, id_number)


def display_student_object(student_object, id_number):
    print_horizontal_line()
    print("Full Name:              ", student_object["full_name"])
    print("Id Number:              ", id_number)
    print("Roll Number:            ", student_object["rollnumber"])
    print("Grade:                  ", student_object["grade"])
    print("Section:                ", student_object["section"])
    print("Gender:                 ", student_object["gender"])
    if "id_creation_date" in student_object:
        print("Created At:         ", student_object["id_creation_date"])
    print("Marks In Physics        ", student_object["physics_point"])
    print("Marks In Chemistry      ", student_object["chemistry_point"])
    print("Marks In Biology        ", student_object["biology_point"])
    print("Marks In Math           ", student_object["math_point"])
    print("Marks In English        ", student_object["english_point"])
    print("Marks In Ict            ", student_object["ict_point"])
    print("Marks In Amharic        ", student_object["amharic_point"])
    print("Marks In Afaan Oromo    ", student_object["afaanoromo_point"])
    print("Marks In Civic          ", student_object["civic_point"])
    print("Marks In Hp             ", student_object["hp_point"])
    print("Marks In Geography      ", student_object["geography_point"])
    print("Marks In History        ", student_object["history_point"])
    print("Average 100%            ", student_object["total_average"])
    print("Rank                    ", student_object["rank"])


def display_all_id_sorted_by(field):
    students = get_students_as_list()
    students = heap_sort(students, field)
    clean_terminal_screen()
    for i in range(0, students.size()):
        student = students.index(i)
        if "id_number" in student:
            display_student_object(student, student["id_number"])


def beatify_field_name(field):
    if field == "full_name":
        return "Full Name"
    if field == "rollnumber":
        return "Roll Number"
    if field == "grade":
        return "Grade"
    if field == "section":
        return "Section"
    if field == "id_creation_date":
        return "Id Creation Date"
    if field == "gender":
        return "Gender"
    if field == "physics_point":
        return "Physics Point"
    if field == "chemistry_point":
        return "Chemistry Point"
    if field == "biology_point":
        return "Biology Point"
    if field == "math_point":
        return "Math Point"
    if field == "english_point":
        return "English Point"
    if field == "ict_point":
        return "Ict Point"
    if field == "amharic_point":
        return "Amharic Point"
    if field == "afaanoromo_point":
        return "Afaan Oromo Point"
    if field == "civic_point":
        return "Civic Point"
    if field == "hp_point":
        return "Hp Point"
    if field == "geography_point":
        return "Geography Point"
    if field == "history_point":
        return "History Point"
    if field == "total_average":
        return "Average"
    if field == "rank":
        return "Rank"
    return "Unknown"


def ask_student_what_field_to_sort_the_display_by():
    print("Sorting by:")
    print_horizontal_line()
    print("► 1 ∙ Full Name")
    print("► 2 ∙ Id Number")
    print("► 3 ∙ Roll Number")
    print("► 4 ∙ Grade")
    print("► 5 ∙ Section")
    print("► 6 ∙ Gender")
    print("► 7 ∙ Id Creating Date")
    print("► 8 ∙ Rank")
    print()
    command = input("Your option: ")
    if command == "1":
        return "full_name"
    if command == "2":
        return "id_number"
    if command == "3":
        return "rollnumber"
    if command == "4":
        return "grade"
    if command == "5":
        return "section"
    if command == "6":
        return "gender"
    if command == "7":
        return "id_creation_date"
    if command == "8":
        return "rank"
    return "full_name"


#----------------------------DISPLAY MENU---------------------------------------

def display_menu():
    clean_terminal_screen()
    print("┌───────────────────────────┐")
    print("│   STUDENT RESULT MENU     │")
    print("├───────────────────────────┤")
    print("│ ▶︎ 1 • Create Student      │")
    print("│ ▶︎ 2 • Update Student Info │")
    print("│ ▶︎ 3 • Delete Student      │")
    print("│ ▶︎ 4 • Search Student Info │")
    print("│ ▶︎ 5 • View Student's List │")
    print("│ ▶︎ 6 • Exit                │")
    print("└───────────────────────────┘")

while True:
    display_menu()
    student_choice = input("\n ☞ Enter your command: ").strip()
    if not student_choice:
        continue  # ignore empty input and loop again
    try:
        student_choice = int(student_choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # loop again if input cannot be converted to int
    clean_terminal_screen()

    if student_choice == 1:
        print("────────────────────── CREATING A NEW STUDENT──────────────────────")
        students_name = input("Full Name: ")
        students_grade = input("Grade: ")
        students_section = input("Section: ")
        students_gender = input("Gender: ")
        students_rollnumber = int(input("Roll Number: "))
        print("──────────────────────STUDENT POINT OUT OF 100──────────────────────")
        physics_point_ = float(input("Physics: "))
        chemistry_point_ = float(input("Chemistry: "))
        biology_point_ = float(input("Biology: "))
        math_point_ = float(input("Math: "))
        english_point_ = float(input("English: "))
        ict_point_ = float(input("Ict: "))
        amharic_point_ = float(input("Amharic: "))
        afaanoromo_point_ = float(input("Afaan Oromo: "))
        civic_point_ = float(input("Civic: "))
        hp_point_ = float(input("Hp: "))
        geography_point_ = float(input("Geography: "))
        history_point_ = float(input("History: "))
        total_average_ = ((physics_point_ + chemistry_point_ + biology_point_ + math_point_ + english_point_ + ict_point_ + amharic_point_ + afaanoromo_point_ + civic_point_ + hp_point_ + geography_point_ + history_point_) / 12.00 )
        rank_ = int(input("Rank: "))


        create_new_student(students_name, students_grade, students_rollnumber, students_section, students_gender, physics_point_, chemistry_point_, biology_point_, math_point_, english_point_, ict_point_, amharic_point_, afaanoromo_point_, civic_point_, hp_point_, geography_point_, history_point_, total_average_, rank_)

    elif student_choice == 2:
        print("──────────────────────CHANGING STUDENT INFORMATION──────────────────────")
        id_number = input("Id Number To Change: ")
        update_information(id_number)

    elif student_choice == 3:
        print("──────────────────────DELETE AN STUDENT──────────────────────")
        id_number = input("Id Number To Delete: ")
        delete_id(id_number)

    elif student_choice == 4:
        print("──────────────────────SEARCH STUDENT──────────────────────")
        query = input("Searching for: ")
        clean_terminal_screen()
        search_id("full_name", query)

    elif student_choice == 5:
        print("──────────────────────DISPLAYING ALL STUDENTS──────────────────────")
        field = ask_student_what_field_to_sort_the_display_by()
        display_all_id_sorted_by(field)

        print("\n\nSorted by student", beatify_field_name(field))
    elif student_choice == 6:
        quit()

    else:
        print("Invalid input. Please enter a valid command number.")

    print()
    print_horizontal_line()
    input("PRESS ENTER TO CONTINUE ")
    print()




while True:
    display_menu()
