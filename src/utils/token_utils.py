from bs4 import BeautifulSoup


def extract_csrf_token(html_content, response_headers):
    """提取CSRF Token（纯工具函数，无业务逻辑）"""
    # 从HTML提取
    soup = BeautifulSoup(html_content, "html.parser")
    token_sources = [
        soup.find("meta", attrs={"name": "csrf-token"}),
        soup.find("meta", attrs={"name": "X-CSRF-TOKEN"}),
        soup.find("input", attrs={"name": "__RequestVerificationToken"}),
        soup.find("meta", attrs={"http-equiv": "X-CSRF-TOKEN"})
    ]
    for source in token_sources:
        if source:
            return source.get("content") or source.get("value")

    # 从响应头提取
    for header_key in ["X-CSRF-TOKEN", "AntiForgery-Token"]:
        if header_key in response_headers:
            return response_headers[header_key]

    return None