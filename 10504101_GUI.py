import tkinter as tk
import tkinter.messagebox
import random
import urllib.parse, urllib.request, json

baseurl = "https://yang4287.github.io/ENGLISH/%E8%8B%B1%E6%96%87%E5%96%AE%E5%AD%97.json"
result = urllib.request.urlopen(baseurl).read().decode("utf-8-sig")

dict = json.loads(result)
new_dict = {v : k for k, v in dict.items()}

def SearchPage():
    search.tkraise()    
def Home():
    home.tkraise()

def TestPage_Eng():#英翻中頁面
    testE.tkraise()
    
def TestPage_Chin():#中翻英頁面
    testC.tkraise()  
def MissPage():
    file = open('record.txt','r')
    data_list = file.readlines()
    file.close()
    scrolly=tkinter.Scrollbar(miss)
    scrolly.grid(row=2,column=2,pady=5)
    mylb=tkinter.Listbox(miss,yscrollcommand=scrolly.set,width=50,height=5)
    mylb.grid(row=2,column=2,pady=5)
    
    list_MissCount=[]
    
    for n in data_list:
        n = n.strip()
        ch=n.split(',')[0]
        list_MissCount.append(ch)
        
    dict_MissCount={}
    dict_MissCount= dict_MissCount.fromkeys(list_MissCount)   
    for m in list_MissCount:
        dict_MissCount[m]=list_MissCount.count(m)
        
    for w,c in dict_MissCount.items():#w是單字的中文意思，c是答錯次數
        mylb.insert(tkinter.END,w+","+new_dict[w]+"------"+str(c))
        
    scrolly.config(command=mylb.yview)
    miss.tkraise()
def SearchResult():
    word=searchinput.get()
    if word in dict:
        tk.messagebox.showinfo("中文意思為:", message=dict[word])

    else:
        tk.messagebox.showinfo("錯誤:", message='抱歉無這個單字')
        
def Start_Chin():#中翻英
    word=random.choice(list(dict.keys()))
    testCinput1.delete(0, tk.END)
    testCinput.delete(0, tk.END)
    testCinput.insert(0,dict[word])
    
def Start_Eng():#英翻中
    word=random.choice(list(dict.keys()))
    testEinput.delete(0, tk.END)
    testEinput1.delete(0, tk.END)
    testEinput1.insert(0,word)
    
def TestResult_Chin():#中翻英
    Chin=testCinput.get()
    Eng=testCinput1.get()
    if Eng in dict.keys() and Chin==dict[Eng]:
        tk.messagebox.showinfo("結果", message='恭喜答對')
    else:
        tk.messagebox.showinfo("結果", message='答錯，答案是:'+new_dict[Chin])
        file = open('record.txt', 'a')
        file.write(Chin + ',' +new_dict[Chin])
        file.write("\n")
        file.close()

def TestResult_Eng():#英翻中
    Chin1=testEinput.get()
    Eng1=testEinput1.get()
    if Chin1 in dict[Eng1].split(";"):
        tk.messagebox.showinfo("結果", message='恭喜答對')
    else:
        tk.messagebox.showinfo("結果", message='答錯，答案是:'+dict[Eng1])
        file = open('record.txt', 'a')
        file.write(dict[Eng1]+ ',' +Eng1)
        file.write("\n")
        file.close()

    

window = tk.Tk()
window.title("單字小學堂")
window.geometry("400x200")
container = tk.Frame(window)
container.grid(row=1,column=1)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)


home = tk.Frame(container)

homeButton = tk.Button(home, text="查單字", command=SearchPage)
homeButton.grid(row=1,column=1,pady=10)
homeButton2 = tk.Button(home, text="英翻中測驗", command=TestPage_Eng)
homeButton2.grid(row=1,column=2,pady=10)
homeButton3 = tk.Button(home, text="中翻英測驗", command=TestPage_Chin)
homeButton3.grid(row=1,column=3,pady=10)
homeButton4 = tk.Button(home, text="易錯單字區", command=MissPage)
homeButton4.grid(row=1,column=4,pady=10)
homeLabel = tk.Label(home, text="歡迎來到"+"\n"+"單字小學堂",fg = "blue")
homeLabel.grid(row=2,column=3,pady=10)

home.grid(row=0, column=0, sticky="nsew")


search = tk.Frame(container)
searchButton = tk.Button(search, text="首頁", command=Home)
searchButton.grid(row=1,column=1,pady=10)
searchLabel = tk.Label(search, text="請輸入要查詢的英文單字:")
searchLabel.grid(row=2,column=2,pady=10)
searchinput=tk.Entry(search, text="")
searchinput.grid(row=2,column=3)
searchButton = tk.Button(search, text="查詢", command=SearchResult)
searchButton.grid(row=3,column=3, pady=10)
search.grid(row=0, column=0, sticky="nsew")

testC = tk.Frame(container)
testCButton = tk.Button(testC, text="首頁", command=Home)
testCButton.grid(row=1,column=1,pady=10)
testCLabel = tk.Label(testC, text="中文意思:")
testCLabel.grid(row=2,column=2,padx=20,pady=10)
testCinput=tk.Entry(testC, text="")
testCinput.grid(row=2,column=3)
testCLabel1 = tk.Label(testC, text="英文單字:")
testCLabel1.grid(row=3,column=2,padx=20,pady=10)
testCinput1=tk.Entry(testC, text="")
testCinput1.grid(row=3,column=3)
testCButton2 = tk.Button(testC, text="開始", command=Start_Chin)
testCButton2.grid(row=4,column=3, pady=10)
testCButton3 = tk.Button(testC, text="結果", command=TestResult_Chin)
testCButton3.grid(row=4,column=4)
testC.grid(row=0, column=0, sticky="nsew")


testE = tk.Frame(container)
testEButton = tk.Button(testE, text="首頁", command=Home)
testEButton.grid(row=1,column=1,pady=10)
testELabel = tk.Label(testE, text="中文意思:")
testELabel.grid(row=2,column=2,padx=20,pady=10)
testEinput=tk.Entry(testE, text="")
testEinput.grid(row=2,column=3)
testELabel1 = tk.Label(testE, text="英文單字:")
testELabel1.grid(row=3,column=2,padx=20,pady=10)
testEinput1=tk.Entry(testE, text="")
testEinput1.grid(row=3,column=3)
testEButton2 = tk.Button(testE, text="開始",command=Start_Eng)
testEButton2.grid(row=4,column=3, pady=10)
testEButton3 = tk.Button(testE, text="結果", command=TestResult_Eng)
testEButton3.grid(row=4,column=4)
testE.grid(row=0, column=0, sticky="nsew")




miss = tk.Frame(container)
missButton = tk.Button(miss, text="首頁", command=Home)
missButton.grid(row=1,column=1,pady=10)
miss.grid(row=0, column=0, sticky="nsew")

home.tkraise()
window.mainloop()