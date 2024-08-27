from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
from datetime import datetime, timedelta
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_service = Service('./chromedriver')

# URLs to monitor
urls = [
    "https://x.io/",
    "https://y.io/",
    "https://z.io/"
]

# Duration of monitoring (2 days)
duration = timedelta(days=3)
# Interval between checks (1 hour)
interval = timedelta(hours=0.5)

# End time for the monitoring
end_time = datetime.now() + duration

# CSV file to store results
csv_file = "monitoring_results_dev.csv"

# Check if the CSV file already exists
file_exists = os.path.isfile(csv_file)

# Write headers to the CSV file if it doesn't exist
if not file_exists:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "URL", "Load Time (s)", "Finish Time (s)"])

# Start monitoring
while datetime.now() < end_time:
    for url in urls:
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        start_time = time.time()
        driver.get(url)

        load_time = time.time() - start_time

        time.sleep(5)
        finish_time = time.time() - start_time

        driver.quit()

        # Log the results
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), url, load_time, finish_time])

    # Wait for the next interval
    time.sleep(interval.total_seconds())

print("Monitoring completed.")
