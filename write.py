from scrapping import search_each_period
from rds import write_db
from config import PAGE_MAX, PAGE_START
from push_periods import push_periods
from get_naver_cookies import get_naver_cookies

periods = push_periods()
print(periods) # temporary one day
cookies = get_naver_cookies()
sellings = search_each_period(periods, cookies)
print(sellings)

# sellings = scrapper(PAGE_START, PAGE_MAX)
# write_db(sellings)