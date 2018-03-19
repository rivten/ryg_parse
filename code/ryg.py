import requests
from html.parser import HTMLParser

#####################################
class month_html_parser(HTMLParser):
    #PrintData = False
    PrintCount = 10
    FoundMonthDiv = False
    InsideArticleList = False
    StopParsing = False
    ArticleLinkList = []

    def handle_starttag(self, tag, attrs):

        if(tag == 'div' and ('class', 'entries') in attrs):
            #self.PrintData = True
            self.FoundMonthDiv = True
            self.StopParsing = False
            #print("Start tag : ", tag, " -- Attributes : ", attrs)

        if(self.StopParsing):
            return

        if(self.FoundMonthDiv and tag == 'li'):
            self.InsideArticleList = True
        if(self.InsideArticleList and tag == 'a'):
            ArticleLink = attrs[0][1]
            self.ArticleLinkList.insert(0, ArticleLink)

    def handle_endtag(self, tag):
        if(self.InsideArticleList and tag == 'li'):
            self.StopParsing = True
        #print("End tag : ", tag)

    def handle_data(self, data):
        pass
        #if(self.PrintData == True and (self.PrintCount != 0)):
            #print("Data : ", data)
            #self.PrintCount -= 1
###################################################################

def ParseArticle(ArticleLink):
    print(ArticleLink);

def ParseMonth(Year, Month):
    Website = 'https://fgiesen.wordpress.com/' + str(Year) + '/' + str(Month).zfill(2) + '/'
    HttpRequest = requests.get(Website);
    MonthHtmlParser = month_html_parser()
    MonthHtmlParser.feed(HttpRequest.text)
    # TODO(hugo): For a reason that I do not understand,
    # the object MonthHtmlParser is not destroyed
    # at the end of this scope (and the list keeps accumulating)
    for ArticleLink in MonthHtmlParser.ArticleLinkList :
        ParseArticle(ArticleLink)
    print("End of ", Year, " ", Month)

ParseMonth(2018, 2)
ParseMonth(2012, 6)


