# Class Demand Predictor
**Westmont College Fall 2024**

**CS 128 Information Retrieval and Big Data**

*Assistant Professor* Mike Ryu (mryu@westmont.edu) 

## Author Information 
* **Name**: Silas Ten Elshof
* **Email**: stenelshof@westmont.edu

## License Information
 MIT 

## Project Description:
This project is to create a tool for professors in a particular department to estimate how many elective classes they should offer in a given semester (specifically for Biola’s philosophy department, but applicable to others). The goal is to offer as many different class options as possible, while still meeting a certain minimum requirement for the number of students in each class. This program will take in data about every student who is pursuing a major in a particular department, specifically how many semesters they have before they graduate and how many elective credits they still need to take. The logic behind the program will assume that each student will spread out their needed classes evenly throughout their remaining semesters. Therefore, it will predict the demand for classes in this department for a given semester by dividing the number of credits needed by the number of of credits per class (to find the number of classes needed) and then divide that number by the number of semesters remaining (to make a prediction for how many classes they will take per semester), for each student who is majoring in this department. It will also take into account a prediction for the demand that the incoming freshman class will have for classes in this department. The program will be provided to the client in a format that is easy to understand and use, requiring little coding ability. 
