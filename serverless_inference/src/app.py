from fastapi import FastAPI
import uvicorn

import glob

app = FastAPI()

@app.get("/ping")
def ping():
    return {"Hello": "World"}


@app.post("/invocations")
def transformation():
    opt_ml_mode_dir = "/opt/ml/model"
    opt_ml_mode_files = {
        'dir': opt_ml_mode_dir,
        'files': []
    }
    files = glob.glob(f"{opt_ml_mode_dir}/*")
    for file in files:
        opt_ml_mode_files['files'].append(file)

    return {"invocated": opt_ml_mode_files}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080
    )
