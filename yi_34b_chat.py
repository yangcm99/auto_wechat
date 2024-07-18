import requests
import json
from auto_wechat import base_config
import KEY_FILE

API_KEY = KEY_FILE.API_KEY
SECRET_KEY = KEY_FILE.SECRET_KEY


def yi_34b_chat_main(content, role):
    url = base_config.llm_url + get_access_token()
    # print(type(content))
    # print(type(role))
    # print(role)
    # print(content)

    payload = json.dumps({
        "temperature": 0.95,
        "top_p": 0.7,
        "penalty_score": 1,
        "messages": [
            {
                "role": role,
                "content": content
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # 将响应转换为JSON格式的字典
    response_json = response.json()
    # 获取result部分
    result = response_json.get('result')
    # 打印result

    result_str = str(result)
    # print(result_str)

    return result_str


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    # print('密钥获取:' + str(requests.post(url, params=params).json().get("access_token")))
    return str(requests.post(url, params=params).json().get("access_token"))
