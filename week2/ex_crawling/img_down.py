import urllib.request as req

url = 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000089/89475/89475_320.jpg'
req.urlretrieve(url, 'test.png') # url로 이미지 다운로드
