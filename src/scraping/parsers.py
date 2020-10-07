import requests
import codecs
import datetime
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ("hh_ru", "habr_com")

headers = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0",
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)"
                   "Chrome/49.0.2623.112 Safari/537.36",
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0",
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
           ]


def hh_ru(url):
    resp = requests.get(url, headers=headers[randint(0, 2)])
    hh_ru_jobs = []
    hh_ru_errors = []
    if resp.status_code == 200:
        soup = BS(resp.content, "html.parser")
        main_div = soup.find("div", attrs={"class": "vacancy-serp"})
        if main_div:
            div_list = main_div.find_all("div", attrs={"class": "vacancy-serp-item"})
            for div in div_list:
                title = div.find("span", attrs={"class": "g-user-content"})
                href = title.a["href"]
                title = title.a.text
                content_1 = div.find("div", attrs={"data-qa": "vacancy-serp__vacancy_snippet_responsibility"}).text
                content_2 = div.find("div", attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"}).text
                content = content_1 + "\n" + content_2
                company = div.find("div", attrs={"class": "vacancy-serp-item__meta-info"}).a.text
                hh_ru_jobs.append({"title": title, "url": href, "company": company, "description": content})
            else:
                hh_ru_errors.append({"url": url, "title": "Div does not exists."})
    else:
        hh_ru_errors.append({"url": url, "title": "Page do not response."})
    return hh_ru_jobs, hh_ru_errors


def habr_com(url):
    domain = "https://career.habr.com"
    resp = requests.get(url, headers=headers[randint(0, 2)])
    habr_com_jobs = []
    habr_com_errors = []
    if resp.status_code == 200:
        soup = BS(resp.content, "html.parser")
        main_div = soup.find("ul", attrs={"class": "card-list card-list--appearance-within-section"})
        if main_div:
            table_list = main_div.find_all("li", attrs={"class": "card-list__item"})
            for table in table_list:
                data_now = datetime.datetime.now().day
                data_site = table.find("time", attrs={"class": "basic-date"}).text
                data_site = data_site.split(" ")
                if data_now == int(data_site[0]):
                    title = table.find("div", attrs={"class": "vacancy-card__title"})
                    href = title.a["href"]
                    content = table.find("div", attrs={"class": "vacancy-card__skills"}).text
                    company = table.find("div", attrs={"class": "vacancy-card__meta"})
                    company = company.find("a", attrs={"class": "link-comp link-comp--appearance-dark"}).text
                    habr_com_jobs.append({"title": title.text, "url": domain + href, "company": company, "description": content})
                else:
                    break
        else:
            habr_com_errors.append({"url": url, "title": "Table does not exists."})
    else:
        habr_com_errors.append({"url": url, "title": "Page do not response."})
    return habr_com_jobs, habr_com_errors


if __name__ == "__main__":
    url = 0
    jobs_habr, errors_habr = habr_com(url)
    h = codecs.open("../hh_job.json", "w", "utf-8")
    h.write(str(jobs_habr))
    h.close()
    jobs_hh, errors_hh = habr_com(url)
    h = codecs.open("../habr_job.json", "w", "utf-8")
    h.write(str(jobs_hh))
    h.close()

