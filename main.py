from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from any frontend (e.g. WeWeb)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 Here's your function - this is where you write your logic
@app.post("/process")
async def process_data(request: Request):
    data = await request.json()

    name = data.get("name")
    age = data.get("age")

    # ✅ You write your logic here
    result = {
        "message": f"Hello {name}, you will be {age + 1} next year!"
    }

    return result
