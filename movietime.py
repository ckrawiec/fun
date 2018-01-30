#!/usr/bin/env python
import pandas
import Tkinter as tk
from PIL import ImageTk, Image
from astropy.table import Table

fields = 'Name', 'Movie', 'Genre', 'Rating'


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries
        
def main():
    root = tk.Tk()

    #pretty
    root.title('M O V I E T I M E')
    logo = "/Users/Christina/Documents/movietimelogo.gif"
    img = ImageTk.PhotoImage(Image.open(logo))
    w = img.width()
    h = img.height()
    x, y = 0, 0
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    panel = tk.Label(root, image=img)
    panel.photo = img
    panel.grid()
    
    
    """
    #entries
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='Show',
                command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
"""
    root.mainloop()

    movie_file = '/Users/Christina/git/fun/moviefile.tab'
    movie_col = 'movie'


#clicking = "<Button-1>"
    
    """
    tab = Table.read(movie_file)
    
    person = raw_input("Are you Frankie or Christina?: ")
    while person not in ['Frankie','Christina']:
        if person=='Frankie':
            print "Hi, Frankie! You're looking, uh, good, I guess."
        elif person=='Christina':
            print "Hi, Christina! You look beautiful, today :) <3"
        else:
            print "SPELL IT RIGHT, DOOFUS"
            person = raw_input("Are you Frankie or Christina?: ")
        
    movie = raw_input("What movie did you watch?: ")
    print "COOL"
    if movie not in tab[movie_col]:
        tab[movie_col].append(movie)
    
    genre = raw_input("What genre is {}".format(movie))
    rating = raw_input("What rating do you give {}?".format(movie))
    
    tab[person][np.where(tab[movie_col]==movie)] = rating
    
    print "THATS GOOD OK BYE BYE"
    exit()
    """

if __name__=="__main__":
    main()
