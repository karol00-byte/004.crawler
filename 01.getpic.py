import requests
from PIL import Image
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}
s=requests.session()

#下載圖片
def download_yzm():
    result=s.get('http://insprod1.tii.org.tw/database/insurance/bmp.asp',headers=headers) #讓人以為是人為在操作
    with open('yzm.jpg','wb') as f:
        f.write(result.content)  #寫入圖片

#識別圖片
def ocr():
    #圖片先進行二值化和灰度化處理
    image=Image.open('yzm.jpg')
    image=Image.convert('L') #灰度
    threshold=127
    table=[]
    for i in range(256):
        if i < 127:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table,'1')
    image.save('yzm.jpg')
    #再次讀取保存後的驗證碼
    with open('yzm.jpg','rb') as f:
        image.read()

    #image.show()
#加入主函數
if __name__=='__main__':
    s.get('http://insprod.tii.org.tw/database/insurance/',headers=headers) #先進到主頁，才找得到驗證碼圖片
    download_yzm()
    #yzm=input("請輸入驗證碼：") #因為要自動化所以忽略
