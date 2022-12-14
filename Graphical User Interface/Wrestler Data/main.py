from tkinter import *
import csv

app = Tk()
app.title("Wrestler data")
app.geometry("600x250")
app.maxsize(600,250)
app.minsize(600,250)
weclome = Label(app,  text = "Welcome to Wrestler data")
weclome.pack()

user_in = Entry()
user_in.pack()

def Search():

    def Wretler_data(data):
            total = int(data[1])+int(data[2])+int(data[3])
            wins = round(int(data[1])/int(total) * 100)
            losses = round(int(data[2])/int(total) * 100)
            draws = round(int(data[3])/int(total) * 100)
            print_win = f"Wins percentage: {wins}%"
            print_loss = f"Losses percentage {losses}%"
            print_draw = f"Draws percentage {draws}%"
            show.delete(1.0,END)
            show.insert(INSERT,(f"{print_win}\n{ print_loss}\n{print_draw}"))
    with open("Wrestler.csv",'r') as csv_file:
        CSV_READER = csv.reader(csv_file,delimiter = ',')
        found = False
        for row in CSV_READER:
            if user_in.get() == row[0]:
                Wretler_data(row)
                found = True
        if not found:
            show.insert(INSERT,(f"User Not found"))

search = Button(app,text = "Search User",command = Search)
search.pack()

show = Text(app,width=25, height=3, font=('arial', 20))
show.pack()
app.mainloop()

Wrestler,Wins,Losses,Draws
Dean Ambrose,133,67,4
Kevin Owens,61,130,2
Tyler Breeze,17,163,2
AJ Styles,108,68,0
Sami Zayn,111,59,6
Dolph Ziggler,114,56,2
Zack Ryder,119,51,2
Rusev,70,97,2
Jey Uso,76,90,0
Baron Corbin,103,59,3
Sheamus,44,115,5
Becky Lynch,102,54,5
Roman Reigns,142,12,5
Apollo Crews,125,30,0
Jason Jordan,126,23,2
Jimmy Uso,70,80,0
Viktor,2,145,1
Chad Gable,120,25,2
The Miz,43,103,1
Mojo Rawley,113,31,2
Natalya,37,109,0
Cesaro,78,62,3
Jack Swagger,73,70,0
Bayley,126,11,2
Big E,107,31,1
Fandango,24,111,0
Kofi Kingston,95,39,1
Kalisto,75,59,0
Sasha Banks,101,28,5
Bray Wyatt,24,107,2
Sin Cara,69,62,2
Aiden English,12,118,2
Enzo Amore,79,48,3
Charlotte,86,42,1
Heath Slater,62,64,0
Alexa Bliss,35,90,0
Curtis Axel,11,114,0
Simon Gotch,11,111,1
Bo Dallas,17,104,1
Carmella,59,62,1
Goldust,96,26,0
Karl Anderson,31,89,2
Braun Strowman,65,53,3
Titus O'Neil,47,73,1
Kane,103,15,0
R-Truth,96,21,1
Seth Rollins,39,75,4
Asuka,112,3,2
Chris Jericho,38,77,0
Konnor,2,110,1
Luke Gallows,27,84,2
Nia Jax,37,72,1
Xavier Woods,83,26,1
Darren Young,74,28,2
Neville,78,26,0
Big Cass,61,40,1
Tye Dillinger,60,41,1
Dash Wilder,34,64,3
Scott Dawson,34,63,3
D-Von Dudley,19,77,0
Shinsuke Nakamura,90,4,2
Samoa Joe,32,59,4
Bubba Ray Dudley,21,72,0
Alberto Del Rio,24,65,2
Peyton Royce,20,67,2
Erick Rowan,14,72,1
Alexander Wolfe,37,49,0
Dana Brooke,11,74,0
Liv Morgan,42,43,0
Naomi,41,43,0
Angelo Dawkins,21,62,0
Billie Kay,27,50,2
Aliyah,26,51,1
Patrick Clark,26,52,0
Elias Samson,29,48,0
The Big Show,60,16,1
No Way Jose,56,19,1
Alicia Fox,49,25,1
Daria Berenato,27,47,0
Epico,21,52,1
Primo,19,54,1
Riddick Moss,18,55,1
Tino Sabbatelli,24,50,0
Stardust,5,66,2
Tucker Knight,28,45,0
Finn Balor,60,11,1
Luke Harper,20,51,1
Sawyer Fulton,28,42,1
Mandy Rose,13,54,1
Andrade Almas,40,23,0
Rhyno,50,13,0
Austin Aries,37,23,1
Rich Swann,41,19,1
Randy Orton,39,21,0
Ryback,37,17,1
Bobby Roode,25,28,1
Summer Rae,12,42,0
Wesley Blake,7,45,1
Ember Moon,36,15,0
John Cena,29,21,0
Oney Lorcan,32,18,0
Curt Hawkins,4,44,0
Nikki Bella,34,13,1
Tommaso Ciampa,32,16,0
Colin Cassady,38,7,2
Johnny Gargano,32,15,0
Steve Cutler,10,35,1
Paige,30,15,0
Shane Thorne,28,17,0
Buddy Murphy,10,33,1
Emma,14,30,0
Manny Andrade,32,12,0
Nick Miller,27,17,0
Tamina,6,36,0
Eva Marie,18,22,0
Jinder Mahal,3,37,0
Cedric Alexander,26,13,0
Kenneth Crawford,16,21,0
Christopher Girard,7,28,1
Hugo Knox,24,11,0
Blake,2,31,1
Murphy,2,31,1
Mark Henry,20,12,0
TJ Perkins,22,10,0
Alex Riley,11,20,0
Charlotte Flair,12,18,1
Sunny Dhinsa,11,19,0
Adam Rose,6,23,0
Damien Sandow,11,18,0
Lince Dorado,15,13,1
Gzim Selmani,11,17,0
Hideo Itami,26,2,0
Adrienne Reese,14,12,0
Akam,23,3,0
Rezar,23,3,0
Dan Matha,7,17,1
Josh Woods,9,15,0
Lana,3,20,0
Niko Bogojevic,7,14,0
Adrian Jaoude,5,14,1
Diego,1,19,0
Otis Dozovic,7,13,0
The Brian Kendrick,11,9,0
Noam Dar,7,12,0
Tony Nese,7,12,0
Roderick Strong,13,5,0
Eric Young,8,9,0
King Barrett,3,14,0
Brie Bella,7,9,0
Drew Gulak,3,13,0
Fernando,1,15,0
Kishan Raftar,6,10,0
Levis Valenzuela Jr.,15,1,0
Ariya Daivari,3,12,0
Jack Gallagher,12,3,0
Nicola Glencross,3,12,0
Noah Kekoa,5,10,0
Tian Bing,6,8,0
Gran Metalik,8,5,0
Nikki Cross,8,5,0
Noah Potjes,3,10,0
Brock Lesnar,8,3,0
Cezar Bononi,1,9,1
James Ellsworth,8,3,0
Macey Estrella,1,10,0
