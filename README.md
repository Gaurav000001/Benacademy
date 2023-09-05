# Project Title

## Introduction
A brief introduction of your project goes here. You may want to cover the purpose of your project, its core functionality, and what problems it solves.

## Deplolyed App
https://deployed-site.whatever

## Video Walkthrough of the project

## Features
List out the key features of your application.

- Feature 1
- Feature 2
- Feature 3

## design decisions or assumptions
List your design desissions & assumptions

## Installation & Getting started
Detailed instructions on how to install, configure, and get the project running.

```bash
npm install my-project
cd my-project
npm start
```

## Usage
Provide instructions and examples on how to use your project.

```bash
# Example
```

Include screenshots as necessary.

## APIs Used
If your application relies on external APIs, document them and include any necessary links or references.

## API Endpoints
In case of Backend Applications provide a list of your API endpoints, methods, brief descriptions, and examples of request/response.

### Student
GET         students/                                       - retrieve all students
POST        students/register/                              - register new student
GET         students/student_id/                            - get student details
PUT         students/update/student_id/                     - update student details
DELETE      students/delete/student_id/                     - delete student

### Instructor
GET         instructors/                                    - retrieve all instructors
POST        instructors/register/                           - register new instructor
GET         instructors/instructor_id/                      - get instructor details
PUT         instructors/update/instructor_id/               - update instructor details
DELETE      instructors/delete/instructor_id/               - delete instructor

### Department
GET         departments/                                    - retrieve all departments
POST        departments/create/                             - create new department
GET         departments/department_id/                      - get department details
PUT         departments/update/department_id/               - update department details
DELETE      departments/delete/department_id/               - delete department

### Course
GET         courses/                                        - retrieve all courses
POST        courses/create/department_id/                   - create new course in department
GET         courses/student_id/                             - get student courses
PUT         courses/update/course_id/instructor_id/         - change course's instructor
DELETE      courses/delete/course_id/                       - delete course

### Enrollment
POST        enrollments/enroll/student_id/course_id/        - enroll student to course
POST        enrollments/enroll/course_id/                   - enroll students to course

### Assignment
POST        assignments/create/course_id/                   - create new assignment in course
GET         assignments/student_id/                         - get student assignments
DELETE      assignments/delete/assignment_id/               - delete assignment

### Submission
POST        submissions/assignment_id/student_id/           - submit assignment for student



## Technology Stack
List and provide a brief overview of the technologies used in the project.

- Python
- Django
- MySQL
- Angular

## ER Diagram

<img src="https://github.com/Gaurav000001/EdTech-Nexus/blob/main/ER%20Diagram.png" width=100%/>
