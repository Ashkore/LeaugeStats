from AutoColumnWidth import FitSheetWrapper
import xlwt
def Write_ToExcel(StatsObject,FileName):
    workbook = xlwt.Workbook()
    sheet = FitSheetWrapper(workbook.add_sheet("Sheet 1"))
    Row0 = 0
    Row1 = 1
    Row2 = 2
    Row3 = 3
    Row4 = 4
    Row5 = 5
    Row6 = 6
    Row7 = 7
    Row8 = 8
    Row9 = 9
    Row10 = 10
    Row11 = 11
    Row12 = 12
    Row13 = 13
    Row14 = 14
    Row15 = 15
    Row16 = 16
    Row17 = 17
    Row18 = 18
    Row19 = 19
    Row20 = 20
    Row21 = 21
    Row22 = 22
    #Setting Colors
    xlwt.add_palette_colour("salmon", 0x21)
    workbook.set_colour_RGB(0x21, 255, 153, 153)
    xlwt.add_palette_colour("light_blue", 0x22)
    workbook.set_colour_RGB(0x22, 173, 216, 230)

    bold = xlwt.easyxf('font: bold 1')
    lightred = xlwt.easyxf('pattern: pattern solid, fore_colour salmon; border: top thin, bottom thin, left thin, right thin')
    lightblue = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue; border: top thin, bottom thin, left thin, right thin')
    GameStartRow = 1
    for Day in range(len(StatsObject)):
        for Game in range(len(StatsObject[Day])):
            #Set up totals.
            BTeamDeaths = int((StatsObject[Day][Game]['Blue Team Char Info']['CharOne'][5]+
                               StatsObject[Day][Game]['Blue Team Char Info']['CharTwo'][5]+
                               StatsObject[Day][Game]['Blue Team Char Info']['CharThree'][5]+
                               StatsObject[Day][Game]['Blue Team Char Info']['CharFour'][5]+
                               StatsObject[Day][Game]['Blue Team Char Info']['CharFive'][5]))
            RTeamDeaths = int((StatsObject[Day][Game]['Red Team Char Info']['CharOne'][5]+
                               StatsObject[Day][Game]['Red Team Char Info']['CharTwo'][5]+
                               StatsObject[Day][Game]['Red Team Char Info']['CharThree'][5]+
                               StatsObject[Day][Game]['Red Team Char Info']['CharFour'][5]+
                               StatsObject[Day][Game]['Red Team Char Info']['CharFive'][5]))
            #TITLES
            sheet.write(Row0,0,"Game Length in Seconds",bold)
            sheet.write(Row1,0,"VOD",bold)
            sheet.write(Row2,0,"Match History",bold)
            #Team Info Titles
            sheet.write(Row3,0,"Team Name",bold)
            sheet.write(Row4,0,"Team Win",bold)
            sheet.write(Row5,0,"Ban One",bold)
            sheet.write(Row6,0,"Ban Two",bold)
            sheet.write(Row7,0,"Ban Three",bold)
            sheet.write(Row8,0,"Towers Destoryed",bold)
            sheet.write(Row9,0,"Dragons Killed",bold)
            sheet.write(Row10,0,"Barons Killed",bold)
            sheet.write(Row11,0,"Kills",bold)
            sheet.write(Row12,0,"Deaths",bold)
            sheet.write(Row13,0,"Gold",bold)
            #Player Char Info Titles
            sheet.write(Row0,4,"Player 1",bold)
            sheet.write(Row0,5,"Player 2",bold)
            sheet.write(Row0,6,"Player 3",bold)
            sheet.write(Row0,7,"Player 4",bold)
            sheet.write(Row0,8,"Player 5",bold)
            sheet.write(Row0,9,"Player 6",bold)
            sheet.write(Row0,10,"Player 7",bold)
            sheet.write(Row0,11,"Player 8",bold)
            sheet.write(Row0,12,"Player 9",bold)
            sheet.write(Row0,13,"Player 10",bold)
            sheet.write(Row1,3,"Name",bold)
            sheet.write(Row2,3,"Champ",bold)
            sheet.write(Row3,3,"SS One",bold)
            sheet.write(Row4,3,"SS Two",bold)
            sheet.write(Row5,3,"Kills",bold)
            sheet.write(Row6,3,"Kills %",bold)
            sheet.write(Row7,3,"Deaths",bold)
            sheet.write(Row8,3,"Deaths %",bold)
            sheet.write(Row9,3,"Assists",bold)
            sheet.write(Row10,3,"Assists %",bold)
            sheet.write(Row11,3,"CS",bold)
            sheet.write(Row12,3,"CS %",bold)
            sheet.write(Row13,3,"Gold",bold)
            sheet.write(Row14,3,"Gold %",bold)
            sheet.write(Row15,3,"Item One",bold)
            sheet.write(Row16,3,"Item Two",bold)
            sheet.write(Row17,3,"Item Three",bold)
            sheet.write(Row18,3,"Item Four",bold)
            sheet.write(Row19,3,"Item Five",bold)
            sheet.write(Row20,3,"Item Six",bold)
            sheet.write(Row21,3,"Trinket",bold)
            sheet.write(Row22,3,"Mastery",bold)
            #Pick Info
            sheet.write(Row1,14,"Pick 1",bold)
            sheet.write(Row2,14,"Pick 3",bold)
            sheet.write(Row3,14,"Pick 3",bold)
            sheet.write(Row4,14,"Pick 5",bold)
            sheet.write(Row5,14,"Pick 5",bold)
            sheet.write(Row0,14,"Pick #",bold)
            sheet.write(Row0,15,"Character",bold)
            sheet.write(Row0,16,"Position",bold)
            sheet.write(Row0,17,"Position",bold)
            sheet.write(Row0,18,"Character",bold)
            sheet.write(Row0,19,"Pick #",bold)
            sheet.write(Row1,19,"Pick 2",bold)
            sheet.write(Row2,19,"Pick 2",bold)
            sheet.write(Row3,19,"Pick 4",bold)
            sheet.write(Row4,19,"Pick 4",bold)
            sheet.write(Row5,19,"Pick 6",bold)
            #Tower Place Holder
            sheet.write(Row7,15,"Time",bold)
            sheet.write(Row8,14,"BotTow1",bold)
            sheet.write(Row9,14,"BotTow2",bold)
            sheet.write(Row10,14,"BotTow3",bold)
            sheet.write(Row11,14,"Botinhib",bold)
            sheet.write(Row12,14,"MidTow1",bold)
            sheet.write(Row13,14,"MidTow2",bold)
            sheet.write(Row14,14,"MidTow3",bold)
            sheet.write(Row15,14,"Midinhib",bold)
            sheet.write(Row16,14,"TopTow1",bold)
            sheet.write(Row17,14,"TopTow2",bold)
            sheet.write(Row18,14,"TopTow3",bold)
            sheet.write(Row19,14,"Topinhib",bold)
            sheet.write(Row20,14,"FTowTop",bold)
            sheet.write(Row21,14,"FTowBot",bold)
            sheet.write(Row7,18,"Time",bold)
            sheet.write(Row8,19,"BotTow1",bold)
            sheet.write(Row9,19,"BotTow2",bold)
            sheet.write(Row10,19,"BotTow3",bold)
            sheet.write(Row11,19,"Botinhib",bold)
            sheet.write(Row12,19,"MidTow1",bold)
            sheet.write(Row13,19,"MidTow2",bold)
            sheet.write(Row14,19,"MidTow3",bold)
            sheet.write(Row15,19,"Midinhib",bold)
            sheet.write(Row16,19,"TopTow1",bold)
            sheet.write(Row17,19,"TopTow2",bold)
            sheet.write(Row18,19,"TopTow3",bold)
            sheet.write(Row19,19,"Topinhib",bold)
            sheet.write(Row20,19,"FTowTop",bold)
            sheet.write(Row21,19,"FTowBot",bold)
            #########
            ulstyle = xlwt.easyxf('font: underline single')
            sheet.write(Row0,1,StatsObject[Day][Game]['Game Length'])#Game X
            link = 'HYPERLINK("%s","VOD")\n' % (StatsObject[Day][Game]['Links']['Video'])
            sheet.write(Row1,1,xlwt.Formula(link),ulstyle)#VOD
            link = 'HYPERLINK("%s","STATS")\n' % (StatsObject[Day][Game]['Links']['Match History'])
            sheet.write(Row2,1,xlwt.Formula(link),ulstyle)#Stats
            #sheet.col(1).width = 100
            #Blue Team General Info
            sheet.write(Row3,1,str(StatsObject[Day][Game]['Game Title'].split(" vs ")[0]),lightblue)#Team A Name
            sheet.write(Row4,1,StatsObject[Day][Game]['Blue Team Info']['Win'],lightblue)
            sheet.write(Row5,1,StatsObject[Day][Game]['Blue Team Info']['Bans'][0],lightblue)#Team A Ban 1
            sheet.write(Row6,1,StatsObject[Day][Game]['Blue Team Info']['Bans'][1],lightblue)#Team A Ban 2
            sheet.write(Row7,1,StatsObject[Day][Game]['Blue Team Info']['Bans'][2],lightblue)#Team A Ban 3
            sheet.write(Row8,1,StatsObject[Day][Game]['Blue Team Info']['Towers'],lightblue)#Team A Towers
            sheet.write(Row9,1,StatsObject[Day][Game]['Blue Team Info']['Dragons'],lightblue)#Team A Dragons
            sheet.write(Row10,1,StatsObject[Day][Game]['Blue Team Info']['Barons'],lightblue)#Team A Barons
            sheet.write(Row11,1,StatsObject[Day][Game]['Blue Team Info']['Kills'],lightblue)#Team A Kills
            sheet.write(Row12,1,StatsObject[Day][Game]['Blue Team Info']['Deaths'],lightblue)#Team A Deaths
            sheet.write(Row13,1,StatsObject[Day][Game]['Blue Team Info']['Gold'],lightblue)
            #Red Team General Info
            sheet.write(Row3,2,str(StatsObject[Day][Game]['Game Title'].split(" vs ")[1]),lightred)#Team B Name
            sheet.write(Row4,2,StatsObject[Day][Game]['Red Team Info']['Win'],lightred)
            sheet.write(Row5,2,StatsObject[Day][Game]['Red Team Info']['Bans'][0],lightred)#Team B Ban 1
            sheet.write(Row6,2,StatsObject[Day][Game]['Red Team Info']['Bans'][1],lightred)#Team B Ban 2
            sheet.write(Row7,2,StatsObject[Day][Game]['Red Team Info']['Bans'][2],lightred)#Team B Ban 3
            sheet.write(Row8,2,StatsObject[Day][Game]['Red Team Info']['Towers'],lightred)#Team B Towers
            sheet.write(Row9,2,StatsObject[Day][Game]['Red Team Info']['Dragons'],lightred)#Team B Dragons
            sheet.write(Row10,2,StatsObject[Day][Game]['Red Team Info']['Barons'],lightred)#Team B Barons
            sheet.write(Row11,2,StatsObject[Day][Game]['Red Team Info']['Kills'],lightred)#Team B Kills
            sheet.write(Row12,2,StatsObject[Day][Game]['Red Team Info']['Deaths'],lightred)#Team B Deaths
            sheet.write(Row13,2,StatsObject[Day][Game]['Red Team Info']['Gold'],lightred)
            #####Blue Team Char Info
            column = 4
            row = GameStartRow
            for character in (StatsObject[Day][Game]['Blue Team Char Info']):
                for attribute in (StatsObject[Day][Game]['Blue Team Char Info'][character]):
                    if isinstance(attribute,list):
                        for a in attribute:
                            sheet.write(row,column,a,lightblue)
                            row +=1
                    else:
                        sheet.write(row,column,str(attribute),lightblue)
                        row +=1
                row = GameStartRow
                column +=1
            for character in (StatsObject[Day][Game]['Red Team Char Info']):
                for attribute in (StatsObject[Day][Game]['Red Team Char Info'][character]):
                    if isinstance(attribute,list):
                        for a in attribute:
                            sheet.write(row,column,a,lightred)
                            row +=1
                    else:
                        sheet.write(row,column,str(attribute),lightred)
                        row +=1
                row = GameStartRow
                column +=1
                #Blue Char Names
            sheet.write(Row1,15,StatsObject[Day][Game]['Blue Team Info']['Picks'][0],lightblue)
            sheet.write(Row2,15,StatsObject[Day][Game]['Blue Team Info']['Picks'][1],lightblue)
            sheet.write(Row3,15,StatsObject[Day][Game]['Blue Team Info']['Picks'][2],lightblue)
            sheet.write(Row4,15,StatsObject[Day][Game]['Blue Team Info']['Picks'][3],lightblue)
            sheet.write(Row5,15,StatsObject[Day][Game]['Blue Team Info']['Picks'][4],lightblue)
                #Blue Char Pos
            sheet.write(Row1,16,StatsObject[Day][Game]['Blue Team Info']['Picks Pos'][0],lightblue)
            sheet.write(Row2,16,StatsObject[Day][Game]['Blue Team Info']['Picks Pos'][1],lightblue)
            sheet.write(Row3,16,StatsObject[Day][Game]['Blue Team Info']['Picks Pos'][2],lightblue)
            sheet.write(Row4,16,StatsObject[Day][Game]['Blue Team Info']['Picks Pos'][3],lightblue)
            sheet.write(Row5,16,StatsObject[Day][Game]['Blue Team Info']['Picks Pos'][4],lightblue)
                #Red Char Pos
            sheet.write(Row1,17,StatsObject[Day][Game]['Red Team Info']['Picks Pos'][0],lightred)
            sheet.write(Row2,17,StatsObject[Day][Game]['Red Team Info']['Picks Pos'][1],lightred)
            sheet.write(Row3,17,StatsObject[Day][Game]['Red Team Info']['Picks Pos'][2],lightred)
            sheet.write(Row4,17,StatsObject[Day][Game]['Red Team Info']['Picks Pos'][3],lightred)
            sheet.write(Row5,17,StatsObject[Day][Game]['Red Team Info']['Picks Pos'][4],lightred)
                #Red Char Name
            sheet.write(Row1,18,StatsObject[Day][Game]['Red Team Info']['Picks'][0],lightred)
            sheet.write(Row2,18,StatsObject[Day][Game]['Red Team Info']['Picks'][1],lightred)
            sheet.write(Row3,18,StatsObject[Day][Game]['Red Team Info']['Picks'][2],lightred)
            sheet.write(Row4,18,StatsObject[Day][Game]['Red Team Info']['Picks'][3],lightred)
            sheet.write(Row5,18,StatsObject[Day][Game]['Red Team Info']['Picks'][4],lightred)
           #Spacing Between Games
            RowGap = 25
            GameStartRow += RowGap
            Row0 += RowGap
            Row1 += RowGap
            Row2 += RowGap
            Row3 += RowGap
            Row4 += RowGap
            Row5 += RowGap
            Row6 += RowGap
            Row7 += RowGap
            Row8 += RowGap
            Row9 += RowGap
            Row10 += RowGap
            Row11 += RowGap
            Row12 += RowGap
            Row13 += RowGap
            Row14 += RowGap
            Row15 += RowGap
            Row16 += RowGap
            Row17 += RowGap
            Row18 += RowGap
            Row19 += RowGap
            Row20 += RowGap
            Row21 += RowGap
            Row22 += RowGap
            
    workbook.save(FileName)
