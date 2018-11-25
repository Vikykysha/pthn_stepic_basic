'''Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.'''

# put your python code here
import re
import requests
def find_links(pattern,s):
    return re.findall(pattern,s)
two_step = False
url1 =input()

pattern = r'<a.*href=\"([^\"]*)\"'

res1 = requests.get(url1)
if res1.status_code == 200:
    url2 = input()
    for link in find_links(pattern, res1.text):
        res = requests.get(link)
        if res.status_code == 200:
            for lin in find_links(pattern, res.text):
                if lin == url2:
                    two_step = True
                    break
            if two_step:
                break
print('Yes' if two_step else 'No')