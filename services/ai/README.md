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

## 오디오 전처리

- 입력 파일을 내부 분석용 `WAV / mono / 16kHz / pcm_s16le` 형식으로 정규화하는 전처리 CLI는 `services/ai/audio_pipeline/audio_preprocess.py`에 둡니다.
- 실행 예시:
  - `python -m services.ai.audio_pipeline.audio_preprocess --input path/to/input.mp4 --output-dir outputs/audio --json-output outputs/audio/audio_preprocess_result.json`
- 이 단계는 전처리 전용입니다. VAD, sliding window, AntiDeepfake 추론, fake score 계산은 포함하지 않습니다.

### Dependency notes

- Use `services/ai/antideepfake/requirements.txt` for the AntiDeepfake runtime.
- The upstream code depends on a pinned `fairseq` commit; do not replace it with the latest PyPI release.
- In the Python 3.9 AntiDeepfake environment, pin `pip==24.0` before installing `services/ai/antideepfake/requirements.txt`.
- This avoids the `fairseq` / `omegaconf 2.0.x` metadata rejection that newer pip versions trigger.

### TODOs

- TODO: map raw AntiDeepfake logits/probabilities into the richer `AudioAnalysisResult` schema once the rest of the audio evidence pipeline is ready.
- TODO: add additional upstream model configs only when this repo actually needs them.
