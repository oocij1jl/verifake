from __future__ import annotations

import unittest


class DownloadServiceTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        from services.backend.tasks import upload_tasks_db

        upload_tasks_db.clear()

    async def test_upload_video_creates_pending_upload_task(self) -> None:
        from services.backend.download_service import upload_video
        from services.backend.tasks import upload_tasks_db

        response = await upload_video(title="sample", link=None, videoFile=None)
        task_id = response["task_id"]

        self.assertIn(task_id, upload_tasks_db)
        self.assertEqual(upload_tasks_db[task_id]["status"], "PENDING")
        self.assertIsNone(upload_tasks_db[task_id]["verdict"])

    async def test_get_status_returns_existing_upload_shape(self) -> None:
        from services.backend.download_service import get_status
        from services.backend.tasks import create_upload_task

        create_upload_task("upload-1")
        result = await get_status("upload-1")

        self.assertEqual(result["task_id"], "upload-1")
        self.assertEqual(result["status"], "PENDING")
        self.assertIn("timestamp", result)
        self.assertIn("verdict", result)

    async def test_get_status_raises_for_missing_upload_task(self) -> None:
        from fastapi import HTTPException

        from services.backend.download_service import get_status

        with self.assertRaises(HTTPException) as context:
            await get_status("missing")

        self.assertEqual(context.exception.status_code, 404)


if __name__ == "__main__":
    unittest.main()
