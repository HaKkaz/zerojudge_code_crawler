from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_code(source : str):
	for i in range(len(source)): 
		if source[i:i+4] == 'code':
			l = i + 7
		if source[i:i+3] == 'pid':
			r = i - 3
		if source[i:i+6] == 'suffix':
			ext = source[i+9]
			break;

	ext = '.py' if ext == 'p' else '.cpp'

	# There are some characters will be change when submit to zerojudge.
	# Use replace() to get original characters.
	code = source[l:r].replace('&lt;','<').replace('&gt;','>').replace('&amp;','&')
	code = code.replace('\\r\\n','\n').replace('\\t','\t')
	code = code.replace('\\\\n','\n')
	code = code[:len(code)-2]

	# return code and extension of the file
	return code, ext


# Set the statue you wanna crawl, default is AC.
status = 'AC'
assert status in ['AC','WA','NA','TLE','OLE','RE','CE']

# MAX_PAGE should be max value of your page number of your AC submissions.
MAX_PAGE = 32

# Set your zerojudge account name here.
account_name = 'HaKkaz'

# Set the chromedrive path
drive_path = "C:Program Files\\Google\\Chrome\\Application\\chromedriver.exe"

# Set the folder path that you wanna store code.
folder_path = 'codes/'

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = drive_path
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

for page in range(1,MAX_PAGE):
	time.sleep(1)

	# go to the page of ac submissions, and get its html
	href_AC_submissions = 'https://zerojudge.tw/Submissions?page='+str(page)+'&&account='+account_name+'&status=' + status
	driver.get(href_AC_submissions)
	soup = BeautifulSoup(driver.page_source, 'html.parser')


	# get the solution_id list
	solution_ids = soup.find_all('td',{'id':'solutionid'})
	problem_ids = soup.find_all('td',{'width':'38%'})

	# get solution ids of current page
	IDs = []
	for item in solution_ids:
		ID = ""
		for c in item:
			if str(c).isdigit():
				ID += c
			elif len(ID) > 0:
				break;
		IDs.append(ID)

	# get problem ids of current page
	problem_IDs = []
	for item in problem_ids:
		item = str(item)
		for i in range(len(item)):
			if item[i].isalpha() and (item[i+1:i+4]).isdigit():
				problem_IDs.append(item[i:i+4])
				break;

	# Iterate all solution_id
	for idx in range(len(problem_ids)):
		time.sleep(1)
		ID = IDs[idx]
		problem_ID = problem_IDs[idx]

		# get the json file of AC submission.
		driver.get('https://zerojudge.tw/Solution.json?data=Code&solutionid='+ID)
		json_str = BeautifulSoup(driver.page_source, 'html.parser')

		# get code and language of this AC code.
		code, ext = get_code(str(json_str))

		# set the distination of your code
		code_path = folder_path+problem_IDs[idx]+ext 
		file = open(code_path, 'w' , encoding="utf8")
		file.write(str(code.replace('\r\n','\n')))
		file.close()
		print(f'problem : {problem_ID} done.')
	print(f'page : {page} done.')