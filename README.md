# Student Management System

A desktop-based Student Management System developed using **Python, Tkinter, and MySQL**.  
This application provides an easy-to-use graphical interface for managing student records efficiently.

The system allows users to add, update, delete, and search student information while storing data securely in a MySQL database.

## Features

- Add new student records
- Update existing student information
- Delete student records
- Search students by different fields
- Display student data in a table format
- MySQL database integration
- User-friendly Tkinter graphical interface

## Technologies Used

- Python
- Tkinter (GUI Framework)
- MySQL Database
- MySQL Connector Python

## Project Structure
Student-Management-System
│
├── Student_Management_System.py
├── database.py
└── README.md

## Requirements

Before running this project, install:

- Python 3.x
- MySQL Server

Install required Python libraries:


## Database Setup

Follow these steps to configure the MySQL database:

### 1. Open MySQL

Open MySQL Workbench or MySQL Command Line.

### 2. Create Database

Create a database with the name:

```sql
CREATE DATABASE student_management;
USE student_management;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    gender VARCHAR(20),
    class VARCHAR(50),
    course VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);

#Replace names with your Database
host = "localhost"
user = "your_mysql_username"
password = "your_mysql_password"
database = "student_management"
