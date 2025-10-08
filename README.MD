FastAPI ToDo API with Authentication

A ToDo REST API built with FastAPI, PostgreSQL, and SQLAlchemy ORM, including JWT-based Authentication and Alembic for migrations.

🚀 Features

✅ User Registration & Login (JWT Authentication)
✅ Create, Read, Update, Delete ToDos
✅ Access control — Each user can only manage their own ToDos
✅ PostgreSQL database
✅ Alembic for version-controlled migrations
✅ Fully tested with Swagger UI and cURL

🧠 Tech Stack

FastAPI – Backend Framework

SQLAlchemy – ORM for database management

Alembic – Database migrations

PostgreSQL – Database

Pydantic – Data validation

Uvicorn – ASGI server

🏗️ Project Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/fastapi-todo-app.git
cd fastapi-todo-app

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Create .env File

Inside your project root, create a .env file with:

DATABASE_URL=Your_Database_url
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

🧩 Database Setup (Alembic)
Step 1: Initialize Alembic
alembic init alembic

Step 2: Edit alembic.ini

Find this line:

sqlalchemy.url = driver://user:pass@localhost/dbname


Replace it with your environment variable:

sqlalchemy.url = postgresql://username:password@localhost:5432/YourDB


Or better, load it dynamically in alembic/env.py:

from dotenv import load_dotenv
import os
from sqlalchemy import engine_from_config, pool
from alembic import context

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

Step 3: Generate and Apply Migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head


✅ This creates tables: users, todos, refresh_tokens, and alembic_version.

▶️ Run the Application
uvicorn app.main:app --reload


Swagger UI will be available at:
👉 http://127.0.0.1:8000/docs

🔑 Authentication Flow
Register User

POST /auth/register

{
  "username": "harshit",
  "email": "harshit@example.com",
  "password": "password123"
}

Login User

POST /auth/login (Form data)

Get access_token and refresh_token

Use your token in Swagger:

Authorization: Bearer <access_token>

🧾 ToDo API Endpoints
Method	Endpoint	Description
POST	/todos/	Create new ToDo
GET	/todos/	List user ToDos
GET	/todos/{id}	Get ToDo by ID
PUT	/todos/{id}	Update ToDo
DELETE	/todos/{id}	Delete ToDo
🗃️ Database Example (PostgreSQL)
SELECT * FROM users;
SELECT * FROM todos;


Example result:

id	title	description	completed	user_id
1	Todo Application	this is todo api application	False	2
📂 Folder Structure
app/
│
├── routers/
│   ├── auth_router.py
│   └── todo_router.py
│
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── deps.py
├── auth.py
└── main.py

🏁 Future Enhancements
Add frontend (React or Next.js)

Add user roles (Admin, Regular User)

Implement task priority & deadlines

Deploy on Render / Railway / AWS
