# Student Management System (Django + MongoDB)

A simple **Student Management System** built with **Django** and **MongoDB** to store and manage student information such as **name**, **email**, and **roll number**.

---

## Features

- Add new students
- View list of students
- Update student details
- Delete student records
- Uses MongoDB as the database

---

## Tech Stack

- **Backend:** Django 5.x
- **Database:** MongoDB
- **Python:** 3.12+
- **Front-end:** Django Templates (HTML, CSS)

---

## Installation

1. **Clone the repository**

```bash
git clone <repository_url>
cd student-management
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install django djangorestframework pymongo djongo
```

4. **Configure MongoDB**

* Install MongoDB locally or use MongoDB Atlas.
* Update your `settings.py` with the MongoDB connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'student_db',
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
        }
    }
}
```

5. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the server**

```bash
python manage.py runserver
```

---

## Project Structure

```
student-management/
├── manage.py
├── student_app/
│   ├── models.py       # Student model (name, email, roll number)
│   ├── views.py        # Views for CRUD operations
│   ├── urls.py         # URL routing
│   ├── templates/      # HTML templates
│   └── admin.py        # Register models in admin
├── student_management/
│   ├── settings.py     # Project settings
│   └── urls.py         # Main URL routing
└── README.md
```

---

## Student Model Example

```python
from djongo import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
```

---

## CRUD Operations

* **Create:** Add new student records via a form.
* **Read:** View all students in a table.
* **Update:** Edit student details.
* **Delete:** Remove student records from the database.

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m "Description"`)
5. Push to the branch (`git push origin feature-name`)
6. Open a Pull Request

---

## License

This project is licensed under the MIT License.

```
Be sure, this README only gives brief idea about project

If you want, I can also **add instructions for creating simple HTML forms for Add/Edit/Delete students** so the project is fully ready for use.  
Do you want me to add that?
```
