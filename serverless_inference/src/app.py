from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
def ping():
    return {"Hello": "World"}

@app.post("/invocations")
def transformation():
    # 推論のコードをここに書きます。
    return {"invocated": True}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080
    )
