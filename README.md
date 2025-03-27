# GabriellaPortfolioChallenge
Am going to submit my portfolio to showcase my career since highschool

programming languages to use HTML, CSS, and MySQL
my idea is to store my CV details in a database and retrieve them to my website. Now let me use the SDLC
Wednesday 26th March 2025
1. Planning 
Tech Stack: Strictly HTML5 + CSS
My method:
The HTML will be for my web page’s structure
The CSS will add style to it
Database for what? I shall put my cv details into my database as a BLOB
My database to store my information will consist of several tables:
1.	Personal_Info – Stores your personal details.
2.	Education – Contains your academic background.
3.	Work_Experience – Lists your job history.
4.	Skills – Stores your skills.
5.	Referees – Contains details of your referees.

My project folder consists of:
GabriellaNWekesaPortfolio/
│── cv_files/                   this contains my original CV file
│── database/                   this stored my SQLite database file
│── downloads/                  this is to store my downloaded CVs
│── style.cs                      
│── images                      this is to store images used in the projec
│── index.html
│── educational_background.html
│── upload_cv.py                this contains Python scripts for backend 
│── download_cv.py              this contains Python scripts for backend 
│── README.md                 		this is for my documentation optional

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

i then decided to 
