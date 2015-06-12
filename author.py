
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
with open("myfile.txt") as f:
    content = f.readlines()
print content

driver = webdriver.Firefox()



driver.find_element_by_name("submit").click()
for x in content:
	x=x.rstrip()

	authorname = driver.find_element_by_name("author_name")
	authorph = driver.find_element_by_name("author_ph")
	authordes = driver.find_element_by_name("author_desig")
	authoremail = driver.find_element_by_name("author_email")
	authorname.send_keys(x)
	authorph.send_keys("+91 9349151985")
	authordes.send_keys("Assistant Professor")
	authoremail.send_keys("drprvarghese@rediffmail.com")
	driver.find_element_by_name("submit").click()
