# Телеграм бот для проекта "Телеагроном"

### Запуск через docker
Чтобы запустить весь сервис, используйте *docker compose*. 
Для корректной работы бота требуется указать переменную окружения **TELEGRAM_API_TOKEN**

### Запуск напрямую
Для запуска бота установите зависимости используя *poetry*.
Для корректной работы бота требуется указать переменную окружения **TELEGRAM_API_TOKEN**

## Конфигурация через переменные окружения
Переменные окружения можно задать в файле `.env`, расположив файл в корне проекта.

#### Обязательные параметры
- **TELEGRAM_API_TOKEN** = *123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11* - токен для телеграм бота

#### Дополнительные параметры
- **API_HOST** = *http://dev.teleagronom.com* - endpoint для API запросов
- **DEBUG** = *True | False* - включает дополнительное логирование. По умолчанию *False*
  

- **SENTRY_DSN** = *https://public@sentry.example.com/1* - адрес dsn для sentry. По умолчанию пустой. 
  Если не указан, sentry не будет использоваться. Строчка должна быть в формате 
  `{PROTOCOL}://{PUBLIC_KEY}:{SECRET_KEY}@{HOST}{PATH}/{PROJECT_ID}`


- **USE_REDIS** = *True | False* - использовать redis как базу данных. По умолчанию *False*.
  Если не указано или указано *False*, в корне проекта будет создан файл `db.json` для дальнейшего использования в качестве базы данных
- **REDIS_IP** = *redis_db* - IP для подключения к redis
- **REDIS_PORT** = *6379* - port для подключения к redis
- **REDIS_PASSWORD** = *secret_password* - master пароль для подключения к redis. По умолчанию не задан

## Генерация адаптера для API
Для генерации использовался автогенератор клиент части от swagger: https://editor.swagger.io.
На момент создания бота API, описанное в swagger сайта, не везде совпадает с реальным API сайта.
Поэтому в адаптер вносились изменения для корректной работы некоторых запросов и аутентификации. 
