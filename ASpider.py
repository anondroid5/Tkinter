#coding: UTF-8

from Tkinter import *
import os,time,urllib,tkFileDialog,tkMessageBox
root=Tk()# windowオブジェクト
root.title(u"ASpider v1.2.0")
root.resizable(False, False)
root.configure(background = '#a72944')

#メニューを生成する関数の定義
def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="切り取り")
    the_menu.add_command(label="コピー")
    the_menu.add_command(label="貼り付け")

#メニューを表示する関数の定義
def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("切り取り", command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("コピー", command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("貼り付け", command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

#メニュー生成関数の実行
make_menu(root)
root.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
urltext=StringVar()

f1=LabelFrame(root, text = "探索設定",bg ='#a72944', bd=2, relief=GROOVE)
Label(f1,text=u"サイトURL:", bg ='#a72944').grid(row=0, column=0)
Entry(f1,textvariable=urltext,bg ='#a72944',fg='black',width=40).grid(row=0, column=1,padx=10,pady=5)


f2=LabelFrame(root, text = "詳細設定",bg ='#a72944', bd=2, relief=GROOVE)
check=IntVar()
Radiobutton(f2, text="幅256px以上",width=10,variable=check,value = 0,bg ='#a72944').grid(row=0,column=0)
Radiobutton(f2, text="幅512px以上",width=10,variable=check,value = 1,bg ='#a72944').grid(row=0,column=1)
Radiobutton(f2, text="幅1024px以上",width=10,variable=check,value = 2,bg ='#a72944').grid(row=0,column=2)
pagetext=IntVar()#ページ数
Label(f2,text=u"ページ数", bg ='#a72944').grid(row=0,column=3)
Spinbox(f2, from_ = 1, to = 500, increment = 1, bg ='#a72944',textvariable=pagetext, width = 4).grid(row=0, column=4)
#ディレクトリ変更
path_name=""
filename=""
cu=""

#保存ディレクトリの選択用
def hozon():
    global path_name,file_name,cu
    cu=os.getcwd()
    filename = tkFileDialog.askdirectory(title="カレントディレクトリ:"+cu+"\nディレクトリを選択してください",initialdir = path_name)
    if filename != "":
        path_name = os.path.dirname(filename)
        os.chdir(filename)

Label(f1,text=u"画像保存先:",bg ='#a72944').grid(row=1, column=0)
Button(f1,text="ディレクトリ選択",width=40, bg ='#a72944',activebackground='#c61e42',cursor='spider',command=hozon).grid(row=1, column=1,padx=10,pady=5)
f3 = LabelFrame(root, text = "実行履歴", bg ='#a72944', bd=2, relief = GROOVE)
# Listbox の生成
lb = Listbox(f3,width=52,height=17,bg='black',fg='white')
# Scrollbar の生成
sb1 = Scrollbar(f3, orient = 'v', command = lb.yview)
sb2 = Scrollbar(f3, orient = 'h', command = lb.xview)
# Listbox の設定
lb.configure(yscrollcommand = sb1.set)
lb.configure(xscrollcommand = sb2.set)
lb.insert(END, "*"* 15 + "実行履歴を表示する領域" + "*" * 15)
lb.insert(END, "※履歴を実行中はフリーズして見ることはできません＼(~o~)／")


#スクレイピングする関数
def scrape(htmlurl):
#--------------------------<html>タグ全体の取得--------------------------------
	htmlfile = urllib.urlopen(htmlurl)
	htmltext = htmlfile.read() # html全体の取得
	lb.insert(END, u"[実行結果]")
	print u"[実行結果]"
	lb.insert(END, u"対象URL:" + htmlurl)
	print u"[対象URL:]" + htmlurl
#--------------------------<img>タグ内URLの取得--------------------------------
	lb.insert(END, u"<img>タグ内の画像取得開始")
	print u"<img>タグ内の画像取得開始"
	regex = '<img.*?src="(.*?)".*?>'
	pattern = re.compile(regex, re.I)# 大文字小文字の区別をしない
	imgageurl = re.findall(pattern, htmltext)
	save(imgageurl)
#-----------------------------<a>タグ内URLの取得-------------------------------
	lb.insert(END, u"<a>タグ内の画像取得開始")
	print u"<a>タグ内の画像取得開始"
	regex = '<a.*?href="(https?://[^"]+\.jpg|\.jpeg|\.png|\.gif)".*?>'
	pattern = re.compile(regex,re.I)
	aurl = re.findall(pattern, htmltext)
	save(aurl)
	htmlfile.close()

#画像の保存関数
def save(saveurls):
	for saveurl in saveurls:
		try:
			lb.insert(END, u"保存成功:" + os.path.basename(saveurl))
			image = urllib.urlopen(saveurl)
			localfile = open(os.path.basename(saveurl),'wb')
			print os.path.basename(saveurl)
			localfile.write(image.read())#画像書き込み
			img.close()
			localfile.close()
		except:
			lb.insert(END, u"保存失敗:" + os.path.basename(saveurl))
			
#ダウンロード実行関数
def download():
    if urltext.get():
		for i in range(pagetext.get()):
			if i == 0:
				scrape(urltext.get())
			else:
				scrape(urltext.get() + u"page-" + str(i) + u".html")
    else:
        tkMessageBox.showerror('エラー','URLを入力してください')


Button(root,text="画像取得開始",bg ='#a72944',activebackground='#c61e42',cursor='spider',command=download).pack(side=BOTTOM,pady=3,fill = BOTH)
f1.pack(side=TOP,pady=3)
f2.pack(side=TOP,pady=3,fill = BOTH)
f3.pack(pady=3,expand = True,fill = BOTH)

# grid による配置
lb.grid(row = 0, column = 0, sticky = 'nsew',padx=1)
sb1.grid(row = 0, column = 1, sticky = 'ns',padx=0)
sb2.grid(row = 1, column = 0, sticky = 'ew',padx=1)


root.mainloop()