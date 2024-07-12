import schedule
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from fetcher import fetch_item_page
from parser import parse_item_details
from generator import generate_data
from database import save_to_db
from utils import load_proxies, load_config, load_item_urls

def process_item(item_url, proxies_list, retries, backoff_factor):
    try:
        print(f"Fetching item page from URL: {item_url}")
        page_content = fetch_item_page(item_url, proxies_list, retries, backoff_factor)
        item_details = parse_item_details(page_content)
        data = generate_data(item_details)
        save_to_db(item_details, data)
        print(f"Item Data:\n{data}")
    except Exception as e:
        print(f"Error processing {item_url}: {e}")

def process_items_concurrently(item_urls, proxies_list, retries, backoff_factor, max_workers):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(process_item, url, proxies_list, retries, backoff_factor): url for url in item_urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error processing {url}: {e}")

def main():
    config_path = "config/config.ini"
    
    # Load proxies from configuration
    proxies_list = load_proxies(config['DEFAULT']['ProxiesFile'])
    
    # Load item URLs from configuration
    item_urls = load_item_urls(config['DEFAULT']['ItemsFile'])
    max_workers = int(config['DEFAULT']['MaxWorkers'])
    retries = int(config['DEFAULT']['Retries'])
    backoff_factor = int(config['DEFAULT']['BackoffFactor'])
    
    # Process items concurrently
    process_items_concurrently(item_urls, proxies_list, retries, backoff_factor, max_workers)

def schedule_tasks():
    config = load_confislacg('config.ini')
    schedule_interval = int(config['DEFAULT']['ScheduleInterval'])
    
    # Schedule the main task to run at the specified interval
    schedule.every(schedule_interval).hours.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_tasks()
