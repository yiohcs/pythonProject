from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

uri = "https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=19&cat3=&cat4=&fct=&order=date&lastcate=order&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource="

req = Request(uri)
resp = urlopen(req)
html = resp.read()
# print(html[:256 ]) # 코드가 깨지므로 인코딩 변경
html = html.decode("utf-8")
# print(html[:256 ]) # 코드가 정상적이다
# 이제 BeautifulSoup 으로 html 을 정제하자
bs = BeautifulSoup(html,"html.parser")
print(bs.title)
print(bs.title.name)
#이쁘게 표현하자 print(bs.prettify()[:1024])
print()
testCount = 0
list = bs.select(".common_sp_list_ul.ea4>li")
for food in list:
    # 전체 레시피 목록
    titles = food.select(".common_sp_thumb>a")

    for title in titles:
        uri2 = title['href']
        uri2 = 'https://www.10000recipe.com'+uri2
        print(uri2)
        # 레시피 주소
        req2 = Request(uri2)
        resp2 = urlopen(req2)
        html2 = resp2.read()
        html2 = html2.decode("utf-8")
        bs2 = BeautifulSoup(html2, "html.parser")
        # 레시피 리스트 목록
        list2 = bs2.select(".container.sub_bg")

        for container in list2:
            # 메인 썸네일
            img = container.select("#main_thumbs")
            print(img[0]['src'])

            # 재료
            ingredient = container.select(".ready_ingre3>ul")
            cnt = 0
            for i1 in ingredient:
                # 재료 제목
                bTag = i1.select("b")
                print(bTag[0].text, end=' ')
                aTag = i1.select("a")
                for i2 in aTag:
                    # 재료 목록
                    str1 = i2.text.replace(" ", "")
                    str1 = str1.replace('\n', "")
                    print(str1, end=' ')
                print('&')

            view_step = container.select(".view_step")
            btt = view_step[0].select(".best_tit>b")
            print(btt[0].text)

            media = view_step[0].select(".view_step_cont")
            for md in media:
                t = md.select(".media-body")
                print(t[0].text)
                r = md.select("img")
                try:
                    print(r[0]['src'])
                except:
                    print("")
        print()
    testCount += 1
    if testCount >= 3:
        break
