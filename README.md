Preview
![image](https://github.com/user-attachments/assets/4fbc89a1-aa70-4c35-ac9d-64af1f8d9deb)


# 📝 Flask + PostgreSQL Notes App (Dockerized)

A simple Flask web app that lets users add and view notes, stored in a PostgreSQL database — all running in Docker containers.

## 🚀 Features
- Add and view notes via a form.
- Notes are stored in a PostgreSQL database.
- Timestamps are shown for each note.
- Styled using Bootstrap for a cleaner UI.
- Docker Compose used to manage services.

## 🛠️ Stack
- Python 3 (Flask)
- PostgreSQL
- Docker + Docker Compose
- Bootstrap 5 (CDN)

## 🐳 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/flask-notes-app.git
cd flask-notes-app
```

### 2. Run with Docker Compose
```bash
docker-compose up --build
```

### 3. Access the app
Open your browser at: [http://localhost:5000](http://localhost:5000)

## 📁 Project Structure
```
flask-notes-app/
│
├── app/
│   ├── app.py                # Flask app
│   ├── requirements.txt      # Python dependencies
│
├── db/
│   └── init.sql              # SQL script to create notes table
│
├── Dockerfile                # Build Flask container
├── docker-compose.yml        # Compose file
└── README.md                 # This file
```

## 📋 Database Schema (`init.sql`)
```sql
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## ✅ To-Do / Ideas
- [ ] Add note deletion
- [ ] Add login / auth
- [ ] Store notes by user
- [ ] Export notes to CSV
- [ ] Deploy on Heroku / Render
