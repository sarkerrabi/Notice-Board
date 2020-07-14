import ssl
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Top10Notices:

    def nsu_top10_notice(self):
        withlink = []
        links = []
        listNotices = []
        url = 'http://www.northsouth.edu/nsu-announcements/?anaunc_start=0'
        source_code = urllib.request.urlopen(url)

        soup = BeautifulSoup(source_code.read(), "html.parser")
        count = 1
        for title in soup.find_all('div', {'class': 'post-scroller-item'}):
            for link in title.find_all('a'):
                listNotices.append(link.text + ' ')
                links.append('http://www.northsouth.edu/' + link.get('href'))
                count += 1
            if count > 10:
                break
            withlink = [listNotices, links]
        return withlink

    def aiub_top10_notice(self):
        listNotices = []
        linksNotices = []
        url = 'http://www.aiub.edu/'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), "html.parser")
        cnt = 1
        for li in soup.find_all('div', {'class': 'bs-callout'}):
            for link in li.find_all('a'):
                listNotices.append(link.text + ' ')
                linksNotices.append('http://www.aiub.edu' + link.get('href'))
                # print(str(cnt) + ' ' + link.text)
                # print('http://www.aiub.edu' + link.get('href'))
                cnt += 1
            if cnt > 10:
                break
            withlinks = [listNotices, linksNotices]
        return withlinks

    def bracu_top10_notice(self):
        listNotices = []
        linksNotices = []
        context = ssl._create_unverified_context()
        url = 'http://www.bracu.ac.bd/#announcement'
        source_code = urllib.request.urlopen(url, context=context)
        soup = BeautifulSoup(source_code.read(), "html.parser")
        count = 1
        for linkdiv in soup.find_all('div', {'class': 'calender-item clearfix'}):
            for link in linkdiv.find_all('a'):
                listNotices.append(link.text + ' ')
                linksNotices.append("http://www.bracu.ac.bd" + link.get('href'))
                # print(str(count) + ' ' + link.text)
                # print("http://www.bracu.ac.bd" + link.get('href'))
                count += 1
            if count > 10:
                break
            withLinks = [listNotices, linksNotices]
        return withLinks

    def ewu_top10_notice(self):
        listNotices = []
        linksNotices = []
        url = 'https://www.ewubd.edu/news/'
        source_code = urllib.request.urlopen(url)
        # print(source_code)
        soup = BeautifulSoup(source_code.read(), "html.parser")
        count = 1
        for linkdiv in soup.find_all('div', {'class': 'news-wrap news-wrap-height'}):
            link = linkdiv.find('h3')
            listNotices.append(link.text + ' ')
            linksNotices.append(url)
            # print(str(count) + ' ' + link.text)
            # print(url)
            count += 1

            if count > 10:
                break

            # listNotices.append(link.text + ' ')
            # linksNotices.append(link.get('href'))

        withlinks = [listNotices, linksNotices]

        return withlinks

    def iub_top10_notice(self):

        listNotices = []
        linksNotices = []
        url = 'http://www.iub.edu.bd/'

        sour_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(sour_code.read(), "html.parser")
        count = 1
        link_div = soup.find('div', {'class': 'col-lg-5 resources'})
        for link in link_div.find_all('a'):
            listNotices.append(link.text + ' ')
            linksNotices.append(link.get('href'))
            # print(str(count) + ' ' + link.text)
            # print(link.get('href'))
            count += 1
            if count > 10:
                break
        withlinks = [listNotices, linksNotices]
        return withlinks

    def iubat_top10_notice(self):
        listNotices = []
        linksNotices = []

        url = 'https://iubat.edu/notice/'
        driver = webdriver.Firefox()
        driver.get(url)

        try:
            wait = WebDriverWait(driver, 60)
            element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "vc_column-inner"))

            )

            source_code = driver.page_source
            soup = BeautifulSoup(source_code, 'html.parser')

            count = 1

            for link in soup.find_all('a', {'class': 'vc_gitem-link'}):

                listNotices.append(link.text + ' ')
                linksNotices.append(link.get('href'))
                # print(str(count) + ' ' + link.text)
                # print(link.get('href'))
                count += 1
                if count > 10:
                    break


        finally:
            driver.quit()

        withlinks = [listNotices, linksNotices]
        return withlinks

    def uiu_top10_notice(self):
        listNotices = []
        linksNotices = []

        url = 'http://www.uiu.ac.bd/notices/'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), 'html.parser')
        count = 1
        for souplink in soup.find_all('h2', {'class': 'entry-title'}):
            link = souplink.find('a')
            listNotices.append(link.text + ' ')
            linksNotices.append(link.get('href'))
            # print(str(count) + ' ' + link.text)
            # print(link.get('href'))
            count += 1
            if count > 10:
                break
        withlinks = [listNotices, linksNotices]
        return withlinks

    def seu_top10_notice(self):
        listNotices = []
        linksNotices = []

        url = 'https://www.seu.edu.bd/notice_board.php'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), 'html.parser')
        count = 1
        for link in soup.find_all('a', {'rel': 'facebox'}):
            listNotices.append(link.text + ' ')
            linksNotices.append(url + link.get('href'))
            # print(str(count) + ' ' + link.text)
            # print(url + link.get('href'))
            count += 1
            if count > 10:
                break
        withlinks = [listNotices, linksNotices]
        return withlinks

    def uniList(self):
        return ['North South University(NSU)', 'American International University-Bangladesh(AIUB)', 'BRAC University(BRACU)', 'East West University(EWU)', 'Independent University, Bangladesh(IUB)', 'International University of Business Agriculture and Technology (IUBAT)', 'United International University(UIU)', 'Southeast University(SEU)']

    def seu_top10_notice007(self):
        listNotices = []
        linksNotices = []
        withlinks = []
        url = 'http://www.seu.ac.bd/notice_board.php'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), 'html.parser')
        count = 1
        for link in soup.find_all('a', {'rel': 'facebox'}):
            listNotices.append(link.text + ' ')
            linksNotices.append(url + link.get('href'))
            # print(str(count) + ' ' + link.text)
            # print(url + link.get('href'))

            count += 1
            if count > 10:
                break
        withlinks = [listNotices, linksNotices]
        return withlinks
