Учебный проект по курсу Stepik

# Автоматизация тестирования API с Python

Учебный репозиторий, собранный по ходу курса «Автоматизация тестирования API с Python. Базовый» (Stepik, автор — Никита Филонов). 

Цель — не набор разрозненных скриптов, а **полноценный тестовый фреймворк для API-тестирования**, построенный поэтапно: от первого HTTP-запроса до параллельного запуска в CI/CD с Allure-отчётами.

Стек: 

**HTTPX, Pydantic, pytest, JSON Schema, Allure / Allure TestOPS, GitHub Actions / GitLab CI**.

Помимо HTTP — работа с **gRPC, WebSocket и TCP/IP**, генерация тестовых данных через **Faker**, 

валидация ответов по **JSON Schema**, 

анализ покрытия API через **swagger-coverage-tool** 

и подключение **AI Review** к ревью кода в Pull Request.
