"""Audio pipeline schemas and helpers."""

from __future__ import annotations

from importlib import import_module

__all__ = [
    "AntiDeepfakeInferenceResult",
    "AudioAnalysisRequest",
    "AudioAnalysisResult",
    "EvidenceLevel",
    "OriginalAudioMetadata",
    "SuspiciousAudioSegment",
    "preprocess_audio",
    "run_antideepfake_inference",
]


def __getattr__(name: str):
    if name in {"AntiDeepfakeInferenceResult", "run_antideepfake_inference"}:
        module = import_module(".antideepfake", __name__)
        return getattr(module, name)

    if name == "preprocess_audio":
        module = import_module(".audio_preprocess", __name__)
        return getattr(module, name)

    if name in {
        "AudioAnalysisRequest",
        "AudioAnalysisResult",
        "EvidenceLevel",
        "OriginalAudioMetadata",
        "SuspiciousAudioSegment",
    }:
        module = import_module(".schemas", __name__)
        return getattr(module, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
