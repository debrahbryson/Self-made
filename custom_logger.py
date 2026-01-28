from datetime import datetime
from pathlib import Path


class Logger:
    LEVELS = {
        "INFO": "ℹ️",
        "WARNING": "⚠️",
        "ERROR": "❌",
        "DEBUG": "🐞"
    }

    def __init__(self, name="app", log_dir="logs", console=True):
        self.name = name
        self.console = console
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / f"{self.name}.log"

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write(self, level, message):
        icon = self.LEVELS.get(level, "")
        log_entry = f"[{self._timestamp()}] {level} {icon} | {message}\n"

        with open(self.log_file, "a") as f:
            f.write(log_entry)

        if self.console:
            print(log_entry.strip())

    def info(self, message):
        self._write("INFO", message)

    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)

    def debug(self, message):
        self._write("DEBUG", message)


class LogSession:
    def __init__(self, logger):
        self.logger = logger

    def __enter__(self):
        self.logger.info("Log session started")
        return self.logger

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.logger.error(f"Exception: {exc_val}")
        self.logger.info("Log session ended")
