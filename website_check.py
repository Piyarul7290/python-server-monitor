
import time
import requests

url = input("Enter website URL: ").strip()

if not url.startswith(("https://", "http://")):
    url = "https://" + url

try:
    start = time.perf_counter()
    response = requests.get(url, timeout=10)
    elapsed = (time.perf_counter() - start) * 1000

    print("\nWEBSITE HEALTH REPORT")
    print("---------------------")
    print("Website:", url)
    print("HTTP Status:", response.status_code)
    print(f"Response Time: {elapsed:.2f} ms")

    if 200 <= response.status_code < 400:
        print("Website Status: AVAILABLE")
    else:
        print("Website Status: CHECK REQUIRED")

except requests.RequestException as error:
    print("Website Status: UNREACHABLE")
    print("Reason:", error)
