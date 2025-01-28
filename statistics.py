import requests
import wikipedia


# Function to search and retrieve article info
def wikipedia_result(search_result):
    search_results = wikipedia.search(search_result)
    print("Search Results:", search_results)

    try:
        # Get the content of an article
        page = wikipedia.page(search_result)
        article = page.title
        summary = page.summary
        url = page.url
        print(f"Title: {article}")
        print(f"Summary: {summary}")
        print(f"URL: {url}")
        return article, url

    except Exception as e:
        print(f"Error: {e}")
        return None, None


# Function to get statistics using Wikipedia Page views API
def get_statistics(url, article, search_result):
    print(f"Fetching statistics for article: {article} from URL: {url}")

    # Extract article title from URL (assuming standard Wikipedia URL structure)
    start_date = "20240101"
    end_date = "20250128"

    # Page views API endpoint with a fixed date range (2024-01-01 to 2025-01-28)
    page_views_url = url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/{search_result}/daily/{start_date}/{end_date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }
    # Make the request to the API
    response = requests.get(page_views_url,headers=headers )

    if response.status_code == 200:
        data = response.json()
        # Sum the views over all the available data
        views = sum(item['views'] for item in data['items'])
        print(f"Total Views for {article}: {views}")
    else:
        print(f"Error: {response.status_code}")


# Main function
def main():
    search_result = "Python programming"

    article, url = wikipedia_result(search_result)

    if article and url:
        get_statistics(url, article, search_result)  # Call to get statistics
    else:
        print("Failed to retrieve article information.")


if __name__ == '__main__':
    main()
