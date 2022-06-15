from fastapi import FastAPI, UploadFile, File, HTTPException
import yaml
import os

api = FastAPI()


@api.get("/greeting")
def greet():
    name = os.environ.get("GREET_NAME", "")
    return {"msg": f"Hello {name}!"}


@api.post("/yamljson")
async def yamlToJson(file: UploadFile = File(...)):
    try:
        return yaml.safe_load(file.file)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail={"message": "Error parsing YAML", "detail": str(e)}
        )
