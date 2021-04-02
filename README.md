# SimpleWebShare
[![CodeFactor](https://www.codefactor.io/repository/github/newpremium/simplewebshare/badge)](https://www.codefactor.io/repository/github/newpremium/simplewebshare)

간단한 설정으로 순식간에 서버를 여실 수 있어요!

### 참고

[Font Awesome](https://fontawesome.com/v4.7.0/license/)

### 심플 웹쉐어 서버 여는법
1. `config.py` 파일에 아래와 같이 작성하여 저장한다.

```python
# 절대경로
main_path = "공유를 원하는 폴더의 경로"
# 타이틀
title = "SimpleWebShare"
# 다운로드 로그
# True = 다운로드 로그 작성
# False = 다운로드 로그 작성 안함
log = False
# 블랙리스트
# list 형식입니다. ["1234.1234.1234.1234", "5678.5678.5678.5678"] 식으로 추가하시면 됩니다.
black_list = []

port = "5000"
```

2. `start.bat` 혹은 `start.sh` 파일을 이용해 실행한다.
혹은 `python app.py` 명령어를 사용할 수 있다.
3. 포트포워딩을 한다(구글 검색시 많이 나와요!)
4. ip:port 형식으로 접속가능!(ex. 0.0.0.0:5000 )

### Screenshot

<img src="https://github.com/NewPremium/SimpleWebShare/blob/main/images/screenshot.png?raw=true" width="500"></img>