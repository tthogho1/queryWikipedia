import wikipedia
import requests

# 英語版Wikipediaを使用するように設定
wikipedia.set_lang("en")

def get_tourist_attractions(query, num_results=5):
    try:
        # 観光地を検索
        search_results = wikipedia.search(query, results=num_results)
        
        for title in search_results:
            try:
                # 記事ページを取得
                page = wikipedia.page(title)
                
                print(f"Title: {page.title}")
                print(f"URL: {page.url}")
                print(f"Summary: {page.summary[:200]}...")  # 最初の200文字のみ表示
                print(f"Content: {page.content}")
                
                # 画像を取得（最初の3枚のみ）
                print("Images:")
                for i, image_url in enumerate(page.images[:3]):
                    print(f"- {image_url}")
                    
                print("\n---\n")
                
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Disambiguation page: {title}. Possible options: {e.options[:5]}")
            except wikipedia.exceptions.PageError:
                print(f"Page not found: {title}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# 世界の観光地について検索
get_tourist_attractions("famous tourist attractions")