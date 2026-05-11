<div align="center">

# 🔔 GlucoVision Notification Service

**The async notification delivery engine for glucose alerts, meal reminders, and medication reminders.**  
*FCM + APNs push · Celery task queue · Localized templates (Sinhala / Tamil / English)*

[![FastAPI](https://img.shields.io/badge/FastAPI-Python-009688?style=for-the-badge&logo=fastapi)](#)
[![Celery](https://img.shields.io/badge/Celery-Task%20Queue-37814A?style=for-the-badge)](#)
[![Redis](https://img.shields.io/badge/Redis-Broker-DC382D?style=for-the-badge&logo=redis)](#)
[![Firebase](https://img.shields.io/badge/FCM-Push-FFCA28?style=for-the-badge&logo=firebase)](#)
[![Docker](https://img.shields.io/badge/Docker-Containerised-2496ED?style=for-the-badge&logo=docker)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-f59e0b?style=for-the-badge)](#)

</div>

---

## 📌 Purpose

GlucoVision Notification Service is the **decoupled, async notification pipeline** that delivers all patient-facing alerts — glucose emergencies, medication reminders, meal reminders, and appointment notifications. It is decoupled from the request path so that a slow FCM delivery never blocks a glucose prediction call.

> Owns its own queue, retry logic, and **localized content templates** for Sinhala and Tamil patients.

---

## 📁 Project Structure

```
08-glucovision-notification-service/
└── (Git repository initialised — structure to be scaffolded)
```

---

## ✨ Planned Features (by phase)

### Phase 1 — Push Delivery
- [ ] FCM push (Android) and APNs push (iOS)
- [ ] Device token registration and management
- [ ] Basic notification API

### Phase 2 — Alert Integration
- [ ] Glucose alerts from `13-risk-alert-engine` via message queue
- [ ] Delivery retry with exponential backoff
- [ ] Delivery receipt tracking

### Phase 3 — Reminders & Localization
- [ ] Meal and medication reminders (Celery Beat)
- [ ] Localized templates: English / Sinhala / Tamil
- [ ] Per-user notification preferences

---

## 🚀 Getting Started

### Prerequisites

- Python ≥ 3.11, Redis ≥ 7, PostgreSQL ≥ 15, Docker & Docker Compose

### Setup (once scaffolded)

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8003

# Celery worker + beat
celery -A worker worker --loglevel=info
celery -A worker beat --loglevel=info

# Or via Docker Compose
docker compose up --build
```

---

## 🏗️ Planned Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI (Python) |
| Task Queue | Celery |
| Broker | Redis |
| Push (Android) | firebase-admin (FCM) |
| Push (iOS) | apns2 / httpx (APNs HTTP/2) |
| Database | PostgreSQL (SQLAlchemy) |
| Scheduler | Celery Beat |
| Containerisation | Docker |

---

## 🔗 Backend Dependencies

| Service | Interaction |
|---|---|
| `13` risk-alert-engine | Triggers glucose alerts |
| `07` user-service | Language preference for localization |
| `15` recommendation-engine | Meal reminder schedule |
| `05` api-gateway | Request routing |

---

## 🔐 Security Notes

- FCM server key and APNs p8 key stored in HashiCorp Vault
- Patient PII never included in notification logs
- Only `13` and `15` can trigger alerts (internal auth)

---

## 🧪 Testing (Planned)

```bash
pytest tests/unit/          # Template rendering, localization
pytest tests/integration/   # Alert → Celery → FCM mock
pytest tests/localization/  # All 3 locales produce valid content
```

---

<div align="center">

*Part of the [GlucoVision Platform](../01-glucovision-platform-architecture) — 21-Repo AI Diabetes Management System*

</div>
