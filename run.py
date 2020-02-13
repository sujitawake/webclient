# Tested on: Python 3.7.3
import requests
import os.path
import schedule
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from eliot import start_action, to_file

# Overwrites log file in every program iteration
# Replace "w+" with "a+", if you want to append
to_file(open("log", "w+"))


# Check urls.txt presence, exit otherwise
if os.path.isfile('urls.txt'):
    pass
else:
    print('[-] ERR: urls.txt missing\n')
    exit(-1)


def do_crawl():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    headers = {'User-Agent': user_agent}
    urls = []

    # Read urls.txt
    with open('urls.txt', 'r') as fObj:
        filecontents = fObj.readlines()
    
        for line in filecontents:
            current_place = line[:-1]
            urls.append(current_place)

    # Initialize web crawler
    with start_action(action_type="domains_iterator"):
        print('[+] Exec on: %s' % str(time.strftime("%c")))
        for url in urls:
            try:
                with start_action(action_type="root_domain", source=url):
                    response = requests.head(url, verify=False, timeout=10,
                        headers=headers)
                    final_url = response.url
                    with start_action(action_type="redirect_url", target=final_url):
                        http_req = requests.get(final_url, verify=False, timeout=10,
                            headers=headers)
                        http_req.raise_for_status()
            except requests.exceptions.ConnectionError as e:
                pass
            except requests.exceptions.HTTPError as e:
                pass
            except requests.exceptions.ReadTimeout as e:
                pass
            except Exception as e:
                pass


do_crawl()


'''
# Monday (Offset: 40 minutes)
schedule.every().monday.at("08:10").do(do_crawl)
schedule.every().monday.at("08:50").do(do_crawl)
schedule.every().monday.at("09:30").do(do_crawl)
schedule.every().monday.at("10:10").do(do_crawl)
schedule.every().monday.at("10:50").do(do_crawl)
schedule.every().monday.at("11:30").do(do_crawl)
schedule.every().monday.at("12:10").do(do_crawl)
schedule.every().monday.at("12:50").do(do_crawl)
schedule.every().monday.at("13:30").do(do_crawl)
schedule.every().monday.at("14:10").do(do_crawl)
schedule.every().monday.at("14:50").do(do_crawl)
schedule.every().monday.at("15:30").do(do_crawl)
schedule.every().monday.at("16:10").do(do_crawl)
schedule.every().monday.at("16:50").do(do_crawl)

# Tuesday
schedule.every().tuesday.at("08:10").do(do_crawl)
schedule.every().tuesday.at("08:50").do(do_crawl)
schedule.every().tuesday.at("09:30").do(do_crawl)
schedule.every().tuesday.at("10:10").do(do_crawl)
schedule.every().tuesday.at("10:50").do(do_crawl)
schedule.every().tuesday.at("11:30").do(do_crawl)
schedule.every().tuesday.at("12:10").do(do_crawl)
schedule.every().tuesday.at("12:50").do(do_crawl)
schedule.every().tuesday.at("13:30").do(do_crawl)
schedule.every().tuesday.at("14:10").do(do_crawl)
schedule.every().tuesday.at("14:50").do(do_crawl)
schedule.every().tuesday.at("15:30").do(do_crawl)
schedule.every().tuesday.at("16:10").do(do_crawl)
schedule.every().tuesday.at("16:50").do(do_crawl)

# Wednesday
schedule.every().wednesday.at("08:10").do(do_crawl)
schedule.every().wednesday.at("08:50").do(do_crawl)
schedule.every().wednesday.at("09:30").do(do_crawl)
schedule.every().wednesday.at("10:10").do(do_crawl)
schedule.every().wednesday.at("10:50").do(do_crawl)
schedule.every().wednesday.at("11:30").do(do_crawl)
schedule.every().wednesday.at("12:10").do(do_crawl)
schedule.every().wednesday.at("12:50").do(do_crawl)
schedule.every().wednesday.at("13:30").do(do_crawl)
schedule.every().wednesday.at("14:10").do(do_crawl)
schedule.every().wednesday.at("14:50").do(do_crawl)
schedule.every().wednesday.at("15:30").do(do_crawl)
schedule.every().wednesday.at("16:10").do(do_crawl)
schedule.every().wednesday.at("16:50").do(do_crawl)

# Thursday
schedule.every().thursday.at("08:10").do(do_crawl)
schedule.every().thursday.at("08:50").do(do_crawl)
schedule.every().thursday.at("09:30").do(do_crawl)
schedule.every().thursday.at("10:10").do(do_crawl)
schedule.every().thursday.at("10:50").do(do_crawl)
schedule.every().thursday.at("11:30").do(do_crawl)
schedule.every().thursday.at("12:10").do(do_crawl)
schedule.every().thursday.at("12:50").do(do_crawl)
schedule.every().thursday.at("13:30").do(do_crawl)
schedule.every().thursday.at("14:10").do(do_crawl)
schedule.every().thursday.at("14:50").do(do_crawl)
schedule.every().thursday.at("15:30").do(do_crawl)
schedule.every().thursday.at("16:10").do(do_crawl)
schedule.every().thursday.at("16:50").do(do_crawl)

# Friday
schedule.every().friday.at("08:10").do(do_crawl)
schedule.every().friday.at("08:50").do(do_crawl)
schedule.every().friday.at("09:30").do(do_crawl)
schedule.every().friday.at("10:10").do(do_crawl)
schedule.every().friday.at("10:50").do(do_crawl)
schedule.every().friday.at("11:30").do(do_crawl)
schedule.every().friday.at("12:10").do(do_crawl)
schedule.every().friday.at("12:50").do(do_crawl)
schedule.every().friday.at("13:30").do(do_crawl)
schedule.every().friday.at("14:10").do(do_crawl)
schedule.every().friday.at("14:50").do(do_crawl)
schedule.every().friday.at("15:30").do(do_crawl)
schedule.every().friday.at("16:10").do(do_crawl)
schedule.every().friday.at("16:50").do(do_crawl)

# Run the task indefinitely (unless stopped explicitly)
while True:
    schedule.run_pending()
    time.sleep(1)

'''
