# 📜 Quotes Web Application

A containerized 3-tier web application using **Flask**, **MongoDB**, and **Nginx**.

---

## 🏛 Architecture & Networks

The app is split into 3 tiers with isolated networks for security:

* **`frontend-backend` Network**: Connects `frontend` and `backend`.
* **`backend-db` Network**: Connects `backend` and `database` (Database is completely isolated from the frontend).

---

## 📁 Project Structure

```text
.
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   └── index.html
├── Dockerfile          # Database Dockerfile
├── init-script.js      # MongoDB Initialization Script
├── docker-compose.yml
└── README.md


```
## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mennatullahelshahawy/quote-app.git](https://github.com/mennatullahelshahawy/quote-app.git)
   cd quote-app
   ```
2. **Start the application:**
   ```bash
   docker compose up --build -d
   ```
3. **Access the App:**
   * **Frontend:** `http://localhost`
   * **Backend API:** `http://localhost:5000`

---

## 🛠 Features

* **Network Isolation:** Secure 2-network topology (`frontend-backend` & `backend-db`).
* **Database Persistence:** Data saved using Docker volumes (`db_data`).
* **Auto Initialization:** Database automatically seeds initial quotes on first run.
* **Health Checks:** Ensures Backend waits for MongoDB to fully start before connecting.


