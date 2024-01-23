/////import datetime
import os
import pytz


# Айди организации. Находится в профиле рекера.
ORG_ID = os.environ.get('BOT-1')

# Токен приложения трекера.
YANDEX_TOKEN = os.environ.get('a1627f2256a04902899c826e0b3e30fc')

# Токен вашего телеграмм бота.
TELEGRAM_TOKEN = os.environ.get('6369195255:AAFEos4YS_jOFRgQ1xghXHyhV_b76OpGvIQ')

# Задаем таймзону и время, чтобы отфильтровать новые задачи за последние 20 минут.
tz = pytz.timezone("Europe/Moscow")
twenty_min_past = datetime.datetime.now(tz) - datetime.timedelta(minutes=20)

# Фиксируем формат времени.
time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
