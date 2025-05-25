create database sms;
use sms;
#------------------------------------------------------------------------------------------
Create table Departments( department_id int primary key,
department_name varchar(50) not null);
insert into departments values(1001, 'mechanical'),(1002,'ECE'),(1003,'CSE'),(1004,'CIVIL');
#--------------------------------------------------------------------------------------
create table Students(student_id int unique not null , sname varchar(50) not null, 
email varchar(50) unique not null, 
dob date not null,
department_id int not null, 
foreign key (department_id) references departments(department_id));
insert into students values (104, 'fadhil', 'Fadhil@gmail.com','2003-09-03', 1004);
select * from students;
#---------------------------------------------------------------------------
create table Courses(course_id int not null, 
course_name varchar(50) not null, 
department_id int not null , 
credits int,
foreign key (department_id) references departments(department_id));

insert into courses values( 2005, 'Data Analytics', 1003, 8);

select * from courses; 
#---------------------------------------------------------------------------------------------

create table Enrollments( enrollment_id int not null unique ,
student_id int not null,
course_id int not null,
semester int not null, 
grade varchar(5) not null,
foreign key(student_id) references students(student_id));
insert into enrollments values 
(3001, 102, 2004, 1, 'A'),
(3002, 103, 2001, 2, 'B+'),
(3003, 101, 2002, 2, 'B'),
(3004, 104, 2003, 2, 'A');

select * from enrollments;


#---------------------------------------------------------------------------------------

# Q2. Write a query to list all students.

select * from students;

#----------------------------------------
# Q3. Write a query to find students born after the year 2002.

select * from students
where year(dob)>2002;

#-------------------------------------------------

# Q4. List students with their department names.
select s.student_id, s.sname, s.email, s.department_id, d.department_name from students s
join departments d on s.department_id = d.department_id;


#--------------------------------------------------------------------------------------
#Q5. Show each student’s name, course name, and grade for the current semester.

select s.student_id, s.sname , c.course_name, e.grade
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
WHERE e.semester = 2; 

#------------------------------------------------------------------------
# Q6. Display each department with the number of students enrolled.;

select d.department_name, count(s.student_id) from departments d
join students s on d.department_id = s.department_id
group by d.department_name;

#-----------------------------------------------------------------------
#Part 4: Subqueries
#Q7. Find students who are enrolled in the course 'Data Structures';.

select student_id, sname, email from students
where student_id in ( select student_id from enrollments
					  WHERE course_id = ( select course_id from courses
										  where course_name = 'Data Structures'));
#-------------------------------------------------------------------------------------------
#Q8. Find students with the highest grade in each course.
select * from enrollments;

select s.student_id, s.sname, e.course_id, e.grade from students s
join enrollments e on s.student_id = e.student_id
where e.grade = (select max(grade) from enrollments);

#--------------------------------------------------------------------------
#Q9. List students who are enrolled in more than 3 courses.
select student_id, sname from students
where student_id in (select student_id from enrollments
					 group by student_id
					 having count(course_id) > 3);
#---------------------------------------------------------------------------------
#Q10. Show courses that are not taken by any student.
select course_id, course_name from courses
where course_id not in (select course_id from enrollments);
