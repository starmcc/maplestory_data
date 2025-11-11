from src.repository.maple_repository import MapleRepository  # 依赖数据访问层
from src.utils.token_utils import extract_csrf_token
import time


class MapleService:
    """业务层：处理“获取下载信息”的完整流程"""

    @staticmethod
    def get_download_info():
        debug_info = []
        result_data = None
        message = "操作成功"

        try:
            get_response, get_debug = MapleRepository.get_download_page()
            debug_info.extend(get_debug)  # 合并调试信息

            delay = 1
            time.sleep(delay)
            debug_info.append(f"GET后延迟{delay}秒（等待JS设置Cookie）")

            csrf_token = extract_csrf_token(get_response.text, get_response.headers)
            debug_info.append(f"提取到CSRF Token：{csrf_token or '未找到'}")

            post_response, post_debug = MapleRepository.post_download_request(csrf_token)
            debug_info.extend(post_debug)

            try:
                result_data = post_response.json()
                debug_info.append("POST响应解析为JSON")
            except ValueError:
                message = "POST响应不是JSON格式"
                debug_info.append(message)

        except Exception as e:
            message = f"业务处理失败：{str(e)}"
            debug_info.append(f"业务异常：{str(e)}")

        return result_data, debug_info, message