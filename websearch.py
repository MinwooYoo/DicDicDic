
# for bs4
import urllib.request
import bs4

class WebSearch():
    def __init__(self, url_pre='https://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query=', print_en=True):
        self.url_pre = url_pre
        self.print_en = print_en

    def print(self, txt):
        if self.print_en:
            print(txt)
    def search(self, word):
        self.print("bs4 search! -> " + word)
        url = self.url_pre + word
        html = urllib.request.urlopen(url)  # url 로 연,  html contents
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        word_box = bsObj.find('div', {'class': 'word_num'}).find_all('dd')
        num = (len(word_box))

        s1 = ""
        # print ("Searching word : " , word)
        a = 0
        while a < num:
            s1 = s1 + word_box[a].find('p').get_text()
            # print(word_box[a].find('p').get_text())
            a = a + 1
        return s1

