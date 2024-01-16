import urllib.request
# 10 files for baby names called babynameranking[year].txt for years 2001-2010

# each line contains a ranking, a boys name, amount of boys named that name, a girls name, amount of girls named that named

# prompt user to enter year, gender, name, then display the ranking of the name for that year



# https://liveexample.pearsoncmg.com/data/babynameranking2001.txt

# open file from website, change url opened according to year entered


# TODO
# process each string in opened files to extract needed info
# user input
# idk




year = "2002.txt"

def open_file(year):
    # year needs to be in the format of "yyyy.txt"
    url = "https://liveexample.pearsoncmg.com/data/babynameranking" + year
    file = urllib.request.urlopen(url)
    return file



for line in open_file(year):
    print(line)
