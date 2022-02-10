from bs4 import BeautifulSoup
from django.http import HttpResponse
from main.models import Account
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from django.http import HttpResponse

def home(request):
    URL = "https://etherscan.io/accounts/"
    opts = webdriver.ChromeOptions()
    # opts.headless = True
    opts.add_argument("--enable-javascript")
    opts.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    r = browser.get(URL)

    select = Select(browser.find_element_by_name('ctl00$ContentPlaceHolder1$ddlRecordsPerPage'))
    # select = Select(browser.find_element_by_id('ContentPlaceHolder1_ddlRecordsPerPage'))

    select.select_by_value("100")

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    table = soup.find('table', attrs={'class':'table table-hover'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        address1 = cols[1].text
        balance1 = cols[3].text
        percentage1 = float(cols[4].text[:len(cols[4].text)-1])
        account = Account(rank=1, address=address1, balance=balance1, percentage=percentage1)
        account.save()

    context = {
        'accounts': Account.objects.all(),
    }
    return render(request, 'main/top_accounts.html', context)

def Statistics(request):
    context = {
        'accounts': Account.objects.all(),
    }
    return render(request, 'main/statistics.html', context)