import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class FinwizNews:
    def __init__(self, company_array, count_of_news, first_run=False):
        self.finwiz_url = "https://finviz.com/quote.ashx?t="
        self.company_array = company_array
        self.count_of_news = count_of_news
        if first_run:
            nltk.downloader.download('vader_lexicon')

    def __news_tables(self):
        news_dict = dict()
        for company in self.company_array:
            url = self.finwiz_url + company
            req = Request(url=url, headers={'user-agent': 'chromedriver'})
            resp = urlopen(req)
            html = BeautifulSoup(resp, features="lxml")

            news_table = html.find(id='news-table')
            news_dict[company] = news_table

        return news_dict

    def recently_news(self):
        for company in self.company_array:
            df = self.__news_tables()[company]
            df_tr = df.findAll('tr')

            print('\n')
            print('Recent News Headlines for {}: '.format(company))

            for i, table_row in enumerate(df_tr):
                a_text = table_row.a.text
                a_href = table_row.a.get('href')
                td_text = table_row.td.text

                td_text = td_text.strip()
                print(i, a_text, '(', td_text, ')', a_href)
                sia = SentimentIntensityAnalyzer()
                sentiment_analyze = sia.polarity_scores(a_text)['compound']
                if sentiment_analyze > 0:
                    print("Positive: ", sentiment_analyze)
                if sentiment_analyze < 0:
                    print("Negative: ", sentiment_analyze)
                if sentiment_analyze == 0:
                    print("Neutral")  # Ниже я описал ход решения проблемы с нейтральной оценки новости


                print()
                if i == self.count_of_news - 1:
                    break


if __name__ == "__main__":
    company_array = ['AAPL', 'TSLA', 'AMZN']
    finwiz_news = FinwizNews(company_array, 5)
    finwiz_news.recently_news()


    #  Так же из дополнение к этому проекту сделать просмотр страниц новостей и сделать оценку целой новости по данному алгоритму
    #  тк используются разные веб ресурсы (не один сайт). Я бы реализововал через dict который составлял бы +- 10
    #  объектов и для каждого этого объекта прописал бы свой web scrapping, а если на этапе проектировки сайт не добавлен добавить его в log для дальнейшего добаввление в dict

