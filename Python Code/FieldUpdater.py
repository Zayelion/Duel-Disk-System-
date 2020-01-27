from bs4 import BeautifulSoup


def Modify_Field_Value(Card,zone,card_img,position,delete):
	Dict_correspondence = { 'P1MZ1': 'P1info1', 
							'P1MZ2': 'P1info2',  
							'P1MZ3': 'P1info3',  
							'P1MZ4': 'P1info4',  
							'P1MZ5': 'P1info5',  
							'P2MZ1': 'P2info1', 
							'P2MZ2': 'P2info2',  
							'P2MZ3': 'P2info3',  
							'P2MZ4': 'P2info4',  
							'P2MZ5': 'P2info5',  
	}
	P2infos = ['P2info1','P2info2','P2info3','P2info4','P2info5',]

	with open('DashboardTest.html') as html_file:
		soup = BeautifulSoup(html_file.read(), features='html.parser')

		new_tag = soup.new_tag("img")
		new_tag['src'] = card_img
		new_tag['class'] = position
		new_tag['id'] = zone

		for tag in soup.find_all(id=zone):
			tag.replace_with(new_tag)

		new_tag = soup.new_tag("p")
		new_tag['class'] = "futurepanel__title"
		new_tag['id'] = Dict_correspondence[zone]
		if not delete:
			new_tag.string = str(Card['atk'])+' / '+str(Card['def'])
		else:
			new_tag.string ='ATK/DEF'

		if Dict_correspondence[zone] in P2infos:
			new_tag['style'] = "transform: rotate(180deg);"

		for tag in soup.find_all(id=Dict_correspondence[zone]):
			tag.replace_with(new_tag)

		new_text = soup.prettify()

	with open('DashboardTest.html', mode='w') as new_html_file:
		new_html_file.write(new_text)


def Modify_Field_Value_Spells(Card,zone,card_img,position):
	Dict_correspondence = { 'P1MZ1': 'P1info1', 
							'P1MZ2': 'P1info2',  
							'P1MZ3': 'P1info3',  
							'P1MZ4': 'P1info4',  
							'P1MZ5': 'P1info5',  
							'P2MZ1': 'P2info1', 
							'P2MZ2': 'P2info2',  
							'P2MZ3': 'P2info3',  
							'P2MZ4': 'P2info4',  
							'P2MZ5': 'P2info5',  
	}
	P2infos = ['P2info1','P2info2','P2info3','P2info4','P2info5',]

	with open('DashboardTest.html') as html_file:
		soup = BeautifulSoup(html_file.read(), features='html.parser')

		new_tag = soup.new_tag("img")
		new_tag['src'] = card_img
		new_tag['class'] = position
		new_tag['id'] = zone

		for tag in soup.find_all(id=zone):
			tag.replace_with(new_tag)

		new_text = soup.prettify()

	with open('DashboardTest.html', mode='w') as new_html_file:
		new_html_file.write(new_text)