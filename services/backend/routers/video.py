# pyright: reportMissingImports=false, reportMissingModuleSource=false, reportUninitializedInstanceVariable=false

import subprocess
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai.common.job_paths import build_job_paths
from services.ai.pipelines.video_stage1.detect import run_video_stage1_detection
from services.backend.services.processor import run_video_stage1_preprocess_job

router = APIRouter()


class VideoStage1PreprocessRequest(BaseModel):
    file_path: str
    job_id: str | None = None


class VideoStage1DetectRequest(BaseModel):
    preprocessing_json: str


@router.post("/video-stage1/preprocess", summary="Stage1 A 전처리 실행", tags=["Video"])
def preprocess_video_stage1(req: VideoStage1PreprocessRequest):
    try:
        input_path = Path(req.file_path)

        if not input_path.exists():
            raise HTTPException(status_code=400, detail="파일이 존재하지 않습니다.")

        result = run_video_stage1_preprocess_job(input_path, job_id=req.job_id)
        job_paths = build_job_paths(result["job_id"])

        return {
            "job_id": result["job_id"],
            "status": result["status"],
            "preprocessing_json": job_paths["preprocessing_json_path"].as_posix(),
        }

    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="ffmpeg 실행 실패")

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/video-stage1/detect", summary="Stage1 B 탐지 실행", tags=["Video"])
def detect_video_stage1(req: VideoStage1DetectRequest):
    preprocessing_json_path = Path(req.preprocessing_json)

    if not preprocessing_json_path.exists():
        raise HTTPException(
            status_code=400,
            detail="preprocessing.json 파일이 존재하지 않습니다.",
        )

    try:
        detection = run_video_stage1_detection(str(preprocessing_json_path))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    job_root = preprocessing_json_path.parent.parent
    return {
        "job_id": detection["job_id"],
        "status": detection.get("status", "success"),
        "detection_json": str(job_root / "output" / "detection.json"),
        "result_json": str(job_root / "output" / "result.json"),
    }
