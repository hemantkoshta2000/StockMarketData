import bs4 as bs
import requests
import re

# url

login_URL = 'https://www.screener.in/login/'
data_URL = 'https://www.screener.in/screen/raw/?query=Market+Capitalization+%3E+1000+AND%0D%0AMarket+Capitalization+%3C+7000'

# credentials

form_data = {
    'username': 'hemantkoshta2000@gmail.com',
    'password': 'Him@98068'
}

# request config

form_csrf_key = 'csrfmiddlewaretoken'
cookie_csrf_key =    'RQ1RoVqljh97iFIk8MLgsaU6byQpBYCh'
cookie_session_key = 'lpmcyudypg6vkw1gudtm8s0rtj5aum9g'
content_type = 'text/html; charset=utf-8'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'

# get form_csrf_value & cookie_csrf_value
#'csrftoken=RQ1RoVqljh97iFIk8MLgsaU6byQpBYCh; expires=Sat, 05 Oct 2024 13:54:31 GMT; Max-Age=31449600; Path=/; SameSite=Lax; Secure'
get_login_request = requests.get(login_URL)
get_login_request_soup = bs.BeautifulSoup(get_login_request.text, 'html.parser')
form_csrf_value = get_login_request_soup.find('input', {'name': form_csrf_key})['value']
cookie_csrf_value = re.search(cookie_csrf_key + '=(.*?);', get_login_request.headers['Set-Cookie']).group(1)

# login into account & get cookie_session_value

form_data[form_csrf_key] = form_csrf_value

post_login_request = requests.post(login_URL, form_data, headers={
    'Cookie': cookie_csrf_key + '=' + cookie_csrf_value,
    'Content-Type': content_type,
    'User-Agent': user_agent,
    'Referer': login_URL
}, allow_redirects=False)

cookie_session_value = re.search(cookie_session_key + '=(.*?);', post_login_request.headers['Set-Cookie']).group(1)

# get data from the desired page

get_data_request = requests.get(data_URL, headers={
    'Cookie': cookie_csrf_key + '=' + cookie_csrf_value + ';' + cookie_session_key + '=' + cookie_session_value,
    'Content-Type': content_type,
    'User-Agent': user_agent,
})

get_data_request_soup = bs.BeautifulSoup(get_data_request.text, 'html.parser')
table_rows = get_data_request_soup.find('table', {'class': 'data-table'}).findAll('tr')