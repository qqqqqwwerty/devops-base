# DevOps Practice Stack

Полноценное локальное окружение для разработки с мониторингом, алертингом в Telegram и изоляцией сетей. Проект демонстрирует навыки работы с Docker Compose, Prometheus, Grafana и управлением конфигурациями через Git Flow.

## Архитектура

- **Web:** Nginx (Alpine) — прокси и статика
- **Backend:** Python 3.12 — HTTP сервер с экспортом метрик
- **Database:** PostgreSQL 14 — хранение данных
- **Monitoring:** Prometheus + Alertmanager + Grafana
- **Alerting:** Уведомления в Telegram при падении сервисов
- **Infra:** Multi-environment (.env.dev / .env.prod), изолированные сети

### Старт

## Клонирование и настройка
git clone git@github.com:ТВОЙ_НИК/devops-base.git
cd devops-base
cp .env.dev .env
# Отредактируй .env, добавив свои пароли и Telegram токены
nano .env

## Запуск стека
docker-compose --env-file .env \
  -f docker-compose.yml \
  -f monitoring/docker-compose.monitoring.yml up -d

## Сервисы 
App localhost:8080
metrics localhost:8080/metrics
prometheus localhost:9090
grafana localhost:3000
alertmanager localhost:9093
