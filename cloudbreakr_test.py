import re

#string = '工作完畢後，有時都會抽時間去做gym，但一早化左妝既我，唔怕做到出晒汗溶晒個妝，因為我用左 Esteelauder Double Wear 粉底😛，真正貼服得黎又高度遮瑕，防水防汗，做完gym 影相都唔怕，真正🍩Dont甩🍩🍩😍!!!
#Dont甩粉底🍩
#盡顯不脫本色 #ConfidenceIsBeautiful#DoubleWear#EsteeHK @esteelauder_hk
#kittychoi #蔡佩賢 #sports#gym #2019 #💄
#4wardfitness'

string1 = '''工作完畢後，有時都會抽時間去做gym，但一早化左妝既我，
唔怕做到出晒汗溶晒個妝，因為我用左 Esteelauder Double Wear 粉底😛，
真正貼服得黎又高度遮瑕，防水防汗，做完gym 影相都唔怕，真正🍩Dont甩🍩🍩😍!!!
#Dont甩粉底🍩  #盡顯不脫本色 #ConfidenceIsBeautiful#DoubleWear#EsteeHK
@esteelauder_hk #kittychoi #蔡佩賢 #sports#gym #2019 #💄 #4wardfitness'''
#string = string.encode().decode('utf-8')

string2 = '''你知道氣象局里長什麼樣子嗎？天氣預報怎麼來？#降雨量？#大_水_災/應該怎麼把自己、
寶寶、寵物安全送離水災區？高災區可怎樣防範以儘量降低災後損失？今晚6:30PM，八度空間，
《#謹訓 #8tvALERT》。 @8tvchinese #8TV'''

string3 = '''📌今となっては卒業旅行第1弾だったタイ旅行 ✔️ラン島

#เก็บรักษ์ #ประเทศไทย #ความสามัคคี
#日焼け止め #美白ケア #ビオレUV #アスリズム #日本化粧品検定
#🇹🇭 #thailand
#卒業旅行 #ラン島
#タビジョ #kohlarn '''

#x = re.findall("#[^.#\s]+", string2)
#x = re.findall("#[^\s\u0021-\u002F\u00A1-\u00BC]+", string2)
string = string3.lower()
x = re.findall("#[\w\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff]]+", string)
#x = re.findall("#[^._\s\u0021-\u002F\u003A-\u0040\u00A1-\u00BC\u3000-\u301F\uFF00-\uFFEF]+", string)
print(x)

#[\w\uD83C-\uDBFF\uDC00-\uDFFF\uD83D\uDC00-\uDDFF]
#y = re.findall("#\W+", string)
#x = re.search(r"#\w+", string)


#for i in x:
#    i.encode().decode('utf-8')
#    print(i)
#print(string)
#print(y)
#print("工作")

#for i in x:
#    i.encode()

#print(i)



if(x):
    print("found")
else:
    print("nope")


str = "hello world"

#Check if the string starts with 'hello':

y = re.findall("^hello", str)
if (y):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
