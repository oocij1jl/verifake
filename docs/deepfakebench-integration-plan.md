# DeepfakeBench 통합 방향 (services/ai 기준)

이 문서는 `DeepfakeBench` 코드를 `verifake` 레포 안으로 가져올 때,
기존 레포 구조를 깨지 않으면서 `services/ai/` 기준으로 어떻게 배치하는 것이 좋은지 정리한 문서입니다.

---

## 1. 기본 원칙

`DeepfakeBench`는 인프라 코드가 아니라,
딥페이크 탐지 모델의 **학습 / 전처리 / 평가 / 추론 기반 엔진** 역할에 가깝습니다.

따라서 `verifake/infra/`에 두는 것보다,
**`verifake/services/ai/` 아래에 두는 것이 더 적절합니다.**

---

## 2. 추천 배치 위치

추천 경로:

```text
verifake/
  services/
    ai/
      deepfakebench/
```

즉,
`DeepfakeBench` 원본 성격을 유지하되,
`verifake` 안에서는 AI 서비스 레이어의 하위 엔진으로 취급합니다.

---

## 3. 추천 폴더 구조

```text
verifake/
  docs/
    deepfakebench-integration-plan.md
  infra/
  services/
    ai/
      README.md
      deepfakebench/
        README.md
        LICENSE
        analysis/
        preprocessing/
        training/
```

---

## 4. 왜 이렇게 나누는가

### 1) 기존 레포 구조를 보호하기 위해
`verifake`는 이미 자체적인 구조와 역할이 있기 때문에,
`DeepfakeBench`를 루트에 그대로 풀어버리면 레포 정체성이 흐려질 수 있습니다.

### 2) 외부 코드와 내부 코드를 구분하기 위해
- `services/ai/deepfakebench/` = 외부 기반 벤치마크 엔진
- 이후 `services/ai/inference/`, `services/ai/pipelines/` = 우리 서비스용 래퍼/추론 로직

이렇게 분리하면 유지보수가 쉬워집니다.

### 3) 향후 교체 가능성을 열어두기 위해
나중에 `DeepfakeBench` 대신 다른 엔진을 쓸 수도 있기 때문에,
외부 코드를 독립된 하위 폴더로 두는 것이 좋습니다.

---

## 5. 어떤 부분을 우선 가져오면 좋은가

우선순위 기준으로 보면:

### 1순위
- `training/`
- `preprocessing/`

### 2순위
- `analysis/`

### 3순위
- 필요 시 `README.md`, `LICENSE`

초기에는 전체를 다 활용하기보다,
**전처리 + 학습/탐지 핵심 구조 중심**으로 들여오는 것이 좋습니다.

---

## 6. 현재 단계에서 추천하는 통합 방식

### 단계 1
`services/ai/deepfakebench/` 폴더를 만들고,
외부 코드가 이 위치에 들어온다는 기준을 먼저 고정합니다.

### 단계 2
`services/ai/README.md`를 두어,
이 레이어가 어떤 목적의 코드들을 담는지 설명합니다.

### 단계 3
`DeepfakeBench`는 원본 그대로 가져오되,
`verifake` 서비스용 코드는 그 바깥에 별도로 만듭니다.

예:

```text
services/ai/
  deepfakebench/
  inference/
  common/
```

---

## 7. 지금 바로 하면 좋은 최소 작업

1. `docs/deepfakebench-integration-plan.md` 추가
2. `services/ai/README.md` 추가
3. `services/ai/deepfakebench/.gitkeep` 또는 안내 파일 추가
4. 이후 실제 코드 반입은 별도 커밋으로 진행

즉,
**구조와 기준을 먼저 만들고, 원본 코드는 그 다음에 넣는 방식**이 안전합니다.

---

## 8. 한 줄 결론

`DeepfakeBench`는 `verifake/infra/`가 아니라,
**`verifake/services/ai/deepfakebench/` 아래에 두는 것이 가장 적절하며**, 
이렇게 해야 기존 레포 구조를 보존하면서도 AI 엔진 코드를 명확히 분리할 수 있습니다.
