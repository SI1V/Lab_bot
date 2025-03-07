from loguru import logger
import sys
from pathlib import Path

# Создаём папку для логов, если её нет
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Удаляем стандартные обработчики, чтобы избежать дублирования
logger.remove()

# Логирование в консоль (с цветами)
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | "
           "<cyan>{module}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

# Логирование в файл (общий лог)
logger.add(
    LOG_DIR / "app.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    rotation="5 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    enqueue=True,
)

# Логирование ошибок в отдельный файл
logger.add(
    LOG_DIR / "error.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {file}:{line}",
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    level="ERROR",
    enqueue=True,
)

def get_logger():
    return logger
