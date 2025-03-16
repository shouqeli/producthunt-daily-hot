import requests
from datetime import datetime, timedelta, timezone
import openai
from bs4 import BeautifulSoup
import pytz
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

try:
    from dotenv import load_dotenv
    # 加载 .env 文件
    load_dotenv()
except ImportError:
    # 在 GitHub Actions 等环境中，环境变量已经设置好，不需要 dotenv
    print("dotenv 模块未安装，将直接使用环境变量")

api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv('BASE_URL')

if not api_key:
    print("警告: 未设置 OPENAI_API_KEY 环境变量，将无法使用 OpenAI 服务")
    client = None
try:
    client = openai.Client(api_key=api_key,base_url=base_url)  # 新版本的客户端初始化方式
    print("成功初始化 OpenAI 客户端")
except Exception as e:
    print(f"初始化 OpenAI 客户端失败: {e}")
    client = None






