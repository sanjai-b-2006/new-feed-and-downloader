from tkinter import *
from gnewsclient import gnewsclient
import webbrowser
import requests
def web(link):
        try:
                import pdfkit
                path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
                pdfkit.from_url(link['link'], output_path=link['title'][:20]+'.pdf', configuration=config)
        except OSError:
                import requests
                r = requests.get(link['link'], allow_redirects=True)
                open(link['title'][:20]+'.html', 'wb').write(r.content)
master = Tk()
master.title("NEWS BULLETIN")
master.geometry("2400x720")
master.configure(bg='white')
bg = PhotoImage(file = "News (1).png")
label1 = Label( master, image = bg).pack()

def show():
	label.config( text = clicked.get() )
options = ['Australia', 'Botswana', 'Canada ', 'Ethiopia', 'Ghana', 'India ', 'Indonesia', 'Ireland', 'Israel ', 'Kenya',
 'Latvia', 'Malaysia', 'Namibia', 'New Zealand', 'Nigeria', 'Pakistan', 'Philippines', 'Singapore', 'South Africa',
 'Tanzania', 'Uganda', 'United Kingdom', 'United States', 'Zimbabwe', 'Czech Republic', 'Germany', 'Austria',
 'Switzerland', 'Argentina', 'Chile', 'Colombia', 'Cuba', 'Mexico', 'Peru', 'Venezuela', 'Belgium ', 'France',
 'Morocco', 'Senegal', 'Italy', 'Lithuania', 'Hungary', 'Netherlands', 'Norway', 'Poland', 'Brazil', 'Portugal',
 'Romania', 'Slovakia', 'Slovenia', 'Sweden', 'Vietnam', 'Turkey', 'Greece', 'Bulgaria', 'Russia', 'Ukraine ',
 'Serbia', 'United Arab Emirates', 'Saudi Arabia', 'Lebanon', 'Egypt', 'Bangladesh', 'Thailand', 'China', 'Taiwan',
 'Hong Kong', 'Japan', 'Republic of Korea']
clicked = StringVar()
clicked.set( "CHOOSE LOCATION" )
drop = OptionMenu( master , clicked , *options )
drop.config(width = 50)
drop.pack()


def show():
	label.config( text = clicked1.get() )
options = ['english', 'indonesian', 'czech', 'german', 'spanish', 'french', 'italian', 'latvian', 'lithuanian', 'hungarian',
 'dutch', 'norwegian', 'polish', 'portuguese brasil', 'portuguese portugal', 'romanian', 'slovak', 'slovenian',
 'swedish', 'vietnamese', 'turkish', 'greek', 'bulgarian', 'russian', 'serbian', 'ukrainian', 'hebrew', 'arabic',
 'marathi', 'hindi', 'bengali', 'tamil', 'telugu', 'malyalam', 'thai', 'chinese simplified', 'chinese traditional',
 'japanese', 'korean']
clicked1 = StringVar()
clicked1.set( "CHOOSE LANGUAGE" )
drop = OptionMenu( master , clicked1 , *options )
drop.config(width = 50)
drop.pack()


def show():
	label.config( text = clicked2.get() )
options = [
    'Top Stories', 'World', 'Nation', 'Business', 'Technology', 'Entertainment', 'Sports', 'Science', 'Health'



]
clicked2 = StringVar()
clicked2.set( "CHOOSE TOPICS" )
drop = OptionMenu( master , clicked2, *options )
drop.config(width = 50)
drop.pack()

client = gnewsclient.NewsClient(language='hindi', location='india', topic='Business', max_results=5)
def news():
    client = gnewsclient.NewsClient(language=clicked1.get(), location=clicked.get(), topic=clicked2.get(), max_results=12)
    news_list = client.get_news()
    k=Tk()
    k.title("BREAKING  NEWS")
    k.geometry("2400x720")
    k.configure(bg='light grey')
    row=2
    def x():
        webbrowser.open(news_list[0]["link"] ,new=1)
        web(news_list[0])
    def x1():
        webbrowser.open(news_list[1]["link"] ,new=1)
        web(news_list[1])
    def x2():
        webbrowser.open(news_list[2]["link"] ,new=1)
        web(news_list[2])
    def x3():
        webbrowser.open(news_list[3]["link"] ,new=1)
        web(news_list[3])
    def x4():
        webbrowser.open(news_list[4]["link"] ,new=1)
        web(news_list[4])
    def x5():
        webbrowser.open(news_list[5]["link"] ,new=1)
        web(news_list[5])
    def x6():
        webbrowser.open(news_list[6]["link"] ,new=1)
        web(news_list[6])
    def x7():
        webbrowser.open(news_list[7]["link"] ,new=1)
        web(news_list[7])
    def x8():
        webbrowser.open(news_list[8]["link"] ,new=1)
        web(news_list[8])
    def x9():
        webbrowser.open(news_list[9]["link"] ,new=1)
        web(news_list[9])
    def x10():
        webbrowser.open(news_list[10]["link"] ,new=1)
        web(news_list[10])
    def x11():
        webbrowser.open(news_list[11]["link"] ,new=1)
        web(news_list[11])
        
    Button(k, text=news_list[0]["title"] , command=x).pack()
    Button(k, text=news_list[1]["title"] , command=x1).pack()
    Button(k, text=news_list[2]["title"] , command=x2).pack()
    Button(k, text=news_list[3]["title"] , command=x3).pack()
    Button(k, text=news_list[4]["title"] , command=x4).pack()
    Button(k, text=news_list[5]["title"] , command=x5).pack()
    Button(k, text=news_list[6]["title"] , command=x6).pack()
    Button(k, text=news_list[7]["title"] , command=x7).pack()
    Button(k, text=news_list[8]["title"] , command=x8).pack()
    Button(k, text=news_list[9]["title"] , command=x9).pack()
    Button(k, text=news_list[10]["title"] , command=x10).pack()
    Button(k, text=news_list[11]["title"] , command=x11).pack()

result_title = StringVar()
result_link = StringVar()
Button(master, text="SHOW", command=news, bg="red").pack()
master.mainloop()



