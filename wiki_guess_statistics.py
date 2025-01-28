import requests
from article_details import get_article

def get_statistics(url, title):
    print(f"Fetching statistics for article: {title} from URL: {url}")

    # Extract article title from URL (assuming standard Wikipedia URL structure)
    start_date = "20240101"
    end_date = "20250128"

    # Page views API endpoint with a fixed date range (2024-01-01 to 2025-01-28)
    # Endpoint: /metrics/unique-devices/{project}/{access}/{granularity}/{start}/{end}
    page_views_url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/{title}/daily/{start_date}/{end_date}"
    page_edit = f"https://wikimedia.org/api/rest_v1/metrics/edits/per-page/en.wikipedia.org/{title}/all-editor-types/daily/{start_date}/{end_date}"

    # simulate a request from a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }
    # Make the request to the API
    response = requests.get(page_views_url, headers=headers)

    # Fetch page views data
    response_views = requests.get(page_views_url, headers=headers)
    if response_views.status_code == 200:
        data_views = response_views.json()
        views = sum(item['views'] for item in data_views['items'])
        print(f"Total Views for {title}: {views}")
    else:
        print(f"Error fetching page views: {response_views.status_code}")

        # Fetch page edits data
    response_edits = requests.get(page_edit, headers=headers)
    if response_edits.status_code == 200:
        data_edits = response_edits.json()
        # print(data_edits)
        edits = sum(result['edits'] for item in data_edits['items'] for result in item['results'])
        print(f"Total Edits for {title}: {edits}")
    else:
        print(f"Error fetching page edits: {response_edits.status_code}")


def main():
    result = get_article()
    url = result[-1]
    title = result[0]
    print(url)

    print(get_statistics(url, title))



if __name__ == '__main__':
    main()