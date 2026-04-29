# pyright: reportMissingImports=false

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from services.backend.main import app
from services.backend.routers import video


client = TestClient(app)


def test_main_exposes_media_stage1_preprocess_route(
    monkeypatch,
    tmp_path: Path,
) -> None:
    input_path = tmp_path / "sample.mov"
    input_path.write_bytes(b"data")

    def fake_run_video_stage1_preprocess_job(file_path: Path, job_id: str | None = None) -> dict[str, str]:
        return {"job_id": job_id or "job_media_001", "status": "success"}

    monkeypatch.setattr(
        video,
        "run_video_stage1_preprocess_job",
        fake_run_video_stage1_preprocess_job,
    )

    response = client.post(
        "/media/video-stage1/preprocess",
        json={"file_path": str(input_path), "job_id": "job_media_001"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "job_id": "job_media_001",
        "status": "success",
        "preprocessing_json": "storage/jobs/job_media_001/metadata/preprocessing.json",
    }


def test_main_exposes_media_stage1_detect_route(
    monkeypatch,
    tmp_path: Path,
) -> None:
    preprocessing_json = tmp_path / "storage" / "jobs" / "job_media_002" / "metadata" / "preprocessing.json"
    preprocessing_json.parent.mkdir(parents=True, exist_ok=True)
    preprocessing_json.write_text("{}", encoding="utf-8")

    def fake_run_video_stage1_detection(preprocessing_json_path: str) -> dict[str, str]:
        return {"job_id": "job_media_002", "status": "success"}

    monkeypatch.setattr(
        video,
        "run_video_stage1_detection",
        fake_run_video_stage1_detection,
    )

    response = client.post(
        "/media/video-stage1/detect",
        json={"preprocessing_json": str(preprocessing_json)},
    )

    assert response.status_code == 200
    assert response.json() == {
        "job_id": "job_media_002",
        "status": "success",
        "detection_json": str(preprocessing_json.parent.parent / "output" / "detection.json"),
        "result_json": str(preprocessing_json.parent.parent / "output" / "result.json"),
    }
