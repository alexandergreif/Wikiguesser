import wikipedia

# import main


# Function to search and retrieve article info
def get_article():
    title = wikipedia.random()
    try:
        summary = wikipedia.summary(title, sentences=1, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError:
        summary = "No summary available."
    except wikipedia.exceptions.PageError:
        return get_article()

    url = wikipedia.page(title).url
    print(title)
    return title, summary, url
#
#
# # Function to get statistics using Wikipedia Page views API
# def get_statistics(url, article, search_result):
#     print(f"Fetching statistics for article: {article} from URL: {url}")
#
#     # Extract article title from URL (assuming standard Wikipedia URL structure)
#     start_date = "20240101"
#     end_date = "20250128"
#
#     # Page views API endpoint with a fixed date range (2024-01-01 to 2025-01-28)
#     page_views_url = url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/{search_result}/daily/{start_date}/{end_date}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#         "Accept": "application/json"
#     }
#     # Make the request to the API
#     response = requests.get(page_views_url,headers=headers )
#
#     if response.status_code == 200:
#         data = response.json()
#         # Sum the views over all the available data
#         views = sum(item['views'] for item in data['items'])
#         print(f"Total Views for {article}: {views}")
#     else:
#         print(f"Error: {response.status_code}")
#
#
# # Main function
# def main():
#     search_result = "Python programming"
#
#     article, url = wikipedia_result(search_result)
#
#     if article and url:
#         get_statistics(url, article, search_result)  # Call to get statistics
#     else:
#         print("Failed to retrieve article information.")
#
#
# if __name__ == '__main__':
#     main()

get_article()