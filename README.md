# incident_api_task

## Установка и запуск

### 1. Клонирование и переход в проект
```bash
git clone git@github.com:opchik/incident_api_task.git
cd incident_api_task/
```

### 2. Создание необходимый переменных окружения
В корне необходимо создать файл .env в который поместить свои данные для БД:
```bash
cat > .env << EOF
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_PORT=5432
EOF
```

### 3. Сборка и запуск docker-compose
```bash
sudo docker-compose up -d
```

### 4. Применение миграций
```bash
sudo docker-compose exec web alembic upgrade head
```

-------------------------------------------------------------

Для проверки работы функционала программы можно перейти по адресу:
http://127.0.0.1:8000/docs

Если вы изменяли настройки, то при помощи команды:
```bash
sudo docker-compose logs -f web
``` 
можно посмотреть, по какому адресу открыт сайт. В путь в таком случае надо будет дописать "docs" для того, чтобы попасть в документацию swagger.

-------------------------------------------------------------

| Method    | Endpoint                   | Description |
|-----------|----------------------------|-------------|
| **POST**  | `/incidents/`              | Create new incident |
| **GET**   | `/incidents/`              | Get list of incidents (with optional status filter) |
| **GET**   | `/incidents/{incident_id}` | Get specific incident by ID |
| **PATCH** | `/incidents/{incident_id}` | Update incident status         |
| **GET**   | `/`                        | API root / health check          |


