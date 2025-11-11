from src.utils import RequestClient


class MapleRepository:
    # 配置常量（数据访问层专属配置）
    BASE_URL = "https://maplestory.beanfun.com/download?handler=DownloadList"
    FULL_HEADERS = {
        "Host": "maplestory.beanfun.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://maplestory.beanfun.com/download?handler=DownloadList",
        "Origin": "https://maplestory.beanfun.com",
        "Content-Type": "application/json",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"
    }

    @staticmethod
    def get_download_page():
        debug = []
        client = RequestClient.get_instance()
        try:
            debug.append(f"发起GET请求：{MapleRepository.BASE_URL}")
            response = client.get(
                url=MapleRepository.BASE_URL,
                headers=MapleRepository.FULL_HEADERS
            )
            response.raise_for_status()  # 非200抛异常
            debug.append(f"GET响应状态码：{response.status_code}")
            return response, debug
        except Exception as e:
            debug.append(f"GET请求失败：{str(e)}")
            raise  # 抛出异常，由业务层处理

    @staticmethod
    def post_download_request(csrf_token=None):
        """发送POST请求获取数据"""
        debug = []
        client = RequestClient.get_instance()
        try:
            # 构建POST请求头（含Token）
            post_headers = MapleRepository.FULL_HEADERS.copy()
            if csrf_token:
                post_headers["x-csrf-token"] = csrf_token
                debug.append(f"POST请求添加Token：{csrf_token}")

            debug.append(f"发起POST请求：{MapleRepository.BASE_URL}")
            response = client.post(
                url=MapleRepository.BASE_URL,
                headers=post_headers,
                content="{}"
            )
            response.raise_for_status()
            debug.append(f"POST响应状态码：{response.status_code}")
            return response, debug
        except Exception as e:
            debug.append(f"POST请求失败：{str(e)}")
            raise