import json
import requests
from pathlib import Path
from setting import headers, url, data


def post(path="Path to wav or mp3 file"):
    files = {'file': open(path, "rb")}
    response = requests.post(url, data=data, headers=headers, files=files)
    result = json.loads(response.text)
    your_id = result['public_id']
    url1 = f"{url}/{your_id}"
    while True:
        response1 = requests.get(url1, headers=headers)
        result1 = json.loads(response1.text)
        if result1["status"] == "finished":
            break
    text = str(result1["results"]["neuralspace"]["text"])
    text = text.replace("ʻ", "'")
    text = text.replace("ʼ", "'")
    file_name = Path(path).stem
    with open(f"{file_name}.txt", mode="w") as file:
        file.write(text)
    return result1['results']["neuralspace"]["text"]


def main():
    i = post()
    print(i)


if __name__ == '__main__':
    main()
