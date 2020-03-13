from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import webbrowser

# Create your views here.


def home(request):
    return render(request, 'home.html')

# 금일 환율 변환 계산


def vnd(request):
    url_nvday = 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_VNDKRW'
    response = requests.get(url_nvday)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.select('div.section_exchange > table > tbody > tr')

    dfcontent = []
    for cont in contents:
        tds = cont.find_all('td')
        for td in tds:
            dfcontent.append(td.text)

    rate_all = []  # 환율 기록 list
    i = 1  # dfcontents 리스트에서 매 9번마다 위치하는 원동화 환율 리스트에 저장.
    while i < len(dfcontent):
        rate_all.append(dfcontent[i])
        i += 9

    rate_all = [float(i) for i in rate_all]  # str 값 float으로 변환하여 리스트로 재반환.
    rate_today = float(rate_all[0])
    rate_yesterday = float(rate_all[1])
    rate_weekAVG = round(sum(rate_all)/len(rate_all), 2)
    amt = float(request.GET['amount'])

    VNDKRW_TODAY = round(amt * rate_today * 0.01)
    VNDKRW_YESTERDAY = round(amt * rate_yesterday * 0.01)
    VNDKRW_weekAVE = round(amt * rate_weekAVG * 0.01)

    # Format 형태로 변환하여 자릿수 표시
    amt_format = format(amt, ',')
    VNDKRW_TODAY_format = format(VNDKRW_TODAY, ',')
    low_yesterday = format(VNDKRW_YESTERDAY - VNDKRW_TODAY, ',')
    high_yesterday = format(VNDKRW_TODAY - VNDKRW_YESTERDAY, ',')
    low_week = format(VNDKRW_weekAVE - VNDKRW_TODAY, ',')
    high_week = format(VNDKRW_TODAY - VNDKRW_weekAVE, ',')

    compare_today_yesterday = []
    compare_today_week = []

    if rate_today < rate_yesterday:
        compare_today_yesterday = ["만약 어제 환전 하셨다면",
                                   low_yesterday, "원 만큼 더 이익이셨어요 ㅠ"]
    elif rate_today == rate_yesterday:
        compare_today_yesterday = ["어제나 오늘이나 환율이 똑같아요"]
    else:
        compare_today_yesterday = ["오늘 환전하셔서 어제보다",
                                   high_yesterday, "원 만큼 이익 보셨어요~!"]

    if rate_today < rate_weekAVG:
        compare_today_week = ["10일간 평균 환율은", rate_weekAVG, "이며 금일 환율로 환전시 평소보다",
                              low_week, "원 손해 입니다."]

    elif rate_today == rate_weekAVG:
        compare_today_week = ["요즘은 환율 변동이 크게 없네요"]

    else:
        compare_today_week = ["10일간 평균 환율은", rate_weekAVG, "이며 금일 환율로 환전시 평소보다",
                              high_week, "원 이득 입니다."]

    return render(request, 'vnd.html', {"amt": amt, "amt_format": amt_format, "VNDKRW_TODAY_format": VNDKRW_TODAY_format, "rate_today": rate_today, "rate_yesterday": rate_yesterday, "rate_weekAVG": rate_weekAVG, "VNDKRW_TODAY": VNDKRW_TODAY, "VNDKRW_YESTERDAY": VNDKRW_YESTERDAY, "VNDKRW_weekAVE": VNDKRW_weekAVE, "compare_today_yesterday": compare_today_yesterday, "compare_today_week": compare_today_week})


def krw(request):
    url_nvday = 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_VNDKRW'
    response = requests.get(url_nvday)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.select('div.section_exchange > table > tbody > tr')

    dfcontent = []
    for cont in contents:
        tds = cont.find_all('td')
        for td in tds:
            dfcontent.append(td.text)

    rate_all = []  # 환율 기록 list
    i = 1  # dfcontents 리스트에서 매 9번마다 위치하는 원동화 환율 리스트에 저장.
    while i < len(dfcontent):
        rate_all.append(dfcontent[i])
        i += 9

    rate_all = [float(i) for i in rate_all]  # str 값 float으로 변환하여 리스트로 재반환.
    rate_today = float(rate_all[0])
    rate_yesterday = float(rate_all[1])
    rate_weekAVG = round(sum(rate_all)/len(rate_all), 2)
    amt = float(request.GET['amount'])

    # ??? 왜 round 1 만 넣어도 결과값은 소수점이 많이 나오는지..
    KRWVND_TODAY = round(amt * 100 / rate_today)
    KRWVND_YESTERDAY = round(amt * 100/rate_yesterday)
    KRWVND_weekAVE = round(amt * 100 / rate_weekAVG)

    amt_format = format(amt, ',')
    KRWVND_TODAY_format = format(KRWVND_TODAY, ',')
    low_yesterday = format(KRWVND_YESTERDAY - KRWVND_TODAY, ',')
    high_yesterday = format(KRWVND_TODAY - KRWVND_YESTERDAY, ',')
    low_week = format(KRWVND_weekAVE - KRWVND_TODAY, ',')
    high_week = format(KRWVND_TODAY - KRWVND_weekAVE, ',')

    compare_today_yesterday = ()
    compare_today_week = ()

    if rate_today > rate_yesterday:
        compare_today_yesterday = (
            "만약 어제 환전 하셨다면", low_yesterday, "VND 만큼 더 이익이셨어요 ㅠ")
    elif rate_today == rate_yesterday:
        compare_today_yesterday = ("어제나 오늘이나 환율이 똑같아요")
    else:
        compare_today_yesterday = (
            "오늘 환전하셔서 어제보다", high_yesterday, "VND 만큼 이익 보셨어요~!")

    if rate_today > rate_weekAVG:
        compare_today_week = ("10일간 평균 환율은", rate_weekAVG, "이며 금일 환율로 환전시 평소보다",
                              low_week, "VND 손해 입니다.")

    elif rate_today == rate_weekAVG:
        compare_today_week = ("요즘은 환율 변동이 크게 없네요")

    else:
        compare_today_week = ("10일간 평균 환율은", rate_weekAVG, "이며 금일 환율로 환전시 평소보다",
                              high_week, "VND 이득 입니다.")

    return render(request, 'krw.html', {"amt": amt, "amt_format": amt_format, "KRWVND_TODAY_format": KRWVND_TODAY_format, "rate_today": rate_today, "rate_yesterday": rate_yesterday, "rate_weekAVG": rate_weekAVG, "KRWVND_TODAY": KRWVND_TODAY, "KRWVND_YESTERDAY": KRWVND_YESTERDAY, "KRWVND_weekAVE": KRWVND_weekAVE, "compare_today_yesterday": compare_today_yesterday, "compare_today_week": compare_today_week})
