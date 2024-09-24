# Web-Application-Scraper

A web scraper is a powerful tool that automates the process of extracting and collecting data from websites. It navigates through web pages, accesses their HTML content, and retrieves pertinent information, such as text and links. Web scrapers are commonly used for various purposes, including data analysis, content aggregation, market research, and security assessments, particularly in identifying vulnerabilities on web applications.

## How `web_scraper.py` Works

The `web_scraper.py` script is designed to perform a systematic and recursive retrieval of unique internal links from a specified domain based on user-defined criteria. Here’s a breakdown of how the script operates:
1. **Input Handling:** Accepts three command-line arguments: domain, starting URL, and depth, validating the input before proceeding.
2. **Initialization:** Clears the output.txt file and logs user input details at the beginning of the output.
3. **Link Extraction:** The scrape_links() function recursively fetches and parses links from the specified URL using get_links(), which employs requests and BeautifulSoup.
4. **Recursive Exploration:** Identifies and records unique internal links while ensuring duplicates are avoided; stops when the depth limit is reached.
5. **Output Generation:** Writes discovered links to output.txt and notifies the user upon completion.

## Setup and Installation

To set up the environment for the web scrper, ensure you have the following packages installed:

### Prerequisites

* Python 3.x
  * Strongly recommend Python3+ due to some inconsistencies in the 2.7 versions of packages (i.e. use "python3" and "pip3" to run [since Python 2 is long dead](https://www.python.org/doc/sunset-python-2/)).
* Install the necessary libraries:
  * [Requests](http://docs.python-requests.org/en/latest/)  |  [urllib3](https://github.com/urllib3/urllib3)  |  [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
  * **Commands:**
    * `pip3 install requests`
    * `pip3 install urllib3`
    * `pip3 install beautifulsoup4`
  * **NOTE:**	If you tried to run the program and get an error like this below:
    *ModuleNotFoundError: No module named 'mechanicalsoup'*
    Simply run this command to resolve the issue:  `python3 -m pip install mechanicalsoup`

## Python Script Execution Examples

`python3 .\web_scraper.py 127.0.0.1 http://127.0.0.1/dvwa/ 3`

`python3 .\web_scraper.py stackoverflow.com https://stackoverflow.com 3`

**Script Format/Outline:**

`python3 .\web_scraper.py [DOMAIN] [URL] [DEPTH]`
