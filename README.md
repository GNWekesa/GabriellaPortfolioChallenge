# GabriellaPortfolioChallenge
Am going to submit my portfolio to showcase my career since highschool

programming languages to use HTML, CSS, and MySQL
my idea is to store my CV details in a database and retrieve them to my website. Now let me use the SDLC
Wednesday 26th March 2025
1. Planning
The challenge is to 
 
Tech Stack: Strictly HTML5 + CSS
My method:
The HTML will be for my web page’s structure
The CSS will add style to it
Database for what? I shall put my cv details into my database
1. Planning
My method:
The HTML will be for my web page’s structure
The CSS will add style to it
Database for what? I shall put my cv details into my database
My database to store my information will consist of several tables:
1.	Personal_Info – Stores your personal details.
2.	Education – Contains your academic background.
3.	Work_Experience – Lists your job history.
4.	Skills – Stores your skills.
5.	Referees – Contains details of your referees.


2. Design
Here are the SQL queries to create the tables and insert my data:
**1. Creating Tables**
CREATE DATABASE Gabriella_CV;
USE Gabriella_CV;

CREATE TABLE Personal_Info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(150),
    objective TEXT
);

CREATE TABLE Education (
    id INT PRIMARY KEY AUTO_INCREMENT,
    institution VARCHAR(100),
    qualification VARCHAR(100),
    year_completed INT,
    grade VARCHAR(20)
);

CREATE TABLE Work_Experience (
    id INT PRIMARY KEY AUTO_INCREMENT,
    job_title VARCHAR(100),
    company VARCHAR(100),
    start_date DATE,
    end_date DATE,
    responsibilities TEXT
);

CREATE TABLE Skills (
    id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(100)
);

**2. Inserting Data**
**Personal Information**
INSERT INTO Personal_Info (name, email, phone, address, objective)
VALUES ('Gabriella Nekesa Wekesa', 'gabriellanekwek@gmail.com', '0115331948', 'P.O. BOX 60680-00200, Nairobi, Kenya', 
        'I seek technical and hands-on opportunities that can develop productive outcomes for the organization I work for. I aim to develop creative methods of ensuring different work activities get performed in feasible ways.');
Education Background
INSERT INTO Education (institution, qualification, year_completed, grade)
VALUES 
    ('St. Paul’s University', 'Diploma in Computer Science', 2020, 'Distinction'),
    ('Eagle Computer College', 'Computer Proficiency', 2019, 'Credit'),
    ('St. Lucie Kiriri Girls Secondary School', 'KCSE', 2014, 'B+');
**Work Experience**
INSERT INTO Work_Experience (job_title, company, start_date, end_date, responsibilities)
VALUES 
    ('Software Engineer', 'Freelance', '2023-07-01', 'CURRENT_DATE', 'Web development using HTML, CSS, JavaScript, Programming in Python, Django, Back-end development using MySQL and PHP'),
    ('Insurance Salesperson', 'Britam', '2023-02-01', '2023-07-01', 'Assessed client needs, promoted and sold life insurance policies, prepared insurance quotes, maintained client records'),
    ('Administrative Assistant', 'Servicehub Global Enterprises Limited', '2022-01-01', '2022-07-01', 'Managed HR operations, handled tenders, stock control, goods deployment, site viewing'),
    ('3D Annotation Specialist', 'Freelance (Remotasks)', '2020-07-01', '2020-12-01', 'Worked with 3D annotation tools and LIDAR platforms, labeled objects with 95%+ accuracy'),
    ('Stock Controller', 'Jolly Logistics', '2016-01-01', '2019-12-01', 'Tracked shipments, managed procurement, maintained inventory reports, ensured accurate stock tracking'),
    ('Assistant Clerk', 'Walker Kontos Advocates', '2014-01-01', '2016-12-01', 'Handled administrative duties, managed files, scheduled tasks for lawyers');
**Skills**
INSERT INTO Skills (skill_name)
VALUES 
    ('Analytical decision making'),
    ('Attention to detail'),
    ('Advanced administration and supervisory skills'),
    ('Microsoft Office Suite proficiency'),
    ('3D and LiDAR annotation'),
    ('Python programming'),
    ('Inventory management'),
    ('Live broadcasting'),
    ('AV equipment setup & operation'),
    ('Troubleshooting & technical support'),
    ('Audio engineering'),
    ('Lighting design & operation');

