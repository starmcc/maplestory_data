import logging
from flask import Flask
from src.api import maple_bp  # 注册表现层蓝图


def create_app():
    app = Flask(__name__)

    # 日志配置
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    app.logger.info("Flask应用初始化完成")

    # 注册蓝图（表现层入口）
    app.register_blueprint(maple_bp, url_prefix='/maple_story')

    return app