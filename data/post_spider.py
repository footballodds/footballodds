import requests, time, datetime, xlrd, xlwt
from data import common


def winalone(css, gamedic):
    li = {}
    if css in gamedic:
        li = common.fullsolowin(gamedic[css][1], gamedic[css][5], gamedic[css][3])
    return li


def letball(css, dic):
    li = []
    if css in dic:
        let_li = [dic[css][p] for p in range(len(dic[css]) + 1) if
                  p % 2 != 0]

        for m in range(0, len(let_li) + 1, 4):
            if (m + 4) <= len(let_li):
                if let_li[m][0] == "+" or let_li[m][0] == '-':
                    if '/' in let_li[m]:
                        new = let_li[m].strip('+').split('/')
                        if new[0] == '0':
                            let_li[m] = float(new[1]) / 2
                        else:
                            let_li[m] = (float(new[0]) + float(new[1])) / 2
                        li.append(
                            common.letball(let_li[m], float(let_li[m + 2]), float(let_li[m + 3])))
                    else:
                        li.append(
                            common.letball(float(let_li[m][1:]), float(let_li[m + 2]), float(let_li[m + 3])))
                else:
                    li.append(
                        common.letball(float(let_li[m]), float(let_li[m + 2]), float(let_li[m + 3])))
    return li


def bigsmall(css, dic):
    li_result = []
    if css in dic:
        li = [dic[css][p] for p in range(len(dic[css]) + 1) if
              p % 2 != 0]
        for n in range(0, len(li) + 1, 4):
            if (n + 4) <= len(li):
                if '/' in li[n]:
                    new = li[n].split('/')
                    if new[0] == '0':
                        li[n] = -float(new[1]) / 2
                    else:
                        li[n] = (float(new[0]) + float(new[1])) / 2
                    li_result.append(common.bigball(li[n], float(li[n + 2]), float(li[n + 3])))
                else:
                    li_result.append(common.bigball(float(li[n]), float(li[n + 2]), float(li[n + 3])))
    return li_result


def writexecel(path, eventname, teamname):
    # C:/Users/Administrator/Desktop/game
    writebook = xlwt.Workbook()
    sheet = writebook.add_sheet(eventname)
    for i in range(len(teamname)):
        sheet.write(i, 0, teamname[i][0])
        sheet.write(i, 1, teamname[i][1])
    writebook.save(path)


def data188():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    url = "http://landing-sb.188sbk.com/zh-cn/Service/CentralService?GetData&ts={}".format(round(time.time() * 1000))
    data = {
        "IsFirstLoad": "true",
        "VersionL": "-1",
        "VersionU": "0",
        "VersionS": "-1",
        "VersionF": "-1",
        "VersionH": "0",
        "VersionT": "-1",
        "IsEventMenu": "false",
        "SportID": "1",
        "CompetitionID": "-1",
        "reqUrl": "/zh-cn/sports/football/matches-by-date/today/full-time-asian-handicap-and-over-under",
        "oIsInplayAll": "false",
        "oIsFirstLoad": "true",
        "oSortBy": "1",
        "oOddsType": "0",
        "oPageNo": "0",
        "hisUrl": "/zh-cn/sports/football/matches-by-date/today/full-time-asian-handicap-and-over-under",
        "LiveCenterEventId": "0",
        "LiveCenterSportId": "0"
    }
    first_dic = requests.post(data=data, url=url, headers=headers).json()
    game_dic = first_dic['mod']['d'][0]['c']

    if game_dic is not None:
        info = {}
        for i in range(len(game_dic)):
            game_name = game_dic[i]['n']
            info[game_name] = []
            execl_teamname = []
            for j in range(len(game_dic[i]['e'])):
                j_info = {}
                game_time = str(datetime.datetime.strptime(game_dic[i]['e'][j]['edt'].replace('T', ' '),
                                                           '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=12))
                j_info['time'] = game_time
                j_info['info'] = {'n': game_dic[i]['e'][j]['cei']['n'],
                                  'game': {'Home': game_dic[i]['e'][j]['i'][0], 'Visit': game_dic[i]['e'][j]['i'][1]}}
                # 全场独赢
                j_info['full_win_alone'] = winalone('1x2', game_dic[i]['e'][j]['o'])
                # 半场独赢
                j_info['half_win_alone'] = winalone('1x21st', game_dic[i]['e'][j]['o'])
                # 全场让球
                j_info['full_let_ball'] = letball('ah', game_dic[i]['e'][j]['o'])
                # 半场让球
                j_info['half_let_ball'] = letball('ah1st', game_dic[i]['e'][j]['o'])
                # 全场大小
                j_info['full_big_small'] = bigsmall('ou', game_dic[i]['e'][j]['o'])
                # 半场大小
                j_info['half_big_small'] = bigsmall('oulst', game_dic[i]['e'][j]['o'])

                j_info['fullmatch'] = common.fullmatch(j_info['full_win_alone'], j_info['full_let_ball'],
                                                       j_info['full_big_small'])
                j_info['halfmatch'] = common.halfmatch(j_info['half_win_alone'], j_info['half_let_ball'],
                                                       j_info['half_big_small'])

                final = common.matchinfo(j_info['time'], game_dic[i]['e'][j]['i'][0],
                                         game_dic[i]['e'][j]['i'][1], j_info['fullmatch'], j_info['halfmatch'])
                info[game_name].append(final)
                # execl_teamname.append((game_dic[i]['e'][j]['i'][0], game_dic[i]['e'][j]['i'][1]))
            # writexecel('C:/Users/Administrator/Desktop/game/{}.xls'.format(game_name),game_name, execl_teamname)
        return info


if __name__ == '__main__':
    data = data188()

