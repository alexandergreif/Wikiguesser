import wikipedia
import requests

# Function to fetch a random Wikipedia article and its summary
def get_article():
    """
    Fetch a random Wikipedia article along with its summary and URL.
    Returns:
        tuple: (title, summary, url)
    """
    while True:
        title = wikipedia.random()
        if "disambiguation" in title:
            continue
        try:
            summary = wikipedia.summary(title, sentences=1, auto_suggest=False)
            break
        except wikipedia.exceptions.PageError:
            continue


    url = wikipedia.page(title).url
    return title, summary, url

def get_statistics(title):
    """
    Fetch page views from Wikimedia API and edits for a given Wikipedia article title.
    Args:
        title (str): The title of the Wikipedia article.
    Returns:
        dict: A dictionary containing page views and edits.
    """
    # Define date range for statistics (modify as needed)
    start_date = "20240101"
    end_date = "20250128"

    # Define API endpoints
    page_views_url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/{title}/daily/{start_date}/{end_date}"
    page_edits_url = f"https://wikimedia.org/api/rest_v1/metrics/edits/per-page/en.wikipedia.org/{title}/all-editor-types/daily/{start_date}/{end_date}"

    # Define headers to simulate a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }

    # Initialize results dictionary
    results = {
        "views": 0,
        "edits": 0
    }

    # Fetch page views
    response_views = requests.get(page_views_url, headers=headers)
    if response_views.status_code == 200:
        data_views = response_views.json()
        results["views"] = sum(item['views'] for item in data_views['items'])
    else:
        print(f"Error fetching page views: {response_views.status_code}")


    return results

if __name__ == "__main__":
    article_title, article_summary, article_url = get_article()
    print(f"Title: {article_title}")
    print(f"Summary: {article_summary}")
    print(f"URL: {article_url}")

    stats = get_statistics(article_title)
    print(f"Statistics: {stats}")
