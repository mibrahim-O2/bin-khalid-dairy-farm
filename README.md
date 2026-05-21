<div align="center">

<img src="https://raw.githubusercontent.com/mibrahim-O2/bin-khalid-dairy-farm/main/static/bufalo.png"
     alt="Bin Khalid Dairy Farm Logo" width="180" />

# Bin Khalid Dairy Farm
### Management System

*"Bin Khalid" Son of Khalid. Built for my father, built for our farm.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live%20%26%20In%20Use-22c55e?style=for-the-badge)](https://mibrahim02.pythonanywhere.com/)

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-Visit%20Now-1a9e5f?style=for-the-badge)](https://mibrahim02.pythonanywhere.com/)
[![GitHub Stars](https://img.shields.io/github/stars/mibrahim-O2/bin-khalid-dairy-farm?style=for-the-badge&color=gold)](https://github.com/mibrahim-O2/bin-khalid-dairy-farm/stargazers)

</div>

---

## 📖 The Story Behind This Project

**Bin Khalid** (بن خالد) means *Son of Khalid* in Arabic a name I chose with pride for this project, dedicated to my father **Khalid**, who runs our family dairy farm in Shahdadpur, Sindh, Pakistan.

For years, our farm manager handled every customer bill manually, calculating milk quantities, writing totals, and keeping records by hand every single month. It was time-consuming, error-prone, and entirely dependent on paper.

As a Computer Science student, I decided to solve this the right way by building a complete digital management system from scratch. Today, this software is **actively used every month** by our farm manager to generate customer bills, track milk delivery, and manage all voucher records. It turned a slow manual process into a fast, professional, digital workflow.

This is not a practice project. **This is real software, solving a real problem, for a real business.**

---

## 🌐 Deployment
> Online deployment is currently in progress.  
> The system is fully functional in the local development environment.
---
## 📸 Screenshots

<div align="center">

### 🔐 Login Page
*A clean, split-panel login interface with farm branding*

<img src="https://raw.githubusercontent.com/mibrahim-O2/bin-khalid-dairy-farm/main/Screenshots/login.png"
     alt="Login Page" width="85%" />

---

### 📊 Dashboard
*Live monthly stats, customer voucher table, and integrated add-voucher form*

<img src="https://raw.githubusercontent.com/mibrahim-O2/bin-khalid-dairy-farm/main/Screenshots/dashboard.png"
     alt="Dashboard" width="85%" />

---

### 🧮 Live Bill Calculator
*Bill total recalculates instantly as data is entered — no manual math needed*

<img src="https://raw.githubusercontent.com/mibrahim-O2/bin-khalid-dairy-farm/main/Screenshots/livecalculation.png"
     alt="Live Bill Calculator" width="35%" />

---

### ℹ️ Help & Info Panel
*Quick-access farm information, contact details, and payment info*

<img src="https://raw.githubusercontent.com/mibrahim-O2/bin-khalid-dairy-farm/main/Screenshots/help.png"
     alt="Help Panel" width="85%" />

---

### 🧾 Customer Bill — Mobile Optimized
*Professional bilingual bill (English + Urdu) downloadable as a PNG image for WhatsApp sharing*

<img src="https://raw.githubusercontent.com/mibrahim-O2/bin-khalid-dairy-farm/main/Screenshots/billview.png"
     alt="Bill View" width="40%" />

</div>

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 🔐 | **Secure Authentication** | Session-based login system with environment variable support for production credentials |
| 📊 | **Live Dashboard** | Real-time monthly summary, total milk collected, income earned, active customers, and voucher count |
| 🧮 | **Live Bill Calculator** | Voucher form recalculates total milk and final bill amount instantly as fields are filled |
| 🧾 | **Bilingual Bills** | Professional customer bills with full English and Urdu labels on every field |
| 📥 | **Save Bill as Image** | Export any bill as a high-resolution PNG, ready to share directly on WhatsApp |
| 📋 | **Customer History** | View the complete voucher history for any customer with cumulative milk and billing totals |
| ✏️ | **Edit & Delete Vouchers** | Modify any record with a live recalculation preview before committing changes |
| 🔍 | **Customer Search** | Instantly filter the customer list by name |
| 📱 | **Fully Responsive** | Clean, usable experience across mobile, tablet, and desktop |
| 🇵🇰 | **Urdu RTL Support** | Urdu payment reminder notice and field labels rendered correctly in right-to-left direction |
| 🔔 | **Flash Notifications** | Real-time success, error, and info toast notifications for every user action |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+, Flask 3.0 |
| **Database** | SQLite3, zero-configuration, file-based |
| **Frontend** | Bootstrap 5.3, Font Awesome 6.5 |
| **Typography** | Playfair Display, DM Sans, Google Fonts |
| **Bill Export** | html2canvas 1.4.1 |
| **Production Server** | Gunicorn |
| **Deployment** | PythonAnywhere |
| **Logo Design** | Canva / Google Gemini AI |

---
## 📁 Project Structure

```text
bin-khalid-dairy-farm/
│
├── static/
│   └── buffalo.png              ← Custom farm logo
│
├── templates/
│   ├── base.html                ← Shared layout (sidebar, topbar, flash toasts)
│   ├── login.html               ← Split-panel login page
│   ├── index.html               ← Main dashboard
│   ├── edit.html                ← Edit voucher with live recalculation
│   ├── bill.html                ← Mobile bill with Save as Image
│   └── history.html             ← Full customer voucher history
│
├── Screenshots/                 ← Project screenshots
│
├── app.py                       ← Flask routes and business logic
├── init_db.py                   ← One-time database initialisation
├── database.db                  ← SQLite database (auto-generated)
├── requirements.txt             ← Python dependencies
└── .gitignore                   ← Git ignore rules
````
---

## 🗄️ Database Schema

**Table: `vouchers`**

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Primary key, auto-increment |
| `name` | TEXT | Customer name |
| `date` | TEXT | Voucher date (YYYY-MM-DD) |
| `days` | INTEGER | Total days milk was delivered |
| `rate` | REAL | Rate per KG in PKR |
| `daily` | REAL | Daily milk quantity in KG |
| `extra` | REAL | Extra milk added |
| `used` | REAL | Milk deducted |
| `due` | REAL | Previous outstanding balance |
| `total_milk` | REAL | Calculated total milk (KG) |
| `amount` | REAL | Calculated milk amount (PKR) |
| `final_bill` | REAL | Final bill including dues (PKR) |
| `created_at` | TEXT | Record creation timestamp |

---

## 🧮 Billing Formula

The system uses this formula to calculate every bill automatically:
```text
Total Milk = (Daily Milk × Total Days) + Extra Milk − Milk Deducted
Milk Amount = Total Milk × Rate per KG
Final Bill = Milk Amount + Previous Due
```
---
The dashboard form recalculates and previews this live as the operator fills in each field eliminating manual errors entirely.

---

## ⚙️ Local Installation

### 1 — Clone the repository

```bash
git clone https://github.com/mibrahim-O2/bin-khalid-dairy-farm.git
cd bin-khalid-dairy-farm
```

### 2 — Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Initialise the database

```bash
python init_db.py
```

### 5 — Start the application

```bash
python app.py
```

Open **http://localhost:10000** in your browser.

---
## 🚀 Deployment Guide

This project is ready to deploy on any Python-compatible hosting platform.
Below are the two most beginner-friendly free options.

---

### Option 1 — PythonAnywhere *(Recommended)*

1. Create a free account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Open a **Bash console** and clone the repository:

```bash
git clone https://github.com/mibrahim-O2/bin-khalid-dairy-farm.git
```

3. Create a virtual environment and install dependencies:

```bash
cd bin-khalid-dairy-farm
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
```

4. Go to the **Web** tab → Add a new web app → Choose **Manual configuration** → Set source directory and WSGI file pointing to `app.py`

---

### Option 2 — Render.com

1. Push your code to GitHub
2. Create a free account at [render.com](https://render.com)
3. New → **Web Service** → Connect your repository
4. Set the following:

| Field | Value |
|-------|-------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --host 0.0.0.0 --port 10000` |

5. Add environment variables under **Environment** tab:

```env
SECRET_KEY        = your-strong-random-secret-key
ADMIN_USERNAME    = your-username
ADMIN_PASSWORD    = your-strong-password
```

> ⚠️ Never use the default credentials (`admin` / `1234`) in a production environment.
---

## 🔮 Planned Improvements

The following enhancements are planned for future versions:

- [ ] 👥 Multi-user roles (Admin, Manager, Viewer)
- [ ] 📊 Visual analytics monthly charts and income graphs
- [ ] ☁️ PostgreSQL / MySQL cloud database support
- [ ] 🔔 Automated WhatsApp bill delivery to customers
- [ ] 📄 PDF bill export in addition to image download
- [ ] 🌐 Full Urdu language interface option

---

## 👨‍💻 About the Developer

I am a **Computer Science student** from Shahdadpur, Sindh, Pakistan.

I built this system to solve a real problem in my own family's business, replacing a slow, manual monthly billing process with a fast, professional, digital solution. Every part of this project from the Flask backend and SQLite database design to the responsive UI, bilingual bill generation, and live deployment was designed, built, and shipped by me.

This project represents my ability to take a real-world problem, design a complete solution, and deliver working software that people actually use.

> *"The best code is the code that solves a real problem for real people."*

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push to your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request
```

---

## 📞 Farm Information

| | |
|---|---|
| 🏡 **Farm Name** | Bin Khalid Dairy Farm |
| 📍 **Location** | Shahdadpur, Sindh, Pakistan |
| 📞 **Phone** | 0324-2991303 |
| 💚 **Easypaisa** | 0324-299130 |
| ❤️ **JazzCash** | 0324-2991303 |
| 👤 **Account Title** | Muhammad Ibrahim |

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
You are free to use, modify, and distribute it with attribution.

---

<div align="center">

**Built with ❤️ for family dairy farm**

*Shahdadpur, Sindh, Pakistan 🇵🇰*

<br/>

⭐ **If this project helped or inspired you, please consider giving it a star!** ⭐

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-mibrahim--O2-181717?style=for-the-badge&logo=github)](https://github.com/mibrahim-O2)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-mibrahim02.pythonanywhere.com-1a9e5f?style=for-the-badge)](https://mibrahim02.pythonanywhere.com/)

</div>

