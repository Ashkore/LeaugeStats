from tkinter import *
import Scoreboard
from datetime import datetime


global Series
global Year
global Region
global Season
def Gui():
    MainWindow = Tk()
    MainWindow.wm_title("Joe's League Stats")
    #Regions
    global rowlist
    rowlist = [2]
    # with open('Regions.txt','r') as Regions:
    #     rowlist.append(Create_Regions_Buttons(MainWindow,Regions.readlines()))
    # #Years
    # with open('Years.txt','r') as Years:
    #     rowlist.append(Create_Year_Buttons(MainWindow,Years.readlines()))
    # #Series
    # with open('Series.txt','r')as Series:
    #     rowlist.append(Create_Series_Buttons(MainWindow,Series.readlines()))
    # with open('Season.txt','r') as Seasons:
    #     rowlist.append(Create_Seasons_Buttons(MainWindow,Seasons.readlines()))
    # with open('Week.txt','r') as Weeks:
    #     rowlist.append(Create_Weeks_Buttons(MainWindow,Weeks.readlines()))


    #Custom URL
    CustomURLLabel = Label(MainWindow,text = "Insert your own URL:")
    CustomURL = Entry (MainWindow,width = 100)
    CustomURLLabel.grid(row = 0,column = 0)
    CustomURL.grid(row = 0, column = 1)
    Process = Label(MainWindow,text = " ")
    Process.grid(row = 3, column = 0, columnspan = 2)
    DoneButton = Button(MainWindow,text = "Done",command =lambda: run_code(CustomURL,Process))
    DoneButton.grid(column = 1, row = 1)

    # YearLabel = Label(MainWindow,text = "To add more to this column,\n edit the Year.txt file.")
    # YearLabel.grid(column = 1,row = max(rowlist))
    # RegionLabel = Label(MainWindow,text = "To add more to this column,\n edit the Region.txt file.")
    # RegionLabel.grid(column = 0,row = max(rowlist))
    # SeriesLabel = Label(MainWindow,text = "To add more to this column,\n edit the Series.txt file.")
    # SeriesLabel.grid(column = 2,row = max(rowlist))
    # SeasonLabel = Label(MainWindow,text = "To add more to this column,\n edit the Season.txt file.")
    # SeasonLabel.grid(column = 3,row = max(rowlist))
    # WeekLabel = Label(MainWindow,text = "To add more to this column,\n edit the Weeks.txt file.")
    # WeekLabel.grid(column = 4,row = max(rowlist))
    MainWindow.mainloop()

def Set_Region(string):
    global Region
    Region = string
def Set_Year(string):
    global Year
    Year = string
def Set_Series(string):
    global Series
    Series = string
def Set_Season(string):
    global Season
    Season = string
def Set_Week(string):
    global Week
    Week = string
def Create_Year_Buttons(MainWindow,Years):
    YearLabel = Label (MainWindow,text = "Please choose a Year:")
    YearLabel.grid(column = 1,row = 0)
    for x in range(len(Years)):
        YearRadio = Button(MainWindow, text = Years[x],command = Set_Year(Years[x]))
        YearRadio.grid(column = 1,row = x+1)
    return x+2
def Create_Series_Buttons(MainWindow,Series):
    label = Label (MainWindow,text = "Please choose a Series:")
    label.grid(column = 2,row = 0)
    for x in range(len(Series)):
        Radio = Button(MainWindow, text = Series[x],command = Set_Series(Series[x]))
        Radio.grid(column = 2,row = x+1)
    return x+2
def Create_Regions_Buttons(MainWindow,Regions):
    label = Label (MainWindow,text = "Please choose a Region:")
    label.grid(column = 0,row = 0)
    for x in range(len(Regions)):
        Radio = Button(MainWindow, text = Regions[x],command = Set_Region(Regions[x]))
        Radio.grid(column = 0,row = x+1)
    return x+2
def Create_Seasons_Buttons(MainWindow,Seasons):
    label = Label (MainWindow,text = "Please choose a Season:")
    label.grid(column = 3,row = 0)
    for x in range(len(Seasons)):
        Radio = Button(MainWindow, text = Seasons[x],command = Set_Season(Seasons[x]))
        Radio.grid(column = 3,row = x+1)
    return x+2
def Create_Weeks_Buttons(MainWindow,Weeks):
    label = Label (MainWindow,text = "Please choose a Season:")
    label.grid(column = 4,row = 0)
    for x in range(len(Weeks)):
        Radio = Button(MainWindow, text = Weeks[x],command = Set_Week(Weeks[x]))
        Radio.grid(column = 4,row = x+1)
    return x+2

def run_code(Cust,Process):
    FileName = "Leauge Stats "+str(datetime.now().strftime('%Y-%m-%d %Hh-%Mm-%Ss'))+".xls"
    Process.config(text = "Trying : "+Cust.get())
    if Cust.get().startswith('http://lol.esportspedia.com/wiki/') and 'Scoreboards' in Cust.get():
        Scoreboard.Main(Cust.get(),FileName)
        Cust.delete(0,len(Cust.get()))
        Process.config(text = "Completed: "+FileName)
    else:
        Process.config(text = "Please Enter a valid website.")

Gui()