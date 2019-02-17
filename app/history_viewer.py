import webbrowser

if __name__ == "__main__":
    url = "http://www.python.org/"
    # see: https://docs.python.org/3/library/webbrowser.html
    # open_new_tab() defaults to open_new() if necessary
    webbrowser.open_new_tab(url)
