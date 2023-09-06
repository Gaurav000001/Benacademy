# Project Title

## Introduction
A brief introduction of your project goes here. You may want to cover the purpose of your project, its core functionality, and what problems it solves.

## Technology Stack

- Python
- Django
- MySQL
- Angular

## Video Walkthrough of the project

## Features
List out the key features of your application.

- Student CRUD
- Instructor CRUD
- Department wise course creation
- Enroll Student to course
- Change Course's Instructor
- Create Assignment in specific Course
- Submit Assignment via Student

## Installation & Getting started
Detailed instructions on how to install, configure, and get the project running.

```bash
npm install my-project
cd my-project
npm start
```


## API Endpoints

### Student

#### Retrieve All Students
- **Endpoint**: GET /students/
- **Description**: Retrieve a list of all students.
- **Scope**: Admin

#### Register New Student
- **Endpoint**: POST /students/register/
- **Description**: Register a new student.
- **Scope**: Admin, User

#### Get Student Details
- **Endpoint**: GET /students/{student_id}/
- **Description**: Get details of a specific student by providing their unique student ID.
- **Scope**: Admin, User

#### Update Student Details
- **Endpoint**: PUT /students/update/{student_id}/
- **Description**: Update details of a specific student by providing their unique student ID.
- **Scope**: User

#### Delete Student
- **Endpoint**: DELETE /students/delete/{student_id}/
- **Description**: Delete a specific student by providing their unique student ID.
- **Scope**: Admin, User

### Instructor

#### Retrieve All Instructors
- **Endpoint**: GET /instructors/
- **Description**: Retrieve a list of all instructors.
- **Scope**: Admin

#### Register New Instructor
- **Endpoint**: POST /instructors/register/
- **Description**: Register a new instructor.
- **Scope**: Admin, User

#### Get Instructor Details
- **Endpoint**: GET /instructors/{instructor_id}/
- **Description**: Get details of a specific instructor by providing their unique instructor ID.
- **Scope**: Admin, User

#### Update Instructor Details
- **Endpoint**: PUT /instructors/update/{instructor_id}/
- **Description**: Update details of a specific instructor by providing their unique instructor ID.
- **Scope**: User

#### Delete Instructor
- **Endpoint**: DELETE /instructors/delete/{instructor_id}/
- **Description**: Delete a specific instructor by providing their unique instructor ID.
- **Scope**: Admin, User

### Department

#### Retrieve All Departments
- **Endpoint**: GET /departments/
- **Description**: Retrieve a list of all base departments.
- **Scope**: Admin

#### Create New Department
- **Endpoint**: POST /departments/create/
- **Description**: Create a new department.
- **Scope**: Admin

#### Get Department Details
- **Endpoint**: GET /departments/{department_id}/
- **Description**: Get details of a specific department by providing its unique department ID.
- **Scope**: Admin

#### Update Department Name
- **Endpoint**: PUT /departments/update/{department_id}/
- **Description**: Update name of a specific department by providing its unique department ID.
- **Scope**: Admin

#### Delete Department
- **Endpoint**: DELETE /departments/delete/{department_id}/
- **Description**: Delete a specific department by providing its unique department ID.
- **Scope**: Admin

### Course

#### Retrieve All Courses
- **Endpoint**: GET /courses/
- **Description**: Retrieve a list of all courses.
- **Scope**: Admin

#### Create New Course in Department
- **Endpoint**: POST /courses/create/{department_id}/
- **Description**: Create a new course in a specific department by providing its unique department ID.
- **Scope**: Admin

#### Get Student's Courses
- **Endpoint**: GET /courses/{student_id}/
- **Description**: Get the list of courses for a specific student by providing their unique student ID.
- **Scope**: Admin, User

#### Change Course's Instructor
- **Endpoint**: PUT /courses/update/{course_id}/{instructor_id}/
- **Description**: Change the instructor of a specific course by providing its unique course ID and the new instructor's ID.
- **Scope**: Admin

#### Delete Course
- **Endpoint**: DELETE /courses/delete/{course_id}/
- **Description**: Delete a specific course by providing its unique course ID.
- **Scope**: Admin

### Enrollment

#### Enroll Student to Course
- **Endpoint**: POST /enrollments/enroll/{student_id}/{course_id}/
- **Description**: Enroll a student to a specific course by providing their unique student ID and the course ID.
- **Scope**: Admin

#### Enroll Students to Course
- **Endpoint**: POST /enrollments/enroll/{course_id}/
- **Description**: Enroll multiple students to a specific course by providing the course ID.
- **Scope**: Admin

### Assignment

#### Create New Assignment in Course
- **Endpoint**: POST /assignments/create/{course_id}/
- **Description**: Create a new assignment in a specific course by providing its unique course ID.
- **Scope**: Admin

#### Get Student's Assignments
- **Endpoint**: GET /assignments/{student_id}/
- **Description**: Get the assignments for a specific student by providing their unique student ID.
- **Scope**: Admin, User

#### Delete Assignment
- **Endpoint**: DELETE /assignments/delete/{assignment_id}/
- **Description**: Delete a specific assignment by providing its unique assignment ID.
- **Scope**: Admin

### Submission

#### Submit Assignment for Student
- **Endpoint**: POST /submissions/{assignment_id}/{student_id}/
- **Description**: Submit an assignment for a specific student by providing the assignment ID and student ID.
- **Scope**: User















<!-- 
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
POST        submissions/assignment_id/student_id/           - submit assignment for student -->



## ER Diagram

<img src="https://github.com/Gaurav000001/EdTech-Nexus/blob/main/ER%20Diagram.png" width=100%/>
