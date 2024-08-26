import requests

S = requests.Session()
URL = "https://ja.wikipedia.org/w/api.php"

# APIパラメータの設定
PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "images",
    "titles": "エマ・ワトソン"  # 取得したい記事のタイトル
}

# APIリクエストの送信
R = S.get(url=URL, params=PARAMS)
DATA = R.json()

# 画像情報の抽出
PAGE = next(iter(DATA["query"]["pages"].values()))
IMAGES = PAGE["images"]

# 画像タイトルの表示
for image in IMAGES:
    print(image["title"])

# 画像URLの取得（追加のリクエストが必要）
for image in IMAGES:
    if image["title"].lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        IMAGE_PARAMS = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "iiprop": "url",
            "titles": image["title"]
        }
        IMAGE_R = S.get(url=URL, params=IMAGE_PARAMS)
        IMAGE_DATA = IMAGE_R.json()
        IMAGE_PAGE = next(iter(IMAGE_DATA["query"]["pages"].values()))
        print(IMAGE_PAGE["imageinfo"][0]["url"])