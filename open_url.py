import webbrowser
import time


def open_url(url):
    """Function to open a specific URL, in the default browser."""
    webbrowser.open(url)
    time.sleep(0.8)

def open_url_list(url_list):
    """Function to open a specific set of URLs, in the default browser."""
    for address in url_list:
        open_url(address)

if __name__ == "__main__":
    url = "https://github.com/"
    url_list = ["https://github.com/",
                "https://www.python.org/"]
    
    # Specific URL groups.
    # Pyton documentation.
    python_docs_url_list = ["https://docs.python.org/3/library/webbrowser.html",
                            "https://docs.python.org/3/library/time.html#module-time"]
    
    # Open single URL.
    #open_url(address)
    
    # Open multiple URLs.
    open_url_list(url_list)
    open_url_list(python_docs_url_list)
