import csv
def add(CSV, str):
    return CSV.writerow(str)
with open ('imdbtitles.csv', newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    for variabls in csvreader:
        start_date=variabls[4]
        title_type=variabls[0]
        primary_title=variabls[1]
        runtime=variabls[6]
        genre=variabls[7]



        if start_date=='2010' or  start_date=='2011' \
                or start_date=='2012' or start_date=='2013' \
                or start_date=='2014' or start_date=='2015' \
                or start_date=='2016' or start_date=='2017' \
                or start_date=='2018' or start_date=='2019':
            if title_type=='movie':
                x=['Type:', title_type, ' Title:',primary_title,' Start:',start_date,' Length', runtime, ' Genre:',genre]
                print (x)
                # Movie_open=open('Movie_v2.csv','w')
                # Movie_write=csv.writer(Movie_open)
                # Movie_write.writerow(['Title type', 'Primary Title','Start Date','Runtime', 'Genre'])
                # print (add(Movie_write,x))










