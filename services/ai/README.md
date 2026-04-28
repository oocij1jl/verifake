# AI Services

이 폴더는 Verifake의 AI 관련 코드들을 두는 영역입니다.

권장 구조:
- `deepfakebench/` : 외부 기반 벤치마크/학습 엔진
- `inference/` : 서비스용 추론 래퍼
- `common/` : 공통 유틸 및 헬퍼

## AntiDeepfake integration

- Vendored upstream source stays in `services/ai/antideepfake/`.
- Audio-pipeline-facing wrapper lives in `services/ai/audio_pipeline/antideepfake.py`.
- Default repo-specific inference config lives in `services/ai/antideepfake/hparams/mms_300m_audio_pipeline.yaml`.
- Default checkpoint path is `services/ai/checkpoints/audio/antideepfake/mms_300m.ckpt`.
- Default runtime entrypoint for the wrapper is:
  - `python -m services.ai.audio_pipeline.antideepfake <audio-file>`
- Direct vendored entrypoint is:
  - `python services/ai/antideepfake/main.py inference services/ai/antideepfake/hparams/mms_300m_audio_pipeline.yaml --base_path <repo-root> --test_csv <protocol.csv> --ckpt_path services/ai/checkpoints/audio/antideepfake/mms_300m.ckpt`

### Dependency notes

- Use `services/ai/antideepfake/requirements.txt` for the AntiDeepfake runtime.
- The upstream code depends on a pinned `fairseq` commit; do not replace it with the latest PyPI release.
- In the Python 3.9 AntiDeepfake environment, pin `pip==24.0` before installing `services/ai/antideepfake/requirements.txt`.
- This avoids the `fairseq` / `omegaconf 2.0.x` metadata rejection that newer pip versions trigger.

### TODOs

- TODO: map raw AntiDeepfake logits/probabilities into the richer `AudioAnalysisResult` schema once the rest of the audio evidence pipeline is ready.
- TODO: add additional upstream model configs only when this repo actually needs them.
