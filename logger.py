# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional


def get_logger(
        name: str,
        level: str = "INFO",
        log_file: Optional[str] = None,
        max_bytes: int = 10 * 1024 * 1024,  # 默认10MB
        backup_count: int = 5
) -> logging.Logger:
    """
    Create and configure a logger with console and optional file output.

    :param name: The name of the logger, typically the module name (e.g., __name__).
    :type name: str
    :param level: The logging level (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
    :type level: str
    :param log_file: Path to the log file. If None, only console logging is enabled.
    :type log_file: str or None
    :param max_bytes: Maximum size of the log file in bytes before rotation.
    :type max_bytes: int
    :param backup_count: Number of backup files to keep when rotating.
    :type backup_count: int
    :return: A configured logger instance.
    :rtype: logging.Logger
    :raises ValueError: If the provided level is not a valid logging level.

    Example:
        >>> logger = get_logger("my_module", level="DEBUG", log_file="app.log")

        >>> logger.info("This is an info message")
    """
    # 获取logger实例
    logger = logging.getLogger(name)

    # 避免重复添加handler（如果logger已有handler则跳过配置）
    if logger.hasHandlers():
        logger.handlers.clear()

    # 设置日志级别
    level = level.upper()
    try:
        logger.setLevel(getattr(logging, level))
    except AttributeError:
        raise ValueError(f"Invalid logging level: {level}. Use DEBUG, INFO, WARNING, ERROR, or CRITICAL.")

    # 定义日志格式
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 添加控制台handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # 如果指定了日志文件，添加文件handler（带旋转功能）
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)  # 确保目录存在
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger
