import requests, time, datetime
from data import common
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
        Final = []
        info = {}
        for i in range(len(game_dic)):
            game_name = game_dic[i]['n']
            info[game_name] = []
            '''
            {
                'time': {},
                'info': {'n': '', 'game': []},
                'full_win_alone': {},
                'half_win_alone': {},
                'full_let_ball': {},
                'half_let_ball': {},
                'full_big_small': {},
                'half_big_small': {},
                'corner_kick': {}
    
            }
            '''
            for j in range(len(game_dic[i]['e'])):
                j_info = {}
                game_time = str(datetime.datetime.strptime(game_dic[i]['e'][j]['edt'].replace('T', ' '),
                                                           '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=12))
                j_info['time'] = game_time
                j_info['info'] = {'n': game_dic[i]['e'][j]['cei']['n'],
                                  'game': {'Home': game_dic[i]['e'][j]['i'][0], 'Visit': game_dic[i]['e'][j]['i'][1]}}
                # 全场独赢
                j_info['full_win_alone'] = {}
                if '1x2' in game_dic[i]['e'][j]['o']:
                    j_info['full_win_alone'] = common.fullsolowin(game_dic[i]['e'][j]['o']["1x2"][1],
                                                                  game_dic[i]['e'][j]['o']["1x2"][5],
                                                                  game_dic[i]['e'][j]['o']["1x2"][3])

                j_info['half_win_alone'] = {}
                # 半场独赢
                if '1x21st' in game_dic[i]['e'][j]['o']:
                    j_info['half_win_alone'] = common.halfsolowin(game_dic[i]['e'][j]['o']["1x21st"][1],
                                                                  game_dic[i]['e'][j]['o']["1x21st"][5],
                                                                  game_dic[i]['e'][j]['o']["1x21st"][3])
                j_info['full_let_ball'] = []
                # 全场让球
                if 'ah' in game_dic[i]['e'][j]['o']:

                    let_li = [game_dic[i]['e'][j]['o']["ah"][p] for p in range(len(game_dic[i]['e'][j]['o']["ah"]) + 1) if
                              p % 2 != 0]

                    for m in range(0, len(let_li) + 1, 4):
                        if (m + 4) <= len(let_li):
                            if let_li[m][0] == "+" or let_li[m][0] == '-':
                                j_info['full_let_ball'].append(common.letball(let_li[m][1:], let_li[m + 2], let_li[m + 3]))
                            else:
                                j_info['full_let_ball'].append(common.letball(let_li[m], let_li[m + 2], let_li[m + 3]))

                # 半场让球
                j_info['half_let_ball'] = []
                if 'ah1st' in game_dic[i]['e'][j]['o']:

                    half_let_li = [game_dic[i]['e'][j]['o']["ah1st"][p] for p in
                                   range(len(game_dic[i]['e'][j]['o']["ah1st"]) + 1) if
                                   p % 2 != 0]
                    for m in range(0, len(half_let_li) + 1, 4):
                        if (m + 4) <= len(half_let_li):
                            if half_let_li[m][0] == "+" or half_let_li[m][0] == '-':
                                j_info['half_let_ball'].append(
                                    common.letball(half_let_li[m][1:], half_let_li[m + 2], half_let_li[m + 3]))
                            else:
                                j_info['half_let_ball'].append(
                                    common.letball(half_let_li[m], half_let_li[m + 2], half_let_li[m + 3]))

                # 全场大小
                j_info['full_big_small'] = []
                if 'ou' in game_dic[i]['e'][j]['o']:

                    li = [game_dic[i]['e'][j]['o']["ou"][p] for p in range(len(game_dic[i]['e'][j]['o']["ou"]) + 1) if
                          p % 2 != 0]
                    for n in range(0, len(li) + 1, 4):
                        if (n + 4) <= len(li):
                            j_info['full_big_small'].append(common.bigball(li[n], li[n + 2], li[n + 3]))

                # 半场大小
                j_info['half_big_small'] = []
                if 'ou1st' in game_dic[i]['e'][j]['o']:

                    half_li = [game_dic[i]['e'][j]['o']["ou1st"][p] for p in
                               range(len(game_dic[i]['e'][j]['o']["ou1st"]) + 1) if
                               p % 2 != 0]
                    for n in range(0, len(half_li) + 1, 4):
                        if (n + 4) <= len(half_li):
                            j_info['half_big_small'].append(
                                (half_li[n], half_li[n + 2]))
                            j_info['half_big_small'].append(common.bigball(half_li[n], half_li[n + 2], half_li[n + 3]))
                j_info['fullmatch'] = common.fullmatch(j_info['full_win_alone'], j_info['full_let_ball'],
                                                       j_info['full_big_small'])
                j_info['halfmatch'] = common.halfmatch(j_info['half_win_alone'], j_info['half_let_ball'],
                                                       j_info['half_big_small'])

                final = common.matchinfo(j_info['time'], game_dic[i]['e'][j]['i'][0],
                                         game_dic[i]['e'][j]['i'][1], j_info['fullmatch'], j_info['halfmatch'])
                info[game_name].append(final)
        return info
if __name__ == '__main__':
    print(data188())

