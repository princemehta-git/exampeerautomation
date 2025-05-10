# Exampeer Quiz Automation 📚🤖

This Python-based automation script is built for **Exampeer** to streamline and automate daily business tasks, specifically the generation of **daily** and **weekly quizzes**. It reduces manual effort by dynamically updating quiz files based on predefined templates or data sources.

---

## 🧰 Features

- 🗓️ Automates creation of **daily quizzes** with `daily_test_update.py`  
- 📅 Automates generation of **weekly quizzes** using `weekly_test_update.py`  
- 📁 Structured Excel file updates in `excels_weekly/`  
- ⏱️ Saves time and reduces manual input errors  
- 🧪 Includes a `rough.py` script for testing/debugging

---

## 📁 Project Structure

exampeer-automation/  
│  
├── daily_test_update.py       # Automates daily test creation  
├── weekly_test_update.py      # Automates weekly test creation  
├── rough.py                   # Sandbox script for debugging  
├── excels_weekly/             # Directory for generated or input Excel files  
└── README.md                  # Project documentation (this file)

---

## 🛠️ Requirements

- Python 3.6+  
- pandas  
- openpyxl  
- xlrd  

Install dependencies with:

pip install pandas openpyxl xlrd

---

## 🖥️ How to Use

1. Place your quiz template or input data in the appropriate directory.
2. Run the daily or weekly script depending on your need:

Daily quiz generation:

python daily_test_update.py

Weekly quiz generation:

python weekly_test_update.py

3. Output Excel files will be saved in the `excels_weekly/` folder or as defined in the script.

---

## 🧪 Sample Use Case

- The content team uploads raw questions or template files.
- This script formats and populates new quiz files for the website/app.
- Reduces daily operational overhead by automating repetitive quiz publishing.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by @princemehta-git  
https://github.com/princemehta-git
