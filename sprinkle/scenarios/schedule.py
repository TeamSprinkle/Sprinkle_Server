"""
  schedule.py
  Sprinkle

  Created by LeeKW on 2021/02/25.
"""
import datetime as dt


def do_schedule( Date, Subject, Time, Action):
    print("do_schedule function")
    print("Data : ")
    Date = cal_date(Date)
    print(Date)

    print("Subject : ")
    print(Subject)

    print("Time : ")
    print(Time)

    print("Action : ")
    print(Action)

    print('do_schedule function end' )


def cal_date( Date ):
    Date = Date.replace("까지", "")
    tempList = Date.split("부터")
    dateList = list()
    for temp in tempList:
        dateList.append(temp.split())

    nowDate = dt.datetime.now()
    resDate = list()

    for date in dateList:
        for data in date:
            if "일" in data:
                if "요일" in data:
                    data = cal_days(data, nowDate)
                else:
                    data = data.replace("일","")
                nowDate = nowDate.replace(day=int(data))
            elif "월" in data:
                data = data.replace("월","")
                nowDate = nowDate.replace(month=int(data))
            elif "년" in data:
                data = data.replace("년","")
                nowDate = nowDate.replace(year=int(data))  
            elif "달" in data:
                data = data.replace("달","")
                nowDate = nowDate + dt.timedelta(month=1)
            elif "주" in data:
                data = data.replace("주","")
                nowDate = nowDate + dt.timedelta(days=7)
        
        resDate.append(nowDate.strftime('%Y-%m-%d'))
    
    return resDate

def cal_days(data, date):
    days = [ '월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일' ]
    
    num = days.index(data)
    num = num - date.weekday()

    return date.day + num


"""
DATE = "3월 2일 부터 4일 까지"

list[0] = 3월, 2일
list[1] = 4일

cal_date( DATE )

    list = DATE를 부터 기준으로 리스트만들어

    now_date = 현재 시간 넣어

    {
        for ( list 개수만큼 )
        {
            list[0] 순회하면서 in [ 년, 월, 일, 달, 주] 있는지 확인
            년 -> now_date 에 년 치환
            월 ->
            일 ->

            달 -> now_date month +1 * x
            주 -> now date day + 7 * x
            (x는 다다의 개수    ex) 다음주 다다음주 다음달 다다음달 )
        } 
        list[] = 계산한 날짜 넣어
    }반복
"""