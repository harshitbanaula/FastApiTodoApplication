# FastAPI ToDo API with Authentication

A **ToDo REST API** built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy ORM**, featuring **JWT-based Authentication** and **Alembic** for database migrations.

---

## Features

-  User Registration & Login (**JWT Authentication**)  
-  Create, Read, Update, Delete (**CRUD**) ToDos  
-  Access Control – each user can manage **only their own ToDos**  
-  **PostgreSQL** database integration  
-  **Alembic** for version-controlled migrations  
-  Fully tested using **Swagger UI** and **cURL**

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | **FastAPI** |
| ORM | **SQLAlchemy** |
| Migrations | **Alembic** |
| Database | **PostgreSQL** |
| Data Validation | **Pydantic** |
| ASGI Server | **Uvicorn** |

---

## Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-todo-app.git
cd fastapi-todo-app
2️⃣ Create and Activate Virtual Environment
bash
Copy code
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create .env File
Inside your project root, create a .env file with the following content:

env
Copy code
DATABASE_URL=postgresql://username:password@localhost:5432/YourDB
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

## Database Setup (Alembic)
Step 1: Initialize Alembic
bash
Copy code
alembic init alembic
Step 2: Configure Alembic
In alembic.ini, find the line:

ini
Copy code
sqlalchemy.url = driver://user:pass@localhost/dbname
Replace it with:

ini
Copy code
sqlalchemy.url = postgresql://username:password@localhost:5432/YourDB
Or dynamically load your .env variable inside alembic/env.py:

python
Copy code
from dotenv import load_dotenv
import os
from sqlalchemy import engine_from_config, pool
from alembic import context

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL)
Step 3: Generate and Apply Migrations
bash
Copy code
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
✅ This creates tables: users, todos, refresh_tokens, and alembic_version.

## Run the Application
bash
Copy code
uvicorn app.main:app --reload
Swagger UI will be available at:
👉 http://127.0.0.1:8000/docs

🔑 Authentication Flow
🧍‍♂️ Register User
POST /auth/register

json
Copy code
{
  "username": "harshit",
  "email": "harshit@example.com",
  "password": "password123"
}

## Login User
POST /auth/login (Form Data)

Response contains:

access_token

refresh_token

Use the token in Swagger:
Authorization: Bearer <access_token>


##ToDo API Endpoints
Method	Endpoint	Description
POST	/todos/	Create a new ToDo
GET	/todos/	List all user ToDos
GET	/todos/{id}	Get a ToDo by ID
PUT	/todos/{id}	Update a ToDo
DELETE	/todos/{id}	Delete a ToDo

## Example Database (PostgreSQL)
Sample Query:
sql
Copy code
SELECT * FROM users;
SELECT * FROM todos;
Example Result:
id	title	description	completed	user_id
1	Todo Application	this is todo api application	False	2

##Folder Structure
pgsql
Copy code
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


##Future Enhancements
Add frontend (React or Next.js)

Add user roles (Admin, Regular User)

Implement task priority & deadlines

Deploy on Render / Railway / AWS