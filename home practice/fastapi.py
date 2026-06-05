from fastapi import FastAPI

app = FastAPI()

# GET request
@app.get("/users")
def get_users():
    return {"message": "List of users"}

# POST request
@app.post("/users")
def create_user():
    return {"message": "User created"}