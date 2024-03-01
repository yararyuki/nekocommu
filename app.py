from flask import Flask, render_template, session, request, redirect, url_for
import mysql.connector
from datetime import timedelta
from PIL import Image
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import random
import string
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "心がカギ"
app.permanent_session_lifetime = timedelta(hours=24)
app.config["MAX_CONTENT_LENGTH"] = 8**20
Extension = set(["png", "jpg", "gif"])


# Gmailの設定
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "nekocommu@gmail.com"
app.config["MAIL_PASSWORD"] = "aeqy wxkm rkki cksr"
app.config["MAIL_DEFAULT_SENDER"] = "nekoco.mmu@gmail.com"

mail = Mail(app)


class DbOP:
    def __init__(self, table):
        self.__host = "localhost"
        self.__user = "nekocommu"
        self.__passwd = "neko"
        self.__db = "nekocommu"
        self.__table = table

        self.__con = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            passwd=self.__passwd,
            db=self.__db,
        )

    def selectAll(self):
        print("selectAll************************************************")

        sql = "SELECT * FROM " + self.__table + ";"
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # HOME画面用
    def homePost(self):
        print("homePost************************************************")

        sql = "SELECT post.* ,user.profile_image FROM post INNER JOIN user ON post.id = user.id ORDER BY post_id DESC;"
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # 検索処理POST
    def searchPost(self, search):
        print("searchPost************************************************")

        sql = (
            "SELECT post.* ,user.profile_image FROM post INNER JOIN user ON post.id = user.id WHERE post.detail LIKE '%"
            + search
            + "%' ORDER BY RAND();"
        )
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # 検索処理USER
    def searchUser(self, search):
        print("searchUser************************************************")

        sql = (
            "SELECT id,profile_image FROM user WHERE id LIKE '%"
            + search
            + "%' ORDER BY RAND();"
        )
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # ログイン
    def Login(self, mail):
        print("LOGIN************************************************")

        sql = 'SELECT * FROM user WHERE mail ="' + mail + '";'
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # ユーザーデータ抽出
    def user(self, id):
        print("USER************************************************")

        sql = 'SELECT * FROM user WHERE id ="' + id + '";'
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # 新規登録ID重複チェック
    def idCheck(self):
        print("IDCHECK************************************************")

        sql = "SELECT id FROM user ;"
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # ユーザーごと投稿抽出
    def postUser(self, id):
        print("POSTUSER************************************************")

        sql = 'SELECT * FROM post WHERE id ="' + id + '";'
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # 投稿単体抽出
    def postSolo(self, id):
        print("POSTSOLO************************************************")

        sql = 'SELECT * FROM post WHERE post_id ="' + id + '";'
        print(sql)

        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    # コメント送信
    def update(self, comment, post_id):

        sql = (
            "UPDATE `"
            + self.__table
            + "` SET `comment` = '"
            + comment
            + "' WHERE post_id = "
            + post_id
            + ""
        )
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        cur.close()

    # コメントだけ取り出す
    def commentTbl(self, post_id):
        sql = (
            "SELECT comment FROM " + self.__table + " WHERE post_id = " + post_id + ";"
        )
        print(sql)
        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()

    # 寄付ポイント処理
    def point(self, post_id, point, user_id, my_id):
        sql = (
            "UPDATE post SET post_point = post_point +"
            + point
            + " WHERE POST_ID ="
            + post_id
            + ";"
        )
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        sql = (
            "UPDATE user SET point = point +" + point + " WHERE ID ='" + user_id + "';"
        )
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        sql = (
            "UPDATE user SET pointAll = pointAll +"
            + point
            + " WHERE ID ='"
            + user_id
            + "';"
        )
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        sql = "UPDATE user SET point = point -" + point + " WHERE ID ='" + my_id + "';"
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        cur.close()

    # コミット
    def commit(self, sql):
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        cur.close()

    # DB接続＆絞込条件抽出
    def selectEx(self, ex):

        sql = "SELECT * FROM " + self.__table + " WHERE" + ex + ";"
        print(sql)
        cur = self.__con.cursor(dictionary=True)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()

        # ２次元配列の０行目（１件）のみを返す
        return res[0]

    # DB接続＆データ挿入
    def insTbl(self, val):
        sql = "INSERT INTO " + self.__table + " VALUES("
        sql += val
        sql += ",'');"
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        cur.close()

    # DB接続＆データ削除
    def delTbl(self, re):
        sql = "DELETE FROM " + self.__table + " WHERE"
        sql += re
        sql += ";"
        print(sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        cur.close()

    # DB切断
    def close(self):
        self.__con.close()


@app.route("/")
def home():
    session.pop("mail", None)
    try:
        dbop = DbOP("post")
        result = dbop.homePost()
        dbop.close()

        if "userId" in session:
            icon = session["userIcon"]
            id = session["userId"]
            dbop = DbOP("user")
            userpoint = dbop.user(id)
            dbop.close()
            for poi in userpoint:
                point = poi["point"]
                session["userPoint"] = point
            return render_template(
                "home.html", result=result, icon=icon, point=point, id=id
            )

        return render_template("home.html", result=result)

    except mysql.connector.errors.ProgrammingError as e:
        print("***DB接続エラー***")
        print(type(e))
        print(e)
    except Exception as e:
        print("***システム運行プログラムエラー***")
        print(type(e))
        print(e)


@app.route("/user")
def user():
    if "userId" in session:
        try:
            id = session["userId"]
            icon = session["userIcon"]
            point = session["userPoint"]

            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            dbop = DbOP("user")
            result = dbop.user(id)
            post_date = dbop.postUser(id)
            dbop.close()
            for rec in result:
                pointAll = rec["pointAll"]
                tag = rec["tag_name"]

            pointAll = f"{pointAll:,}"
            if " " in tag:
                tag_tbl = tag.split(" ")
            else:
                tag_tbl = {tag}
                print(tag_tbl)

            return render_template(
                "myprofile.html",
                result=result,
                icon=icon,
                point=point,
                pointAll=pointAll,
                tag_tbl=tag_tbl,
                post_date=post_date,
            )

        except mysql.connector.errors.ProgrammingError as e:
            print("***** DB接続エラー *****")
            print(type(e))
            print(e)
        except Exception as e:
            print("***** システム運行プログラムエラー *****")
            print(type(e))
            print(e)
    else:
        test = {}
        return render_template("login.html", test=test)


@app.route("/post")
def post():
    if "userId" in session:
        try:
            id = session["userId"]
            icon = session["userIcon"]
            point = session["userPoint"]
            dbop = DbOP("user")
            result = dbop.user(id)
            dbop.close()
            print("44444444444447878787878")
            for rec in result:
                tag = rec["tag_name"]
                print(tag)
            if " " in tag:
                tag_tbl = tag.split(" ")
                print(tag_tbl)

            else:
                tag_tbl = {tag}
                print(tag_tbl)

            return render_template(
                "post.html",
                result=result,
                icon=icon,
                id=id,
                point=point,
                tag_tbl=tag_tbl,
            )
        except mysql.connector.errors.ProgrammingError as e:
            print("***** DB接続エラー *****")
            print(type(e))
            print(e)
        except Exception as e:
            print("***** システム運行プログラムエラー *****")
            print(type(e))
            print(e)
    else:
        test = {}
        return render_template("login.html", test=test)


@app.route("/loginCheck", methods=["POST"])
def loginCheck():
    try:
        result = {}
        test = request.form
        mail = test["mail"]
        err = ""
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        dbop = DbOP("user")
        result = dbop.Login(mail)
        dbop.close()

        if not result:
            err = "メールアドレスまたはパスワードが違います"
            return render_template("login.html", err=err, test=test)
        for rec in result:
            print(rec["pass"])
            id = rec["id"]
            icon = rec["profile_image"]
            point = rec["point"]
        if not test["pass"] == rec["pass"]:
            err = "メールアドレスまたはパスワードが違います"
            return render_template("login.html", result=result, err=err, test=test)

        session["userId"] = id
        session["userIcon"] = icon
        session["userPoint"] = point
        dbop = DbOP("post")
        result = dbop.homePost()
        dbop.close()
        return render_template(
            "home.html", id=id, result=result, icon=icon, point=point
        )

    except mysql.connector.errors.ProgrammingError as e:
        print("***** DB接続エラー *****")
        print(type(e))
        print(e)
    except Exception as e:
        print("***** システム運行プログラムエラー *****")
        print(type(e))
        print(e)


@app.route("/signup")
def signup():

    return render_template("signup.html")


@app.route("/signupMail", methods=["POST"])
def signupMail():
    result = request.form
    to_email = result["mail"]
    subject = "ねここみゅアカウント新規登録確認メール"

    # 画像を "static" フォルダ内に保存しておく
    # img_path = "./static/furniture_mail.jpg"

    body = render_template("email_template.html", to_email=to_email)

    message = Message(subject=subject, recipients=[to_email], html=body)

    mail.send(message)
    return render_template("signupMail.html", to_email=to_email)


@app.route("/signupSetting/<mail>")
def signupSetting(mail):
    session["mail"] = mail
    name = ""
    id = ""
    if "name" in session:
        name = session["name"]
        id = session["id"]
    return render_template("signupSetting.html", name=name, id=id)


@app.route("/signupCheck", methods=["POST"])
def signupCheck():
    mail = session["mail"]
    result = request.form
    err = ""

    if not result["pass"] == result["pass2"]:

        return render_template("signupSetting.html", result=result)

    try:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        dbop = DbOP("user")
        idCheck = dbop.idCheck()
        dbop.close()
        if result["id"] in idCheck:
            return render_template("signupSetting.html", result=result, err=err)
        session["name"] = result["name"]
        session["id"] = result["id"]
        session["pass"] = result["pass"]
        return render_template("signupCheck.html", result=result, mail=mail)

    except mysql.connector.errors.ProgrammingError as e:
        print("***** DB接続エラー *****")
        print(type(e))
        print(e)
    except Exception as e:
        print("***** システム運行プログラムエラー *****")
        print(type(e))
        print(e)


@app.route("/signupComplete", methods=["POST"])
def signupComplete():
    result = session.copy()
    sql = (
        "'"
        + result["id"]
        + "','"
        + result["name"]
        + "','"
        + result["mail"]
        + "','"
        + result["pass"]
        + "','"
        "','"
        "'"
    )

    try:
        dbop = DbOP("user")
        dbop.insTbl(sql)
        dbop.close()
        session.pop("id", None)
        session.pop("name", None)
        session.pop("pass", None)
        return render_template("home.html")

    except mysql.connector.errors.ProgrammingError as e:
        print("***** DB接続エラー *****")
        print(type(e))
        print(e)
    except Exception as e:
        print("***** システム運行プログラムエラー *****")
        print(type(e))
        print(e)


@app.route("/signout")
def signout():
    session.clear()
    return render_template("signout.html")


@app.route("/searchArea", methods=["GET"])
def searchArea():
    if "userId" in session:
        icon = session["userIcon"]
        point = session["userPoint"]
        return render_template("search.html", icon=icon, point=point)

    return render_template("search.html")


@app.route("/search", methods=["GET"])
def search():
    search = request.args.get("search")
    print(search)
    try:
        dbop = DbOP("post")
        resultPost = dbop.searchPost(search)
        print(resultPost)
        dbop = DbOP("user")
        resultUser = dbop.searchUser(search)
        print(resultUser)
        dbop.close()

        if "userId" in session:
            icon = session["userIcon"]
            point = session["userPoint"]
            return render_template(
                "search.html",
                resultPost=resultPost,
                resultUser=resultUser,
                icon=icon,
                point=point,
            )
        return render_template(
            "search.html", resultPost=resultPost, resultUser=resultUser
        )

    except mysql.connector.errors.ProgrammingError as e:
        print("***** DB接続エラー *****")
        print(type(e))
        print(e)
    except Exception as e:
        print("***** システム運行プログラムエラー *****")
        print(type(e))
        print(e)


@app.route("/donation/<post_id>/<number>", methods=["POST"])
def donation(post_id, number):

    print(number)
    if "userId" in session:
        point = session["userPoint"]
        if number == "1":
            toggle = 1

            try:
                dbop = DbOP("post")
                result = dbop.postSolo(post_id)
                print(result)

                return render_template(
                    "donation.html",
                    toggle=toggle,
                    post_id=post_id,
                    result=result,
                    point=point,
                )

            except mysql.connector.errors.ProgrammingError as e:
                print("***** DB接続エラー *****")
                print(type(e))
                print(e)
            except Exception as e:
                print("***** システム運行プログラムエラー *****")
                print(type(e))
                print(e)

        elif number == "2":
            toggle = 2
            resultPoint = request.form["resultPoint"]
            print(resultPoint)
            my_id = session["userId"]
            try:
                dbop = DbOP("post")
                result = dbop.postSolo(post_id)
                for rec in result:
                    user_id = rec["id"]

                dbop = DbOP("post")
                dbop.point(post_id, resultPoint, user_id, my_id)

                return render_template(
                    "donation.html",
                    toggle=toggle,
                    post_id=post_id,
                    result=result,
                    point=point,
                )

            except mysql.connector.errors.ProgrammingError as e:
                print("***** DB接続エラー *****")
                print(type(e))
                print(e)
            except Exception as e:
                print("***** システム運行プログラムエラー *****")
                print(type(e))
                print(e)
    # elif number==3:

    else:
        test = {}
        return render_template("login.html", test=test)


@app.route("/upload", methods=["POST"])
def upload():
    if "userId" in session:
        id = session["userId"]
        icon = session["userIcon"]
        point = session["userPoint"]
        vtbl = {"file": "写真", "detail": "詳細", "tag_name": "タグ"}

        # ***結果格納TBL***
        result = {}
        # ***エラー受信***
        errmsg = {}

        # ***データ受信***
        result = request.form
        # ***空白・未入力チェック***
        err_cnt = 0
        for key, value in result.items():
            if not value:
                errmsg[key] = vtbl[key] + "が入力されていません"
                err_cnt += 1
            else:
                errmsg[key] = ""

        print("********************空白**********")
        # ***画像ファイル名チェック***
        # if 'file' not in request.files:
        #     return print('No file part')
        file = request.files["file"]
        fileName = file.filename
        print(fileName)
        if fileName:
            if not extension_check(fileName):
                print("ファイルの容量が多い")

        # ***画像加工＆保存処理***

        try:
            # ***保存日時作成
            savedata = datetime.now().strftime("%Y%m%d_%H%M%S_")
            # ***安全な保存ファイル名作成
            fileName = id + savedata + secure_filename(fileName)

            # ***保存ファイル名作成
            save_path1 = os.path.join("./static/images/post/", fileName)
            print("***保存された*********")
            print(fileName)

            # ***画像ファイル名を開く
            img = Image.open(file)

            # ***画像ファイル保存
            img.save(save_path1, quality=90)
        except FileNotFoundError as e:
            print("*****画像ファイル処理エラー*****")
            print(type(e))
            print(e)
            errmsg = {
                "msg1": "画像ファイル処理エラー",
                "msg2": "ファイルの保存に失敗しました",
            }
            return render_template(
                "post.html",
                result=result,
                icon=icon,
                id=id,
                point=point,
            )

        except Exception as e:
            print("*****システム運航プログラムエラー*****")
            print(type(e))
            print(e)
        # INSERT SQL(val)
        print(result)
        sql = (
            "'','"
            + id
            + "','"
            + fileName
            + "','','"
            + result["detail"]
            + "','"
            + result["tag_name"]
            + "'"
        )
        try:
            dbop = DbOP("post")
            print(sql)
            dbop.insTbl(sql)
            dbop.close()

            # 結果出力処理
            return redirect("/")
            # return render_template("home.html",
            #     result=result,
            #     icon=icon,
            #     id=id,
            #     point=point)

        except mysql.connector.errors.ProgrammingError as e:
            print("DB接続エラー")
            print(type(e))
            print(e)
        except Exception as e:
            print("システム運行プログラムエラー")
            print(type(e))
            print(e)
            print("++++++++++++++++++++++++++++++++++++++++")
    else:
        test = {}
        return render_template("login.html", test=test)


@app.route("/comment/<post_id>", methods=["POST"])
def comment(post_id):
    if "userId" in session:
        try:
            result = request.form.get("comment")
            print(result)
            dbop = DbOP("post")
            comment = dbop.commentTbl(post_id)
            dbop.close()
            # なんでとれへんのかわからん
            print(comment)
            if comment is not None:
                result = comment + result
            else:
                result = result

            dbop = DbOP("post")
            dbop.update(result, post_id)
            dbop.close()
            # 結果出力処理
            return redirect("/")
        except mysql.connector.errors.ProgrammingError as e:
            print("DB接続エラー")
            print(type(e))
            print(e)
        except Exception as e:
            print("システム運行プログラムエラー")
            print(type(e))
            print(e)
            print("++++++++++++++++++++++++++++++++++++++++")
    else:
        test = {}
        return render_template("login.html", test=test)


@app.route("/profile/<number>", methods=["POST"])
def profile(number):
    print(number)
    if "userId" in session:
        if number == "1":
            toggle = 1
            return render_template("profileUp.html", toggle=toggle)
        elif number == "2":
            toggle = 2
            name = request.form["name"]
            detail = request.form["detail"]
            my_id = session["userId"]
            print(name)

            # ***ファイルオブジェクト取得***
            file = request.files["file"]

            filename = file.filename
            # ***ファイル受信チェック***
            if not filename:
                sql = (
                    'UPDATE user SET name= "'
                    + name
                    + '", profile_detail = "'
                    + detail
                    + '" WHERE id = "'
                    + my_id
                    + '";'
                )
                print(sql)
                try:
                    dbop = DbOP("user")
                    dbop.commit(sql)
                    dbop.close()
                except mysql.connector.errors.ProgrammingError as e:
                    print("***DB接続エラー***")
                    print(type(e))
                    print(e)
                except Exception as e:
                    print("***システム運行プログラムエラー***")
                    print(type(e))
                    print(e)

            else:
                directory_path = "static/images/icon/"
                file_name = session["userIcon"]
                file_path = os.path.join(directory_path, file_name)
                if not file_name == "unknownUser.jpg":
                    os.remove(file_path)

                # ***ファイルオープン***
                rec = extension_check(filename)
                if rec == "True":
                    img = Image.open(file)
                    img = crop_max_square(img)
                    # ***日時情報の取得***
                    savedate = datetime.now().strftime("%Y%m%d_%H%M%S_")
                    # ***安全なファイル名に変換***
                    filename = savedate + secure_filename(filename)
                    # ***保存用フルパス作成***
                    os.path.join("./static/images/icon", filename)
                    save_path = os.path.join("./static/images/icon", filename)
                    # ***ファイル保存***

                    img.save(save_path, quality=90)

                icon = filename
                sql = (
                    'UPDATE user SET name = "'
                    + name
                    + '", profile_image = "'
                    + icon
                    + '", profile_detail = "'
                    + detail
                    + '" WHERE id = "'
                    + my_id
                    + '";'
                )
                print(sql)
                try:
                    dbop = DbOP("user")
                    dbop.commit(sql)
                    dbop.close()
                    session["icon"] = icon
                    return render_template("profileUp.html", toggle=toggle)
                except mysql.connector.errors.ProgrammingError as e:
                    print("***DB接続エラー***")
                    print(type(e))
                    print(e)
                except Exception as e:
                    print("***システム運行プログラムエラー***")
                    print(type(e))
                    print(e)

    else:
        test = {}
        return render_template("login.html", test=test)


def extension_check(filename):

    # ***ドット検出
    if "." in filename:
        # ***ドットで分割（右から１回のみ分割）
        strtbl = filename.rsplit(".", 1)
        # ***拡張子のみを取得
        ext = strtbl[1]

        # ***拡張子を小文字に変換
        ext = ext.lower()
        # ***拡張子が許可されているか
        if ext in Extension:
            return 1

    return 0


def image_reduction(img, maxsize):

    # ***新サイズ算出（maxsizeを超えた場合のみ処理）
    if img.width > maxsize or img.height > maxsize:

        if img.width >= img.height:
            width = maxsize
            height = int(img.height * (width / img.width))
        else:
            height = maxsize
            width = int(img.width * (height / img.height))

        # ***画像をリサイズする
        img = img.resize((width, height))

    return img


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(
        (
            (img_width - crop_width) // 2,
            (img_height - crop_height) // 2,
            (img_width + crop_width) // 2,
            (img_height + crop_height) // 2,
        )
    )


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


if __name__ == "__main__":
    app.run(debug=True)
