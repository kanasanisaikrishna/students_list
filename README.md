﻿# students_list

Students List API
This Django API project provides endpoints for managing a list of students. It includes functionality for adding new students, updating existing student records, and retrieving student details by their IDs.

#Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd students_list

Create and activate a virtual environment (optional but recommended):

#Install dependencies:

pip install -r requirements.txt
Usage
To run the development server, execute the following command:

#Database integration :
create a new database 'New_database'
update the database name in the project setting.py file with username and password of your local database

Run the bellow commands for the creation of the required tables

bash
py manage.py makemigrations
py manage.py migrate

bash
python manage.py runserver
Endpoints
Add a New Student
URL: /api/addstudent

Method: POST

Description: Add a new student to the database.

Update and retrive a Student details by ID
URL: /api/<student_id>/

Method: PUT

Description: Retriving Update an existing student's details.

List of all student details

URL: /api/

Method: GET

Description: Retrieve details of a student by their ID.

#Contributing
Contributions to this project are welcome. Please follow the guidelines in CONTRIBUTING.md.
