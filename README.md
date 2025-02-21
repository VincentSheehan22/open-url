# open-url
`open-url` defines a Python script to open single URL or multiple URLs in the default browser, based on the `webbrowser` module from the Python Standard Library.

`open_url.py` defines two functions - `open_url()` and `open_url_list()`. 
* `open_url()` takes a single URL string as input and uses as input for `webbrowser.open()`, open as a new tab in the default browser.
* `open_url_list()` takes a list of URL strings as input, and for each URL in the list, calls `open_url()`.

URLs or URL lists are defined as variables, and functions called with these variables as input.
