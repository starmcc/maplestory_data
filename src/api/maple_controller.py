import logging
import time

from flask import jsonify, render_template

from src.api import maple_bp
from src.services.maple_service import MapleService  # 依赖业务层

@maple_bp.route('/', methods=['GET'])
def download_page():
    return render_template('download/index.html')



_cache_data = None
_cache_time = 0
CACHE_TTL = 600  # 10分钟

@maple_bp.route('/download_url', methods=['GET'])
def download_url():
    global _cache_data, _cache_time
    now = time.time()

    # 缓存有效：直接返回
    if _cache_data and (now - _cache_time < CACHE_TTL):
        return jsonify(_cache_data)
    try:
        result_data, debug_info, message = MapleService.get_download_info()
        _cache_data = {
            "status": "success" if result_data else "warning",
            "data": result_data,
            "message": message,
            "debug_info": debug_info
        }
    except Exception as ex:
        logging.error("Failed to get download info: {}".format(ex))
    _cache_time = now
    return jsonify(_cache_data)