import webbrowser

print("CyberBrowser")

url = input("Link: ")

if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

webbrowser.open(url)
