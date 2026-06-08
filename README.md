# 🍵 API Portal

A sleek, full-stack REST API portal built with **FastAPI** and a custom glassmorphism login UI. Features JWT authentication, SQLAlchemy database integration, role-based access control, an admin dashboard, and a persistent Todo manager.

---

## ✨ Features

- 🔐 **JWT Authentication** — Secure token-based login with bcrypt password hashing
- 🗄️ **SQLAlchemy + SQLite** — Persistent database for users and todos
- 👮 **Role-Based Access Control** — Admin vs regular user route protection
- 📊 **Admin Dashboard** — Live stats on users, todos, and activity
- ✅ **Todo Manager** — Full CRUD with priority levels, status filtering, and per-user data
- 🎨 **Custom Login UI** — Dark glassmorphism design with smooth animations
- 🧪 **Pytest Test Suite** — Auth and endpoint tests with TestClient
- 📄 **Auto Swagger Docs** — Interactive API docs at `/docs`

---

## 🗂️ Project Structure

```
sip-api/
├── app.py           # Main FastAPI app — routes & startup
├── auth.py          # JWT token creation, bcrypt hashing
├── database.py      # SQLAlchemy engine & session dependency
├── models.py        # DB models: User, Todo
├── schemas.py       # Pydantic request/response schemas
├── test_app.py      # Pytest test suite
├── .env             # Secret keys (never commit this!)
├── index.html       # Login page UI
├── admin.html       # Admin dashboard UI
└── sip.db           # Auto-created SQLite database
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sip-api-portal.git
cd sip-api-portal
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt] python-dotenv jinja2 httpx pytest
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_super_secret_key_change_this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

### 5. Run the server

```bash
uvicorn app:app --reload
```

The app will be live at **http://127.0.0.1:8000**

---

## 📡 API Endpoints

### Auth

| Method | Endpoint  | Description              | Auth Required |
|--------|-----------|--------------------------|---------------|
| POST   | `/login`  | Login and receive JWT    | ❌            |

### Todos

| Method | Endpoint          | Description                     | Auth Required |
|--------|-------------------|---------------------------------|---------------|
| POST   | `/todos`          | Create a new todo               | ✅            |
| GET    | `/todos`          | List todos (filter by `status`) | ✅            |
| PATCH  | `/todos/{id}`     | Update todo status              | ✅            |
| DELETE | `/todos/{id}`     | Delete a todo                   | ✅            |

### Admin

| Method | Endpoint        | Description                  | Admin Only |
|--------|-----------------|------------------------------|------------|
| GET    | `/admin/stats`  | Get platform-wide statistics | ✅         |
| GET    | `/admin`        | Admin dashboard page         | ✅         |

### Misc

| Method | Endpoint       | Description                  |
|--------|----------------|------------------------------|
| GET    | `/`            | Login page                   |
| GET    | `/hello`       | Health check                 |
| GET    | `/greet`       | Greet by name and age        |
| POST   | `/user`        | Create a user (demo)         |
| GET    | `/docs`        | Swagger UI (auto-generated)  |

---

## 🔑 Authentication Flow

1. POST to `/login` with `uname` and `psw` form fields
2. On success, receive a **JWT access token**
3. Include the token in the `Authorization` header for protected routes:

```
Authorization: Bearer <your_token>
```

Tokens expire after the duration set in `ACCESS_TOKEN_EXPIRE_MINUTES`.

---

## ✅ Todo Filtering

Filter todos by status using a query parameter:

```
GET /todos?status=pending
GET /todos?status=done
```

Each user only sees their own todos.

---

## 🧪 Running Tests

```bash
pytest test_app.py -v
```

The test suite covers:

- ✅ Successful login
- ✅ Failed login with wrong credentials
- ✅ Creating a todo (authenticated)
- ✅ Accessing protected routes without a token (expects 401)

---

## 🛠️ Tech Stack

| Layer     | Technology                         |
|-----------|------------------------------------|
| Backend   | FastAPI, Python 3.10+              |
| Database  | SQLite via SQLAlchemy ORM          |
| Auth      | JWT (python-jose), bcrypt (passlib)|
| Templating| Jinja2                             |
| Frontend  | HTML5, CSS3 (glassmorphism)        |
| Testing   | Pytest, HTTPX TestClient           |
| Server    | Uvicorn (ASGI)                     |

---

## 🙋 Demo Credentials

> For testing purposes only. Replace with hashed passwords before production.

| Username | Password   | Role  |
|----------|------------|-------|
| `admin`  | `password` | Admin |
| `Jhony`  | `sip`      | Admin |

---

## 📌 Roadmap

- [ ] User registration endpoint (`POST /register`)
- [ ] Refresh token support
- [ ] Pagination on `/todos`
- [ ] Rate limiting on `/login` (brute-force protection)
- [ ] Dockerize the application
- [ ] Deploy to Render / Railway

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with ❤️ by [Astha](https://github.com/your-username)
