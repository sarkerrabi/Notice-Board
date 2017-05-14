import urllib.request
from bs4 import BeautifulSoup

class Top10Notices:

    def nsu_top10_notice(self):
        withlink = []
        links = []
        listNotices = []
        url = 'http://www.northsouth.edu/nsu-announcements/?anaunc_start=0'
        source_code = urllib.request.urlopen(url)

        soup = BeautifulSoup(source_code.read(), "html.parser")
        count = 1
        for title in soup.find_all('h3'):
            # print(str(count) + ' ' + title.text)

            for link in title.find_all('a'):
                listNotices.append(link.text + ' ')
                links.append('http://www.northsouth.edu/' + link.get('href'))
                # print('http://www.northsouth.edu/' + link.get('href'))
                count += 1
            if count > 10:
                break
            withlink = [listNotices,links]
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
            withlinks = [listNotices,linksNotices]
        return withlinks

    def bracu_top10_notice(self):
        listNotices = []
        linksNotices = []
        url = 'http://www.bracu.ac.bd/news-archive?field_news_department_tid_selective=46'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), "html.parser")
        count = 1
        for linkdiv in soup.find_all('div', {'class': 'field-content title'}):
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
        url = 'http://www.ewubd.edu/category/news/'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), "html.parser")
        count = 1
        for link in soup.find_all('a', {'class': 'post_list_item_title h3'}):
            listNotices.append(link.text + ' ')
            linksNotices.append(link.get('href'))
            #
            # print(str(count) + ' ' + link.text)
            # print(link.get('href'))
            count += 1
            if count > 10:
                break
        withlinks = [listNotices,linksNotices]

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
        withlinks =[listNotices,linksNotices]
        return withlinks

    def iubat_top10_notice(self):
        listNotices = []
        linksNotices = []

        url = 'http://iubat.edu/web1/index.php/notice/'
        source_code = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code.read(), "html.parser")

        link_div1 = soup.find('section', {'class': 'fusion-columns columns fusion-columns-1 columns-1'})

        link_div2 = soup.find('div',
                              {'class': 'fusion-recent-posts avada-container layout-date-on-side layout-columns-1'})
        count = 1
        for link in link_div2.find_all('a'):
            link1 = link_div1.find('a')
            if link1 != link:
                listNotices.append(link.text + ' ')
                linksNotices.append(link.get('href'))
                # print(str(count) + ' ' + link.text)
                # print(link.get('href'))
                count += 1
                if count > 10:
                    break
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

    def uniList(self):
        return ['NSU','AIUB','BRACU','EWU','IUB','IUBAT','UIU','SEU']













