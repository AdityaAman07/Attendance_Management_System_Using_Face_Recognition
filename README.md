## Attendance Management System Using Face Recognition 💻

This project involves building an attendance system which utilizes facial recognition to mark the presence, time-in, and time-out of employees. It covers areas such as facial detection, alignment, and recognition, along with the development of a web application to cater to various use cases of the system such as registration of new employees, addition of photos to the training dataset, viewing attendance reports, etc. This project intends to serve as an efficient substitute for traditional manual attendance systems. It can be used in corporate offices, schools, and organizations where security is essential.

This project aims to automate the traditional attendance system where the attendance is marked manually. It also enables an organization to maintain its records like in-time, out time, break time and attendance digitally. Digitalization of the system would also help in better visualization of the data using graphs to display the no. of employees present today, total work hours of each employee and their break time. Its added features serve as an efficient upgrade and replacement over the traditional attendance system.

## Scope of the project 🚀
Facial recognition is becoming more prominent in our society. It has made major progress in the field of security. It is a very effective tool that can help low enforcers to recognize criminals and software companies are leveraging the technology to help users access the technology. This technology can be further developed to be used in other avenues such as ATMs, accessing confidential files, or other sensitive materials.
This project servers as a foundation for future projects based on facial detection and recognition. This project also convers web development and database management with a user-friendly UI. Using this system any corporate offices, school and organization can replace their traditional way of maintaining attendance of the employees and can also generate their availability(presence) report throughout the month.

**The system mainly works around 2 types of users**
1. Employee
2. Admin

**Following functionalities can be performed by the admin: <br>**
• Login <br>
• Register new employees to the system <br>
• Add employee photos to the training data set <br>
• Train the model <br>
• View attendance report of all employees. Attendance can be filtered by date or employee. <br>

**Following functionalities can be performed by the employee: <br>**
• Login <br>
• Mark his/her time-in and time-out by scanning their face <br>
• View attendance report of self <br>

## Face Detection
Dlib's HOG facial detector.

## Facial Landmark Detection
Dlib's 68 point shape predictor

## Extraction of Facial Embeddings
face_recognition by Adam Geitgey

## Classification of Unknown Embedding 
using a Linear SVM (scikit-learn)

## How to Run ?
- Clone this code with your Computer.
- Create a separate Virtual environment or use the deafault one already installed in your computer.
- Clone requirements.txt file with your computer.
- Set specific file path according to your system path.
- Type python manage.py makemigration
- Again type python manage.py migrate
- Let's run the project using command python manage.py runserver



## Thank you
- Author: Aditya Aman