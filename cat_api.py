import requests
from typing import Optional

def get_random_cat_image() -> Optional[str]:
    """
    Делает запрос к TheCatAPI для получения случайного изображения кошки.
    Возвращает URL изображения или None при ошибке.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and data and 'url' in data[0]:
                return data[0]['url']
        return None
    except Exception:
        return None
