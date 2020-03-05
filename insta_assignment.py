import requests
import webbrowser

# https://www.instagram.com/developer/embedding/
like_lion_URL = 'https://api.instagram.com/oembed'
jpg_url = 'https://instagram.com/p/B8OBL7BDEpL/media'

# URL 파라미터 'param', 이미지 출력 파라미터 'size_img'
param = {'url': 'https://www.instagram.com/p/B8OBL7BDEpL/'}
size_img = 'l'

# 메인 contents 출력
# ? 여기서 json이렇게 쓰는게 맞는것인지.. 원리가 잘 이해가 가지 않습니다.
info_like_lion = requests.get(like_lion_URL, params=param)
contents = info_like_lion.json()
print(contents['title'])


# 이미지 출력
# ? 사이즈를 위에서 l로 설정하였는데도, t,m,l간에 차이가 없이 나타납니다.
jpg_like_lion = requests.get(jpg_url, params=size_img)
webbrowser.open(jpg_like_lion.url)
