import requests
import time

def fetch_item_page(url, proxies_list, retries, backoff_factor):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    for attempt in range(retries):
        proxy = proxies_list[attempt % len(proxies_list)]
        proxies = {
            'http': proxy,
            'https': proxy
        }
        print(f"Attempting to fetch page with proxy: {proxy}. Attempt {attempt + 1} of {retries}.")
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                print("Page fetched successfully.")
                return response.text
            elif response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    sleep_time = int(retry_after)
                else:
                    sleep_time = backoff_factor * (2 ** attempt)
                print(f"Rate limited. Sleeping for {sleep_time} seconds...")
                time.sleep(sleep_time)
        except requests.exceptions.ProxyError as e:
            print(f"Proxy error: {e}. Retrying with next proxy...")
        except requests.exceptions.ConnectTimeout:
            print(f"Connection timed out with proxy: {proxy}. Retrying with next proxy...")
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}. Retrying...")
    print(f"Failed to fetch page after {retries} attempts.")
    raise Exception(f"Failed to fetch page after {retries} attempts")
