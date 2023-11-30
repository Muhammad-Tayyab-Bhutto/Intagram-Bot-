# web driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# for pressing enter key
from selenium.webdriver.common.keys import Keys
# for sleep
from time import sleep

browser = webdriver.Chrome()

browser.implicitly_wait(1)

url = 'https://www.instagram.com/'
browser.get(url)

sleep(2)

username_input = browser.find_element("xpath", "//input[@name='username']")
password_input = browser.find_element("xpath", "//input[@name='password']")

# credentials
username = 'ashiambreen32'
password = 'raeela123'
target = 'muhammad_tayyab_bhutto'

username_input.send_keys(username)
print('usernme is entered')
sleep(3)
password_input.send_keys(password)
print('passwrod entered')

sleep(1)
login_button = browser.find_element("xpath", "//button[@type='submit']")
login_button.click()


print('login successfull')

sleep(5)
# try:
#     save_login_dialog = browser.find_element("xpath", "//main[@role='main']")
#     print('got the dialog!')
#     not_button = browser.find_element("xpath", "//div[@class='cmbtv']/button")
#     not_button.click()
#     print('no login save clicked!')
# except:
#     print("didn't get dialog")

# sleep(5)

# try:
#     not_now_button = browser.find_element("xpath", "//button[@class='_a9-- _a9_1']")
#     not_now_button.click()
# except:
#     print('Error while not_now_button')

# sleep(5)

# search_bar = browser.find_element("xpath", "//input[@placeholder='Search']")
# search_bar.send_keys(target)

browser.get(url + target)
sleep(5)
print('reached to profile!')

browser.get(url + target + '/followers/')


print('reached to followers')
sleep(10)
followers_dialog = browser.find_element("xpath", "//div[@role='dialog']")
# browser.execute_script("document.querySelector('.dialog').scrollIntoView(true);", followers_dialog)
sleep(10)


followers_dialog_inner = followers_dialog.find_element('xpath', ".//div[@class='_aano']")
followers_dialog_inner1 = followers_dialog_inner.find_element('xpath', ".//div")




# additional class
class infine_scroll(object):
   
  def __init__(self, last):
    
    self.last = last

  def __call__(self, browser):
    new = browser.execute_script('return document.querySelector("._aano").scrollHeight')  
    if new > self.last:
        return new
    else:
        return False




last_height = browser.execute_script('return document.querySelector("._aano").scrollHeight')
flag=1
while flag==1:

  browser.execute_script('window.scrollTo(0,document.querySelector("._aano").scrollHeight)')

  try:
   wait = WebDriverWait(browser, 10)

   new_height = wait.until(infinite_scroll( last_height))
   last_height = new_height

  except:
      print("End of page reached")
      flag = 0


print("Height: ", followers_dialog_inner1.size['height'])

print('clicked down scroll!')
followers_dialog = browser.find_element("xpath", "//div[@role='dialog']")
followers = followers_dialog.find_elements('xpath', ".//a[@role='link']")
# followers = browser.find_elements("xpath", "//div[@role='dialog']//a[12]")
# browser.execute_script("arguments[0].scrollIntoView(true);", followers)


print('printing followers')
print(followers)
print('printed\n\n')
followers_links = [follower.get_attribute('href') for follower in followers]
print('printing links')
print(followers_links)
print('links printed')
sleep(9999999)

browser.close()




# <div class="_aacl _aacp _aacu _aacx _aad6 _aade"><span class="_ac2a" title="127">127</span> followers</div>