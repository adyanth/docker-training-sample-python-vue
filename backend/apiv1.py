from fastapi import FastAPI, UploadFile, File, HTTPException
import yaml

api = FastAPI()

@api.post("/yamljson")
async def yamlToJson(file: UploadFile = File(...)):
    try:
        return yaml.safe_load(file.file)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail={"message": "Error parsing YAML", "detail": str(e)}
        )
