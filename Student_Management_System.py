
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

conn = mysql.connector.connect(
    host = "localhost",
    user = input("Enter your user database username"),
    password =  input("Enter MySQL Password: "),
    database = input("Enter your database Name: ")
)
cursor = conn.cursor()
print("Connected Successfully!")


root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")



def save_records():

    cursor.execute(
        """
        INSERT INTO students
        (student_id, full_name, dob, gender, class, course, phone, email)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            Id.get(),
            Name.get(),
            DoB.get(),
            gender.get(),
            Class.get(),
            Course.get(),
            phone.get(),
            email.get()
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student saved successfully!"
    )
    
    load_students()

def clear_fields():

    Id.delete(0, END)
    Name.delete(0, END)
    DoB.delete(0, END)

    gender.set("Select Gender")

    Class.delete(0, END)
    Course.delete(0, END)
    phone.delete(0, END)
    email.delete(0, END)

def delete_records():
    student_id = Id.get()
    cursor.execute(
        "DELETE FROM students WHERE student_id = %s",(student_id,)
    )
    conn.commit()
    
    messagebox.showinfo("Success", "Student deleted successfully!")

    clear_fields()
    load_students()

def update_student():

    cursor.execute(
        """
        UPDATE students
        SET
            full_name=%s,
            dob=%s,
            gender=%s,
            class=%s,
            course=%s,
            phone=%s,
            email=%s
        WHERE student_id=%s
        """,
        (
            Name.get(),
            DoB.get(),
            gender.get(),
            Class.get(),
            Course.get(),
            phone.get(),
            email.get(),
            Id.get()
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student updated successfully!"
    )
    load_students()

def search_student():

    name = bar.get()

    cursor.execute("""
        SELECT
        student_id,
        full_name,
        dob,
        gender,
        class,
        course,
        phone,
        email
        FROM students
        WHERE student_id=%s OR full_name=%s
    """, (name,name,))

    student = cursor.fetchone()

    if student:

        result_id.config(text=f"ID: {student[0]}")
        result_name.config(text=student[1])
        result_dob.config(text=f"DOB: {student[2]}")
        result_gender.config(text=f"Gender: {student[3]}")
        result_class.config(text=f"Class: {student[4]}")
        result_course.config(text=f"Course: {student[5]}")
        result_phone.config(text=f"Phone: {student[6]}")
        result_email.config(text=f"Email: {student[7]}")

        result_frame.grid(
            row=3,
            column=0,
            columnspan=4,
            padx=15,
            pady=15,
            sticky="ew"
            
        )
        bar.delete(0, END)

    else:
        result_frame.grid_remove()

        messagebox.showerror(
            "Not Found",
            "Student does not exist in records."
        )
    
        
def close():
    result_frame.grid_forget()
    bar.grid(column=0, row=1, rowspan=2, padx=30, pady=10, ipady=10, sticky="w")
    S_btn.grid(row=1, column=3)
    
def load_students():

    # Clear old rows
    table.delete(*table.get_children())

    # Get all students
    cursor.execute("""
        SELECT
        student_id,
        full_name,
        dob,
        gender,
        class,
        course,
        phone,
        email
        FROM students
    """)

    rows = cursor.fetchall()

    # Insert into table
    for row in rows:

        table.insert(
            "",
            END,
            values=row
        )
    
    
root.title("Student Management System")

# Top Frame
Up_heading = Frame(root, bg="#ffffff", height=100)
Up_heading.pack(side="top", fill="x",)
Up_heading.pack_propagate(False)

# logo_img = Image.open("logo.png")
# logo_img = logo_img.resize((150, 100))  # width, height
# logo = ImageTk.PhotoImage(logo_img)


# logo_label = Label(Up_heading, image=logo, bg="#ffffff")
# logo_label.pack(side="left")

Heading = Label(
    Up_heading,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial Black", 22, "bold"),
    bg="#ffffff"
)
Heading.pack(pady=7, anchor="sw")

H2 = Label(Up_heading, text="Manage Student Records Efficiently", font=("Segoe UI", 12, "normal"), bg="#ffffff", fg="#4F4F50")
H2.pack(anchor="sw")

# Main Container
main = Frame(root, bg="#F3F3F3")
main.pack(fill="both", expand=True)

# Top Section
top_section = Frame(main, bg="#F3F3F3")
top_section.pack(fill="x", pady=10)

# Left Frame
info = Frame(top_section, bg="#FFFFFF", width=950, height=440)
info.pack(side="left", padx=10)
info.grid_propagate(False)

# icon = Label(info, image=Student_icon, bg="#FFFFFF")
# icon.grid(row=0, column=0, padx=10, pady=10, sticky="w")

heading = Label(
    info,
    text="STUDENT INFORMATION",
    font=("Segoe UI", 14, "bold"),
    fg="#1e6af8",
    bg="#FFFFFF"
)
heading.grid(row=0, column=0, columnspan=2, sticky="w", padx=50, pady=15)

# Student ID
l1 = Label(info, text="Student ID", bg="#FFFFFF")
l1.grid(row=1, column=0, sticky="w", padx=15)

Id = Entry(info, width=50, bg="#F5F7FA")
Id.grid(row=2, column=0, padx=15, pady=5, ipady=6, ipadx=40)

# Class
l5 = Label(info, text="Class", bg="#FFFFFF")
l5.grid(row=1, column=1, sticky="w", padx=15)

Class = Entry(info, width=50, bg="#F5F7FA")
Class.grid(row=2, column=1, padx=15, pady=5, ipady=6, ipadx=40)

# Full Name
l2 = Label(info, text="Full Name", bg="#FFFFFF")
l2.grid(row=3, column=0, sticky="w", padx=15)

Name = Entry(info, width=50, bg="#F5F7FA")
Name.grid(row=4, column=0, padx=15, pady=5, ipady=6, ipadx=40)

# Course
l6 = Label(info, text="Course", bg="#FFFFFF")
l6.grid(row=3, column=1, sticky="w", padx=15)

Course = Entry(info, width=50, bg="#F5F7FA")
Course.grid(row=4, column=1, padx=15, pady=5, ipady=6, ipadx=40)

# DOB
l3 = Label(info, text="Date of Birth", bg="#FFFFFF")
l3.grid(row=5, column=0, sticky="w", padx=15)

DoB = Entry(info, width=50, bg="#F5F7FA")
DoB.grid(row=6, column=0, padx=15, pady=5, ipady=6, ipadx=40)

# Phone
l7 = Label(info, text="Phone No", bg="#FFFFFF")
l7.grid(row=5, column=1, sticky="w", padx=15)

phone = Entry(info, width=50, bg="#F5F7FA")
phone.grid(row=6, column=1, padx=15, pady=5, ipady=6, ipadx=40)

# Email
l8 = Label(info, text="Email", bg="#FFFFFF")
l8.grid(row=7, column=1, sticky="w", padx=15)

email = Entry(info, width=50, bg="#F5F7FA")
email.grid(row=8, column=1, padx=15, pady=5, ipady=6, ipadx=40)

# Gender
l4 = Label(info, text="Gender", bg="#FFFFFF")
l4.grid(row=7, column=0, sticky="w", padx=15)

gender = ttk.Combobox(
    info,
    values=["Male", "Female", "Other"],
    state="readonly",
    width=50
)
gender.set("Select Gender")
gender.grid(row=8, column=0, padx=15, pady=5, ipady=6, ipadx=30)

# Buttons
button_frame = Frame(info, bg="#FFFFFF")
button_frame.grid(row=25, column=0, columnspan=2, pady=65, ipady=10, ipadx=30, padx=20)

save = Button(button_frame, text="SAVE", font=("Segoe UI", 13, "bold"),  bg="green", fg="white", width=12, height=1, command=save_records)
save.grid(row=1, column=0, padx=25)

update = Button(button_frame, text="UPDATE", font=("Segoe UI", 13, "bold"), bg="blue", fg="white", width=12, height=1, command=update_student)
update.grid(row=1, column=1, padx=25)

delete = Button(button_frame, text="DELETE",font=("Segoe UI", 13, "bold"), bg="red", fg="white", width=12, height=1, command=delete_records)
delete.grid(row=1, column=2, padx=25)

clear = Button(button_frame, text="CLEAR",font=("Segoe UI", 13, "bold"), bg="gray", fg="white", width=12, height=1, command=clear_fields)
clear.grid(row=1, column=3, padx=25)


# Right Frame
Search = Frame(top_section, bg="#FFFFFF", width=950, height=440)
Search.pack(side="right", padx=20)
Search.grid_propagate(False)

# image_lable = Label(Search, image=search_icon, bg="#FFFFFF")
# image_lable.grid(row=0, column=0, sticky="w", padx=10)

heading2 = Label(Search, text="SEARCH STUDENT", font=("Segoe UI", 14, "bold"), fg="#1e6af8", bg="#FFFFFF")
heading2.grid(row=0, column=0, columnspan=2, sticky="w", padx=35, pady=15)


bar = Entry(Search, width=110, bg="#F5F7FA")
bar.grid(column=0, row=1, rowspan=2, padx=30, pady=10, ipady=10, sticky="w")


S_btn = Button(Search, text="Search" , font=("Segoe UI", 14, "bold") ,width=12, bg="#1e6af8", fg="white", command=search_student)
S_btn.grid(row=1, column=3)

result_frame = Frame(
    Search,
    bg="#F8FAFC",
    bd=1,
    relief="solid"
)

result_name = Label(
    result_frame,
    font=("Segoe UI", 18, "bold"),
    bg="#F8FAFC"
)

result_id = Label(result_frame, bg="#F8FAFC")
result_dob = Label(result_frame, bg="#F8FAFC")
result_gender = Label(result_frame, bg="#F8FAFC")
result_class = Label(result_frame, bg="#F8FAFC")
result_course = Label(result_frame, bg="#F8FAFC")
result_phone = Label(result_frame, bg="#F8FAFC")
result_email = Label(result_frame, bg="#F8FAFC")
result_name.grid(row=0, column=0, columnspan=2, pady=15)

result_id.grid(row=1, column=0, sticky="w", padx=20, pady=5)
result_gender.grid(row=1, column=1, sticky="w", padx=20, pady=5)

result_dob.grid(row=2, column=0, sticky="w", padx=20, pady=5)
result_class.grid(row=2, column=1, sticky="w", padx=20, pady=5)

result_course.grid(row=3, column=0, sticky="w", padx=20, pady=5)
result_phone.grid(row=3, column=1, sticky="w", padx=20, pady=5)

result_email.grid(row=4, column=0, columnspan=2, sticky="w", padx=20, pady=5)


# Student list
student_list = Frame(main, bg="#E9E8E8", height=400)
student_list.pack(fill="x", padx=10, pady=10)
student_list.pack_propagate(False) 

student_list.grid_rowconfigure(1, weight=1)
student_list.grid_columnconfigure(0, weight=1)

# List_icon = Label(student_list, image=list_icon)
# List_icon.grid(row=0, column=0, sticky="w", padx=10)

heading3 = Label(student_list, text="STUDENT LIST", font=("Segeo UI", 14, "bold"), fg="#1e6af8", bg="#E9E8E8") 
heading3.grid(row=0, column=0, padx= 40, pady=10, sticky='w')

# Table
table = ttk.Treeview(
    student_list,
    columns=("ID", "Name", "DOB", "Gender", "Class", "Course", "Phone", "Email"),
    show="headings",
    height=12
)

# Headings
table.heading("ID", text="ID")
table.heading("Name", text="Full Name")
table.heading("DOB", text="Date of Birth")
table.heading("Gender", text="Gender")
table.heading("Class", text="Class")
table.heading("Course", text="Course")
table.heading("Phone", text="Phone")
table.heading("Email", text="Email")

# Column Widths
table.column("ID", width=30, anchor=CENTER)
table.column("Name", width=180, anchor=CENTER)
table.column("DOB", width=120, anchor=CENTER)
table.column("Gender", width=100, anchor=CENTER)
table.column("Class", width=30, anchor=CENTER)
table.column("Course", width=150, anchor=CENTER)
table.column("Phone", width=100, anchor=CENTER)
table.column("Email", width=200, anchor=CENTER)


# Table Position
table.grid(row=1,column=0,padx=15,pady=10,sticky="nsew",  ipadx=20)

style = ttk.Style()

style.theme_use("clam")

# Header Style
style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 11, "bold"),
    background="#1e6af8",
    foreground="white",
    relief="flat"
)

# Table Style
style.configure(
    "Treeview",
    font=("Segoe UI", 10),
    rowheight=25,
    background="white",
    fieldbackground="white",
    foreground="black",
    borderwidth=0
)

style.map(
    "Treeview",
    background=[("selected", "#d6e6ff")],
    foreground=[("selected", "black")]
)

scroll_y = Scrollbar(student_list, orient=VERTICAL)

scroll_y.grid(
    row=1,
    column=1,
    sticky="ns",
    pady=10
)

table.configure(yscrollcommand=scroll_y.set)
scroll_y.config(command=table.yview)


load_students()
root.mainloop()
