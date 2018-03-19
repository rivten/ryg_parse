import requests
from html.parser import HTMLParser

#print("Hello, sailor");

#Website = 'https://fgiesen.wordpress.com/2009/10/'
Website = 'https://fgiesen.wordpress.com/2018/02/'
HttpRequest = requests.get(Website);
#print(HttpRequest.text)


class month_html_parser(HTMLParser):
    PrintData = False
    PrintCount = 10
    FoundMonthDiv = False
    InsideArticleList = False
    StopParsing = False

    def handle_starttag(self, tag, attrs):

        if(tag == 'div' and ('class', 'entries') in attrs):
            self.PrintData = True
            self.FoundMonthDiv = True
            self.StopParsing = False
            #print("Start tag : ", tag, " -- Attributes : ", attrs)

        if(self.StopParsing):
            return

        if(self.FoundMonthDiv and tag == 'li'):
            self.InsideArticleList = True
        if(self.InsideArticleList and tag == 'a'):
            ArticleLink = attrs[0][1]
            print(ArticleLink)

    def handle_endtag(self, tag):
        if(self.InsideArticleList and tag == 'li'):
            self.StopParsing = True
        #print("End tag : ", tag)

    def handle_data(self, data):
        pass
        #if(self.PrintData == True and (self.PrintCount != 0)):
            #print("Data : ", data)
            #self.PrintCount -= 1

MonthHtmlParser = month_html_parser()

MonthHtmlParser.feed(HttpRequest.text)
