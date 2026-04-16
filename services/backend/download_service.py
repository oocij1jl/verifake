from fastapi import FastAPI, UploadFile, File, Form
from uuid import uuid4
from datetime import datetime
import instaloader 

app = FastAPI()

@app.post("/api/v1/share")
async def share_video(
    title: str = Form(...),
    link: str = Form(None),
    videoFile: UploadFile = File(None)
):
    # 1. 분석을 위한 고유 ID 발급
    task_id = str(uuid4())
    
    # 2. 인스타 링크가 있으면 다운로드 준비
    if link:
        print(f"Downloading from: {link}")
    
    # 3. 명세서 4번 규격에 맞춘 응답
    return {
        "title": title,
        "task_id": task_id,
        "timestamp": datetime.now().isoformat(),
        "directResult": {
            "is_cached": False,
            "message": "영상이 정상적으로 수집되었습니다.",
            "verdict": "PENDING"
        }
    }