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
    PreviousArticleCount = len(MonthHtmlParser.ArticleLinkList)
    Website = 'https://fgiesen.wordpress.com/' + str(Year) + '/' + str(Month).zfill(2) + '/'
    HttpRequest = requests.get(Website);
    if(HttpRequest.status_code == 200):
        MonthHtmlParser.feed(HttpRequest.text)
        print("End of ", Year, " ", Month)
    else:
        print(HttpRequest)
    if(len(MonthHtmlParser.ArticleLinkList) - PreviousArticleCount == 7):
        print("7 articles ! Hum ?")

MonthHtmlParser = month_html_parser()
ParseMonth(2018, 3)
ParseMonth(2018, 2)
ParseMonth(2018, 1)

ParseMonth(2017, 12)
ParseMonth(2017, 11)
ParseMonth(2017, 10)
ParseMonth(2017, 9)
ParseMonth(2017, 8)
ParseMonth(2017, 7)
ParseMonth(2017, 6)
ParseMonth(2017, 5)
ParseMonth(2017, 4)
ParseMonth(2017, 3)
ParseMonth(2017, 2)
ParseMonth(2017, 1)

ParseMonth(2016, 12)
ParseMonth(2016, 11)
ParseMonth(2016, 10)
ParseMonth(2016, 9)
ParseMonth(2016, 8)
ParseMonth(2016, 7)
ParseMonth(2016, 6)
ParseMonth(2016, 5)
ParseMonth(2016, 4)
ParseMonth(2016, 3)
ParseMonth(2016, 2)
ParseMonth(2016, 1)

ParseMonth(2015, 12)
ParseMonth(2015, 11)
ParseMonth(2015, 10)
ParseMonth(2015, 9)
ParseMonth(2015, 8)
ParseMonth(2015, 7)
ParseMonth(2015, 6)
ParseMonth(2015, 5)
ParseMonth(2015, 4)
ParseMonth(2015, 3)
ParseMonth(2015, 2)
ParseMonth(2015, 1)

ParseMonth(2014, 12)
ParseMonth(2014, 11)
ParseMonth(2014, 10)
ParseMonth(2014, 9)
ParseMonth(2014, 8)
ParseMonth(2014, 7)
ParseMonth(2014, 6)
ParseMonth(2014, 5)
ParseMonth(2014, 4)
ParseMonth(2014, 3)
ParseMonth(2014, 2)
ParseMonth(2014, 1)

ParseMonth(2013, 12)
ParseMonth(2013, 11)
ParseMonth(2013, 10)
ParseMonth(2013, 9)
ParseMonth(2013, 8)
ParseMonth(2013, 7)
ParseMonth(2013, 6)
ParseMonth(2013, 5)
ParseMonth(2013, 4)
ParseMonth(2013, 3)
ParseMonth(2013, 2)
ParseMonth(2013, 1)

ParseMonth(2012, 12)
ParseMonth(2012, 11)
ParseMonth(2012, 10)
ParseMonth(2012, 9)
ParseMonth(2012, 8)
ParseMonth(2012, 7)
ParseMonth(2012, 6)
ParseMonth(2012, 5)
ParseMonth(2012, 4)
ParseMonth(2012, 3)
ParseMonth(2012, 2)
ParseMonth(2012, 1)

ParseMonth(2011, 12)
ParseMonth(2011, 11)
ParseMonth(2011, 10)
ParseMonth(2011, 9)
ParseMonth(2011, 8)
ParseMonth(2011, 7)
ParseMonth(2011, 6)
ParseMonth(2011, 5)
ParseMonth(2011, 4)
ParseMonth(2011, 3)
ParseMonth(2011, 2)
ParseMonth(2011, 1)

ParseMonth(2010, 12)
ParseMonth(2010, 11)
ParseMonth(2010, 10)
ParseMonth(2010, 9)
ParseMonth(2010, 8)
ParseMonth(2010, 7)
ParseMonth(2010, 6)
ParseMonth(2010, 5)
ParseMonth(2010, 4)
ParseMonth(2010, 3)
ParseMonth(2010, 2)
ParseMonth(2010, 1)

ParseMonth(2009, 12)
ParseMonth(2009, 11)
ParseMonth(2009, 10)
ParseMonth(2009, 9)
ParseMonth(2009, 8)
ParseMonth(2009, 7)
ParseMonth(2009, 6)
ParseMonth(2009, 5)
ParseMonth(2009, 4)
ParseMonth(2009, 3)
ParseMonth(2009, 2)
ParseMonth(2009, 1)

# TODO(hugo): For a reason that I do not understand,
# the object MonthHtmlParser is not destroyed
# at the end of this scope (and the list keeps accumulating)
for ArticleLink in MonthHtmlParser.ArticleLinkList :
    ParseArticle(ArticleLink)


