# Description:

This Python script monitors website loading times for a specified duration and interval. It utilizes Selenium with a headless Chrome browser to automate the process and generates a CSV file containing timestamps, URLs, load times, and finish times.

## Installation:

Python: Ensure you have Python installed on your system.
Selenium: Install Selenium using pip install selenium.
ChromeDriver: Download the appropriate ChromeDriver version for your Chrome browser from "https://developer.chrome.com/docs/chromedriver/downloads" and place it in the same directory as this script (./chromedriver).
## Usage:

Modify URLs: Update the urls list within the script to include the specific websites you want to monitor.
Customize Duration & Interval: Adjust the duration and interval variables to define the monitoring period and frequency of checks.
Run Script: Run the script using python your_script_name.py.
Output:

The script will create a CSV file named monitoring_results_dev.csv. It contains columns for timestamp, URL, load time (seconds), and finish time (seconds).

## Notes:

This script runs in headless mode, meaning the Chrome browser won't be visible.
The script uses a basic example for monitoring. You might need to adjust it based on specific website functionalities or complex page loading processes.
Consider adding error handling for potential exceptions during website loading.
Additional Information:

For further customization, refer to the Selenium documentation:

 https://www.selenium.dev/documentation/
