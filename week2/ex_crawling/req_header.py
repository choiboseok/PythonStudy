import requests

url = "https://www.oxfordlearnersdictionaries.com/definition/english/subject_1?q=subject"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
# header 정보를 체크하는 사이트
res = requests.get(url, headers=header) # 헤더 정보 추가
print(res.status_code)
