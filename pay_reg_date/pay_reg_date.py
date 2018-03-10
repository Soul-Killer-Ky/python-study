import pymysql
import sys, datetime, time

db5config = {
    'host': '172.18.2.5',
    'port': 3306,
    'user': 'gaore_sdk',
    'pass': 'snFmr5obxfluix6Hbk',
    'dbname': 'sy_center',
    'charset': 'utf8'
}
dbconfig = {
    'host': '172.18.2.7',
    'port': 3306,
    'user': 'kaifa',
    'pass': 'MR7967zF',
    'dbname': 'db_www',
    'charset': 'utf8'
}

def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                back = True  # 整百年能被400整除的是闰年
            else:
                back = False
        else:
            back = True  # 非整百年能被4整除的为闰年
    else:
        back = False

def gen_date():
    global year1, year2, month1, month2, day1, day2
    if year1 < year2:
        if month1 == 2:
            if is_leap_year(year1):
                if day1 < 29:
                    day1 += 1
                else:
                    day1 = 1; month1 += 1
            else:
                if day1 < 28:
                    day1 += 1
                else:
                    day1 = 1; month1 += 1
        elif month1 in [1, 3, 5, 7, 8, 10, 12]:
            if month1 == 12:
                if day1 < 31:
                    day1 += 1
                else:
                    day1 = 1; month1 = 1; year1 += 1

try:
    pay_sdate_str = sys.argv[1]
    pay_edate_str = sys.argv[2]
    pay_sdate_str = datetime.date.fromtimestamp(time.mktime(time.strptime(pay_sdate_str, "%Y-%m-%d")))
    pay_edate_str = datetime.date.fromtimestamp(time.mktime(time.strptime(pay_edate_str, "%Y-%m-%d")))
    # pay_sdate = pay_sdate_str.isocalendar()
    # pay_edate = pay_edate_str.isocalendar()
    year1 = pay_sdate_str.year; month1 = pay_sdate_str.month; day1 = pay_sdate_str.day
    year2 = pay_edate_str.year; month2 = pay_edate_str.month; day2 = pay_edate_str.day

except IndexError as e:
    pay_sdate_str = datetime.datetime.now()
    # pay_sdate_str = now.strftime('%Y-%m-%d')
    delta = datetime.timedelta(days=1)
    pay_edate_str = pay_sdate_str + delta
    # pay_sdate = pay_sdate_str.isocalendar()
    # pay_edate = pay_edate_str.isocalendar()
    year1 = pay_sdate_str.year; month1 = pay_sdate_str.month; day1 = pay_sdate_str.day
    year2 = pay_edate_str.year; month2 = pay_edate_str.month; day2 = pay_edate_str.day

# print(year1, month1, day1, end='\n')
# print(year2, month2, day2, end='\n')

if year1 > year2 or (year1 == year2 and month1 > month2 or (year1 == year2 and month1 == month2 and day1 > day2)):
    print('参数错误')
    sys.exit(-1)

conn = pymysql.Connect(dbconfig)
cursor = conn.cursor()
conn5 = pymysql.Connect(db5config)
cursor5 = conn5.cursor()

while True:
    pay_sdate = str(year1) + '_' + str(month1) + '_' + str(day1)

    if year1 == year2 and month1 == month2 and day1 == day2:
        print('执行完成')
        break
    sql = "select "
