from fastapi import FastAPI, Form, status, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
from jinja2 import Template

app = FastAPI(title="Sip API Portal")

# Mock User Database
users = [
    {"name": "admin", "psw": "password", "admin": True},
    {"name": "Jhony", "psw": "sip", "admin": True}
]

# Jinja2 Template for styled response pages
RESULT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Status</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            --card-bg: rgba(30, 41, 59, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --success-color: #10b981;
            --error-color: #ef4444;
            --btn-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        body {
            background: var(--bg-gradient);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-primary);
            overflow: hidden;
            position: relative;
        }

        /* Ambient glow spots */
        body::before, body::after {
            content: '';
            position: absolute;
            width: 300px;
            height: 300px;
            border-radius: 50%;
            filter: blur(120px);
            z-index: 0;
            opacity: 0.4;
            pointer-events: none;
        }

        body::before {
            background: {% if success %}#10b981{% else %}#ef4444{% endif %};
            top: 20%;
            left: 20%;
        }

        body::after {
            background: #1e1b4b;
            bottom: 20%;
            right: 20%;
        }

        .result-container {
            width: 100%;
            max-width: 440px;
            padding: 3rem 2.5rem;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            z-index: 1;
            text-align: center;
            animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .status-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 72px;
            height: 72px;
            border-radius: 50%;
            margin-bottom: 1.5rem;
            background: {% if success %}rgba(16, 185, 129, 0.1){% else %}rgba(239, 68, 68, 0.1){% endif %};
            border: 2px solid {% if success %}#10b981{% else %}#ef4444{% endif %};
            color: {% if success %}#10b981{% else %}#ef4444{% endif %};
        }

        .status-icon svg {
            width: 36px;
            height: 36px;
        }

        h1 {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            background: linear-gradient(to right, #ffffff, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .message {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
            line-height: 1.5;
        }

        .action-btn {
            display: inline-block;
            width: 100%;
            padding: 14px;
            background: var(--btn-gradient);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
        }

        .action-btn:hover {
            opacity: 0.95;
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.3);
        }

        .action-btn:active {
            transform: translateY(1px);
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.2);
        }
    </style>
</head>
<body>
    <div class="result-container">
        <div class="status-icon">
            {% if success %}
            <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"></path>
            </svg>
            {% else %}
            <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
            {% endif %}
        </div>
        <h1>{{ title }}</h1>
        <p class="message">{{ message }}</p>
        <a href="/" class="action-btn">Go Back</a>
    </div>
</body>
</html>
"""

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/greet")
def greet(name: str, age: int = None):
    return {"message": f"hello, {name}, Age {age}!"}


class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"message": f"User {user.name} of age {user.age} created successfully!"}

@app.post("/items", status_code=status.HTTP_201_CREATED)
def add_item(item: dict):
    return {"created": True}

todos = []

@app.post("/todos")
def add(todo: str):
    todos.append(todo)
    return {"todos": todos}

@app.get("/todos")
def list_todos():
    return {"todos": todos}

@app.delete("/todos")
def delete(index: int):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Todo index out of range")
    todos.pop(index)
    return {"todos": todos}

@app.post("/login", response_class=HTMLResponse)
def login_post(uname: str = Form(""), psw: str = Form("")):
    # Check credentials against the mock database (case-insensitive username check)
    user = next((u for u in users if u["name"].lower() == uname.strip().lower() and u["psw"] == psw), None)
    
    template = Template(RESULT_TEMPLATE)
    if user:
        html_content = template.render(
            success=True,
            title="Access Granted",
            message=f"Welcome back, {user['name']}! You have successfully signed in to the Sip API Portal."
        )
    else:
        html_content = template.render(
            success=False,
            title="Access Denied",
            message="Invalid username or password. Please double-check your credentials and try again."
        )
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)