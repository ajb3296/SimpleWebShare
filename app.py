import os
from urllib import parse
from flask import Flask, render_template, request, send_file, abort

from config import main_path, port, title, black_list, log


app = Flask(__name__)

@app.route("/")
def index():
    # 블랙리스트 차단
    if request.remote_addr in black_list:
        abort(403)  # Forbidden

    vpath = request.args.get('path', "/")
    if vpath == "":
        vpath = "/"
    vpath = parse.unquote(vpath)
    path = vpath.split("/")
    goodpath = []
    for i in path:
        if i != ".." or i != "":
            goodpath.append(i)

    # 뒤로가기용 경로
    print("/".join(goodpath[:-2]))
    back_path = "/" + "/".join(goodpath[:-2]) + "/"
    # 메인 경로
    printpath = "/".join(goodpath)
    # 전체 경로
    path = main_path + "/" + "/".join(goodpath)

    back_path = back_path.replace("//", "/").replace("//", "/").replace(" ", "+")
    path = path.replace("//", "/").replace("//", "/")
    printpath = printpath.replace("//", "/").replace("//", "/")

    if not os.path.exists(path):
        abort(404)

    files = []
    folders = []

    for file in os.listdir(path):
        if os.path.isdir(path+"/"+file):
            if file[0] != ".":
                folders.append(file)
        else:
            if file[0] != ".":
                files.append(file)

    # 정렬
    folders.sort()
    files.sort()

    return render_template("index.html", 
                            url = request.url_root, # URL (ex. https://127.0.0.1 )
                            title_url = request.host,
                            port = port, # 포트
                            vpath = printpath, # 출력용 경로
                            path = path, # 전체 경로 
                            back_path = back_path, # 뒤로가기 경로
                            folderlist = folders, # 폴더 리스트
                            files = files, # 파일 리스트
                            title = title, # 타이틀
                            os = os, # os 모듈
                            version = version # 버전
                            )

@app.route("/download/")
def download():
    # 블랙리스트 차단
    if request.remote_addr in black_list:
        abort(403)  # Forbidden

    vpath = request.args.get('path', "/")
    if vpath == "":
        vpath = "/"
    vpath = parse.unquote(vpath)
    path = vpath.split("/")
    goodpath = []
    for i in path:
        if i != "..":
            goodpath.append(i)
    # 메인 경로
    printpath = "/".join(goodpath)
    # 전체 경로
    path = main_path + "/" + "/".join(goodpath)

    path = path.replace("///", "/").replace("//", "/")
    printpath = printpath.replace("///", "/").replace("//", "/")

    if not os.path.isfile(path):
        abort(404)

    if log:
        if not os.path.exists("log.txt"):
            file = open("log.txt", "w", encoding = 'UTF-8')
        else:
            file = open("log.txt", "a", encoding = 'UTF-8')
        file.write(f"Download - {request.remote_addr} - File: {path}\n")
        file.close()

    return send_file(path,
                     attachment_filename=goodpath[-1], # 다운받아지는 파일 이름. 
                     as_attachment=True)


# 404 ERROR 처리
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", url = request.host, port = port, title = title, error = error, version = version), 404

if __name__ == '__main__':
    version = "V 1.0.0"
    app.run(debug=True, host='0.0.0.0', port = str(port), threaded=True)