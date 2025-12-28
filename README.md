# 📊 CSV Export using Django Admin Actions – Task 5

This project is developed as **Task-5** of my internship assignment.  
It demonstrates how to **export saved database records into a CSV file** using a **custom Django Admin Action**, accessible only to the **superadmin**.

---

## 🎯 Task Requirement

> **Create a function in `views.py` which can export the saved data in `.csv` format and that trigger button should be on superadmin of Django along with Actions.**

---

## 🧠 What This Task Does

- Uses **Django Admin Actions**
- Adds a custom **“Export to CSV”** option
- Allows **superadmin** to:
  - Select records
  - Download them as a `.csv` file
- Restricts export access to **superuser only**

---

## 🛠️ Tech Stack

- 🐍 Python 3.x  
- 🌐 Django 4.x  
- 🗄️ SQLite3  
- 📄 CSV (Python `csv` module)

---

## 📁 Project Structure

Task-5-CSV-Export/
│
├── csv_export_project/
│ ├── settings.py
│ ├── urls.py
│
├── records/
│ ├── models.py # Student model
│ ├── views.py # CSV export function
│ ├── admin.py # Admin action registration
│
├── manage.py
├── README.md
└── requirements.txt


---

## 📦 Model Used

### 📄 `models.py`

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
