from bs4 import BeautifulSoup
import requests
import os
os.environ["PARSE_API_ROOT"] = "https://astanasu.herokuapp.com/parse"
from parse_rest.datatypes import Function, Object, GeoPoint
from parse_rest.connection import register
from parse_rest.query import QueryResourceDoesNotExist
from parse_rest.connection import ParseBatcher
from parse_rest.core import ResourceRequestBadRequest, ParseError

APPLICATION_ID = 'AberdeenGirl'
REST_API_KEY = 'AberdeenGirlClient'
MASTER_KEY = 'AberdeenMasterKey'

register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)


class Programme(Object):
    pass
class SubProgramm(Object):
	pass
base_link = "https://budget.egov.kz"
def parseBasic(number): 
	headers = {'Accept-Language': 'ru-RU'}
	result = requests.get("https://budget.egov.kz/budgetprogram/budgetprogram?page="+number+"&budgetState=APPROVED",headers = headers, verify=False)
	return result.content
def parseDetailed(link):
	headers = {'Accept-Language': 'ru-RU'}
	result = requests.get(link,headers = headers, verify=False)
	return result.content
subProgrammes = []

for page in range(1,135):
	html = parseBasic(str(page))
	soup = BeautifulSoup(html)
	samples = soup.find_all("a", "bpname")
	for sample in samples:
		subProgrammes = []
		link = base_link+sample['href']+"&lang=ru"
		text = sample.getText().rstrip()
		html_detailed = parseDetailed(link)
		suop_detailed = BeautifulSoup(html_detailed)
		headers = tables = suop_detailed.find_all("h1")
		header = headers[0]
		tables = suop_detailed.find_all("td")
		oldlen = len(tables)
		for longtables in range(0,len(tables)*5):
			tables.append(tables[longtables])
		print(tables[21].getText().rstrip())
		name = header.getText() # Nazvanie Programmi
		administrator_budget_program = tables[1].getText() # Администратор бюджетных программ
		budget_programm = tables[3].getText()
		head_budget_programm = tables[5].getText()
		print(head_budget_programm)
		norm_prav_osnova = tables[7].getText()
		opisanie_obosnovanie = tables[9].getText()
		vid_gos_upr = tables[11].getText()
		vid_gos_sod = tables[13].getText()
		vid_soc_real = tables[15].getText()
		tekushee_ili_razvitie = tables[17].getText()
		goal = tables[19].getText()
		zadacha = tables[21].getText()
		year = tables[23].getText()
		howmany = 0
		start = 0
		money_type = 'тенге'
		budget_2016 = 0
		budget_2017 = 0
		budget_2018 = 0
		budget_2019 = 0
		budget_2020 = 0
		once = True
		overallindex = 0
		for q in range(0, oldlen):
			if tables[q].getText().rstrip()=="Расходы по бюджетной программе, всего":
				print('start')
				start = q
			if (("Итого расходы по бюджетной" in tables[q].getText().rstrip()) and once):
				print(tables[q].getText().rstrip())
				once = False
				overallindex = q
				howmany = int((q - start)/7)
				print(howmany)
		money_type = tables[overallindex+1].getText()
		budget_2016 = tables[overallindex+2].getText()
		budget_2017 = tables[overallindex+3].getText()
		budget_2018 = tables[overallindex+4].getText()
		budget_2019 = tables[overallindex+5].getText()
		budget_2020 = tables[overallindex+6].getText()
		programm = Programme(name = name, administrator_budget_program = administrator_budget_program, budget_programm = budget_programm, norm_prav_osnova = norm_prav_osnova, opisanie_obosnovanie=opisanie_obosnovanie,vid_gos_upr=vid_gos_upr,vid_gos_sod=vid_gos_sod,vid_soc_real=vid_soc_real,tekushee_ili_razvitie=tekushee_ili_razvitie,goal=goal,zadacha=zadacha,year=year,money_type=money_type,budget_2016=budget_2016,budget_2017=budget_2017,budget_2018=budget_2018,budget_2019=budget_2019,budget_2020=budget_2020)
		programm.save()	
		for o in range(0,howmany):
			start = o*7+start
			sp = SubProgramm(name = tables[start+1].getText(),money_type = tables[start+2].getText(),budget_2016 = tables[start+3].getText(),budget_2017 = tables[start+4].getText(),budget_2018 = tables[start+5].getText(),budget_2019 = tables[start+6].getText(),budget_2020 = tables[start+7].getText())
			relation = programm.relation('subProgrammes')
			relation.add([sp])


		




	

