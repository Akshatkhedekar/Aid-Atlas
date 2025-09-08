# 🗺️ Aid Atlas – Real-Time Emergency Mapping & Assistance Platform

## 📌 Project Overview

Aid Atlas is a **real-time emergency mapping and assistance platform** designed to make emergency response **faster, coordinated, and location-based**.

The system allows **citizens to report incidents** (accidents, crimes, fires, medical emergencies, etc.) which are then displayed on an **interactive live map**.
Authorities such as **police, hospitals, and fire stations** can log in to access **detailed reports** with full location and contact information, enabling quicker response times.

---

## 🚀 Features (Current Progress)

✅ **Phase 1 (Completed)**

* Built using **Flask (Python) + HTML/CSS/JavaScript**.
* Integrated **Leaflet.js** for live map visualization.
* Implemented **manual incident reporting** form.
* Stored reports in a **SQLite database**.
* Displayed incidents on map in real time.

✅ **Phase 2 (In Progress)**

* Added **user authentication** (via Flask-Login).
* Created **restricted dashboard** for authorities to see detailed incidents.
* Public users only see **generalized alerts**.
* Initial prototype of **real-time updates** for logged-in users.
* Planning **location-based filtering** (district/municipality-level).

⏳ **Upcoming (Phase 3 & 4)**

* Heatmaps & time-based analysis of incidents.
* Push notifications & email alerts.
* Automatic GPS detection for user location.
* AI/ML models for hotspot prediction (scikit-learn).
* NLP for analyzing incident descriptions (spaCy/Transformers).
* Deployment on **Heroku/Render** with PostgreSQL for scalability.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Framework:** Flask
* **Frontend:** HTML, CSS, JavaScript, Leaflet.js
* **Database:** SQLite (dev) → PostgreSQL (deployment)
* **Authentication:** Flask-Login
* **AI/ML (planned):** Pandas, Scikit-learn, spaCy/Transformers
* **Version Control:** Git & GitHub
* **Deployment:** Heroku / Render

---

## 📂 Project Structure

```
AidAtlas/
│
├── app.py              # Flask backend  
├── templates/          # HTML templates  
│   ├── index.html      # Public map & reporting UI  
│   ├── login.html      # Login page  
│   ├── dashboard.html  # Authority dashboard  
│
├── static/             # (optional) CSS, JS, assets  
├── aidatlas.db         # SQLite database (local)  
└── README.md           # Project documentation  
```

---

## 👨‍💻 Contributors

* Akshat Khedekar
* Om Kumbhar
* Yash Gupta
* Sneha Singh
* Gargi Singh
* Anika Khare

---

## 📈 Vision

Aid Atlas aims to become a **comprehensive emergency response tool** that bridges the gap between **citizens and authorities**. With AI-powered analytics, real-time notifications, and scalable deployment, it will strengthen **public safety, governance, and disaster management**.

---

Would you like me to also include a **setup guide (install + run instructions)** in this README, so that your teammates can clone and run the project easily?
