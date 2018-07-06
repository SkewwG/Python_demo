# 返回网址
import newspaper

qq_paper = newspaper.build('http://www.chinanews.com/')       # 返回构造的原对象， 而不是文章的下载或者解析

# for article in qq_paper.articles:                 # 获取文章地址
#     print(article.url)

for category in qq_paper.category_urls():           # 获取子域
    print(category)

'''
C:\Python36\python36.exe C:/Users/Asus/Desktop/py/demo/Python_demo/demo_newspaper/demo_build_articles.py
http://xxgk.nankai.edu.cn/2014/1229/c2762a13403/page.htm
http://xxgk.nankai.edu.cn/2018/0622/c2780a102620/page.htm
http://xxgk.nankai.edu.cn/2018/0705/c2780a103934/page.htm
http://xxgk.nankai.edu.cn/2018/0705/c2780a103935/page.htm
http://xxgk.nankai.edu.cn/2018/0705/c2780a103936/page.htm
http://xxgk.nankai.edu.cn/2018/0704/c2780a103874/page.htm
http://xxgk.nankai.edu.cn/2014/1217/c2781a12406/page.htm
http://xxgk.nankai.edu.cn/2014/1217/c2781a12405/page.htm
http://xxgk.nankai.edu.cn/2014/1217/c2781a12404/page.htm
http://nankai.en.school.cucas.cn/en/news?cid=16&pid=16
http://nankai.en.school.cucas.cn/en/article?cid=96&pid=58&spid=57
http://nankai.en.school.cucas.cn/en/gallery?cid=25&pid=25&spid=1
http://nankai.en.school.cucas.cn/en/article?cid=30&pid=29&spid=2
http://nankai.en.school.cucas.cn/en/article?cid=3&pid=3
http://nankai.en.school.cucas.cn/en/article?cid=40&pid=40&spid=4
http://nankai.en.school.cucas.cn/en/article?cid=70&pid=41&spid=4
http://nankai.en.school.cucas.cn/en/article?cid=94&pid=42&spid=4
http://nankai.en.school.cucas.cn/en/article?cid=68&pid=43&spid=4
http://nankai.en.school.cucas.cn/en/article?cid=44&pid=44&spid=4
http://nankai.en.school.cucas.cn/en/article?cid=72&pid=48&spid=5
http://nankai.en.school.cucas.cn/en/article?cid=49&pid=49&spid=5
http://nankai.en.school.cucas.cn/en/article?cid=53&pid=53&spid=6
http://nankai.en.school.cucas.cn/en/gallery?cid=64&pid=64&spid=61
http://nankai.en.school.cucas.cn/en/article?cid=76&pid=65&spid=61
http://nankai.en.school.cucas.cn/en/news/detail?cid=132&pid=16&spid=0&detail=1539
http://nankai.en.school.cucas.cn/en/news/detail?cid=131&pid=16&spid=0&detail=1530
http://nankai.en.school.cucas.cn/en/news/detail?cid=130&pid=16&spid=0&detail=1532
http://nankai.en.school.cucas.cn/en/news/detail?cid=16&pid=16&spid=0&detail=1491
http://nankai.en.school.cucas.cn/en/news/detail?cid=16&pid=16&spid=0&detail=1464
http://nankai.en.school.cucas.cn/en/news/detail?cid=16&pid=16&spid=0&detail=1545
http://nankai.en.school.cucas.cn/en/news/detail?cid=16&pid=16&spid=0&detail=1543
http://nankai.en.school.cucas.cn/en/news/detail?cid=16&pid=16&spid=0&detail=1542
http://nankai.en.school.cucas.cn/en/article/detail?cid=96&pid=58&spid=57&detail=1393
http://nankai.en.school.cucas.cn/en/article/detail?cid=98&pid=58&spid=57&detail=1546
http://nankai.en.school.cucas.cn/en/article/detail?cid=60&pid=58&spid=57&detail=1490
http://nankai.en.school.cucas.cn/en/article/detail?cid=76&detail=206&spid=61&pid=61
http://www.lib.nankai.edu.cn/news/tzgg
http://www.lib.nankai.edu.cn/news/tzgg/1100.html
http://www.lib.nankai.edu.cn/news/tzgg/1098.html
http://www.lib.nankai.edu.cn/news/tzgg/1088.html
http://www.lib.nankai.edu.cn/news/tzgg/1086.html
http://www.lib.nankai.edu.cn/news/tzgg/1101.html
http://www.lib.nankai.edu.cn/news/tzgg/1099.html
http://www.lib.nankai.edu.cn/news/tzgg/1097.html
http://nkuef.nankai.edu.cn/c/news.html
http://nkuef.nankai.edu.cn/c/news
http://www.nankai.edu.cn/2018/0620/c159a102463/page.htm
http://www.nankai.edu.cn/2018/0622/c157a102620/page.htm
http://www.nankai.edu.cn/2018/0705/c157a103934/page.htm
http://www.nankai.edu.cn/2018/0705/c157a103935/page.htm
http://www.nankai.edu.cn/2018/0705/c157a103936/page.htm
http://www.nankai.edu.cn/2018/0704/c157a103874/page.htm
http://www.nankai.edu.cn/2018/0625/c5697a102756/page.htm
http://www.nankai.edu.cn/2018/0624/c5697a102671/page.htm
http://www.nankai.edu.cn/2018/0621/c5697a102536/page.htm

Process finished with exit code 0

'''


'''
C:\Python36\python36.exe C:/Users/Asus/Desktop/py/demo/Python_demo/demo_newspaper/demo_build_articles.py
http://news.nankai.edu.cn
http://xxgk.nankai.edu.cn
http://news.nankai.edu.cn/
http://zsb.nankai.edu.cn
http://xuebao.nankai.edu.cn
http://nkuaa.nankai.edu.cn
http://bbs.nankai.edu.cn
http://nankai.en.school.cucas.cn
http://www.lib.nankai.edu.cn
http://nkuef.nankai.edu.cn
http://www.nankai.edu.cn

Process finished with exit code 0

'''