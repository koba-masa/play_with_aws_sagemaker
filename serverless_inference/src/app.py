from fastapi import FastAPI
import uvicorn

import glob
import os

app = FastAPI()

@app.get("/ping")
def ping():
    return {"Hello": "World"}


@app.post("/invocations")
def transformation():
    os_env_path = os.environ.get('PATH')
    opt_ml_mode_dir = "/opt/ml/model"
    opt_ml_mode_files = {
        'dir': opt_ml_mode_dir,
        'files': []
    }
    files = glob.glob(f"{opt_ml_mode_dir}/*")
    for file in files:
        opt_ml_mode_files['files'].append(file)

    results = {
        "opt_ml_mode_files": opt_ml_mode_files,
        "os_env_path": os_env_path
    }

    return {"results": results}


# if __name__ == "__main__":
#     uvicorn.run(
#         "app:app",
#         host="0.0.0.0",
#         port=8080
#     )
