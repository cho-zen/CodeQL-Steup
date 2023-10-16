import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://www.onlinesbi.sbi/"
    data = fetch_data(url)
    print(data)


'''
In this code, the requests library is used to make HTTP requests. If the project depends on a version of requests that
contains a known security vulnerability, CodeQL can identify this as a security issue.
'''
