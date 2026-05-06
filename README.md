# 🎉 Automated Birthday Wisher

A Python automation project that sends birthday wishes automatically via email using SMTP.

The program reads birthday data from a CSV file, checks the current date, and sends customized birthday emails with text messages, images, and GIF attachments.

---

# 🚀 Features

- Read birthday records from CSV file
- Automatically checks today's birthdays
- Sends personalized emails
- Supports:
  - Text messages
  - Images
  - GIF attachments
- Uses Gmail SMTP server
- MIME multipart email support

---

# 🛠 Technologies Used

- Python
- SMTP
- CSV Module
- Datetime Module
- MIME (email attachments)

---

# 📂 Project Structure

```bash
DAY-32/
│
├── DOB.csv
├── hbd.txt
├── chat.png
├── batman.gif
├── panda.gif
├── HBD.gif
└── main.py
```

---

# 📄 CSV Format

```csv
name,email,year,month,day
John,john@gmail.com,2001,5,6
Alex,alex@gmail.com,2000,8,12
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <[(https://github.com/subhramannil/AUTOMATED-BIRTHDAY-WISHER)]>
```

---

## 2️⃣ Install Python

Make sure Python 3.x is installed.

---

## 3️⃣ Enable Gmail App Password

Generate an App Password from your Google Account.

---

## 4️⃣ Add Credentials

```python
my_email = "your_email@gmail.com"
password = "your_app_password"
```

---

## 5️⃣ Run Program

```bash
python main.py
```

---

# 🔒 Security Note

Do NOT upload your real Gmail password or App Password to GitHub.

Use environment variables instead.

---

# 📧 Example Workflow

1. Read birthday data from CSV
2. Check today's date
3. Generate email body
4. Attach images/GIFs
5. Send birthday email automatically

---

# 🎯 Learning Outcomes

This project helped practice:

- File handling
- CSV processing
- Email automation
- SMTP protocol
- MIME attachments
- Python automation scripting

---

# 📌 Future Improvements

- HTML email templates
- Scheduled execution
- Random birthday quotes
- GUI version
- Database integration

---

# 👨‍💻 Author

Subhranil Das
