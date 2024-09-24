# Name:  Jonathan Ho
# Project:  Web Application Scraper


import sys
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup




#Extracts all links from the HTML content of a given URL
def get_links(url):
    try:
        response = requests.get(url)   #Sends a GET request to the URL
        content_type = response.headers.get("content-type", "").lower()

        if "text/html" in content_type or "text/css" in content_type or "application/javascript" in content_type:
            soup = BeautifulSoup(response.content, "html.parser")   #Parses the HTML content

            links = set()   #Sets to store the extracted links

            for link in soup.find_all("a"):
                href = link.get("href")
                if href:
                    links.add(href)

            for script in soup.find_all("script"):
                src = script.get("src")
                if src:
                    links.add(src)

            for link in soup.find_all("link"):
                href = link.get("href")
                if href:
                    links.add(href)

            for img in soup.find_all("img"):
                src = img.get("src")
                if src:
                    links.add(src)

            #Filter out None values and empty links
            links = [link for link in links if link]

            return links

        #Returns the list of links
        return []

    except requests.exceptions.RequestException:
        #Returns an empty list if there's an error during the request
        return []


#Checks if a given URL is an internal link within the specified domain
def is_internal_link(domain, url):
    parsed_url = urlparse(url)

    #Compares the netloc (domain) of the URL with the specified domain
    return (parsed_url.netloc == domain)


def scrape_links(domain, url, depth, visited=set(), unique_links=set()):
    #Base cases:
    #  - If the depth is negative-----------------
    #             OR                             |----> Return and stop scraping the website
    #  - If the URL has already been visited------
    if depth < 0 or url in visited:
        return

    #Mark the URL as visited to not revisit the site (OR ELSE will cause an infinite loop)
    visited.add(url)

    #Check if the URL is an internal link within the specified domain
    if is_internal_link(domain, url):
        #Get all links from the URL
        links = get_links(url)

        #Append the URL to the output file
        with open("output.txt", "a") as file:
            #Recursively scrape each link found within the URL
            for link in links:
                absolute_url = urljoin(url, link)

                if absolute_url.startswith(url):
                    parsed_url = urlparse(absolute_url)
                    formatted_link = parsed_url.netloc + parsed_url.path if parsed_url.netloc else parsed_url.path

                    if formatted_link not in unique_links:
                        unique_links.add(formatted_link)
                        file.write(formatted_link + "\n")

        for link in links:
            absolute_url = urljoin(url, link)

            if absolute_url.startswith(url):
                #Decrease the depth by 1 and continue scraping recursively
                scrape_links(domain, absolute_url, depth - 1, visited, unique_links)


def main():        
    #Validate command-line arguments
    if len(sys.argv) != 4:
        print("Invalid number of arguments.")
        print("Usage:  python3 web_scraper.py <domain> <starting_url> <depth>")
        print("   EX:  python3 .\web_scraper.py stackoverflow.com https://stackoverflow.com 3")

        return

    #Retrieves the command-line arguments / user inputs
    domain = sys.argv[1]
    starting_url = sys.argv[2]
    depth = int(sys.argv[3])

    #Clears the content of the output file
    with open("output.txt", "w") as file:
        file.write("")

    #Appends metadata to the output file to inform the user what command-line arguments they utilized
    with open("output.txt", "a") as file:
        file.write("# Domain:  " + domain + "\n" +
                   "# URL:  " + starting_url + "\n" +
                   "# Depth:  " + str(depth) + "\n\n\n")
    
    #Prints out to display the user's input
    print("============= USER INPUT =============")
    print("# Domain:  " + domain + "\n" +
          "# URL:  " + starting_url + "\n" +
          "# Depth:  " + str(depth) + "\n")
    
    #Calls/executes this scrape_links() function  |  Starts scraping links
    scrape_links(domain, starting_url, depth)

    #Prints out this statement  |  Informs the user that the scraping is completed with the results stored in the output.txt file
    print("Web scraping completed ---> Results saved in output.txt\n")


if __name__ == "__main__":
    main()
