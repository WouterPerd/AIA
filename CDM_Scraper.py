from bs4 import BeautifulSoup
import sys
import requests
import re

page = requests.get(sys.argv[1]).text
document = BeautifulSoup(page, "html.parser")
tr = document.find_all("tr")

# Project Title ICOMPLETE, still need to write code to scrape appendices!!!
projectInfo = str(tr[0].find("span")).replace("<span>", "").replace("</span>", "")
print("Project title:")
print(projectInfo)
x = int(0)
for link in tr[0].find_all("a", href=True):
    if x == 0:
        string = str("PDD: ")
    else:
        string = str("RRF: ")
    print(string + str(link['href']))
    x += 1
print()

# SDC Description Report. NB this part says 'Not Available' for most CDM Projects!!!
reportInfo = str(tr[1].find("strong")).replace("<strong>", "").replace("</strong>", "")
print("SDC description report:")
if reportInfo.__contains__("Not Available"):
    link = tr[0].find("a", href=True)
    print(reportInfo + "Please refer to our " + str(link['href']))
else:
    reportInfo = reportInfo + str(tr[1].find("span")).replace("<span>", "").replace("</span>", "")
    print(reportInfo)
print()

# Host Parties
countryName = str(tr[2].find("strong")).replace("<strong>", "").replace("</strong>", "")
print("Host Parties:")
print(countryName)
x = int(0)
for link in tr[2].find_all("a", href=True):
	if x == 0:
		string = str("Approval: ")
	else:
		string = str("Authorization: ")
	print(string + str(link['href']))
	x += 1
authorizedParticipants = str(tr[2].find("span"))
startInd = authorizedParticipants.index("Authorized")
stopInd = authorizedParticipants.rindex("</span>")
print(" ".join(authorizedParticipants[startInd:stopInd].split()))
print()

# Other Parties Involved
print("Other parties involved:")
for span in tr[3].find_all("span"):
	countryName = str(span.find("strong")).replace("<strong>", "").replace("</strong>", "")
	if (countryName == "None"):
		continue
	print(countryName)
	x = int(0)
	for link in span.find_all("a", href=True):
		if x == 0:
			string = str("Approval: ")
		else:
			string = str("Authorization: ")
		print(string + str(link['href']))
		x += 1
	startInd = str(span).index("Authorized")
	stopInd = str(span).rindex("</span>")
	print(" ".join(str(span)[startInd:stopInd].split()).replace(" <hr/>", ""))
print()

# Sectoral Scopes
scope = str(tr[4].find("td")).replace("<td>", "").replace("</td>", "")
print("Sectoral Scopes:")
print(" ".join(scope.split()))
print()

# Activity Scale
scaleValue = " ".join(tr[5].find("td").string.split())
print("Activity scale:")
print(scaleValue)
print()

# Methodologies Used
methodology = tr[6].find("a", title=True)
methodologyLink = tr[6].find("a", href=True)
print("Methodologies Used:")
print(str(methodology['title']) + " https://cdm.unfccc.int" + str(methodologyLink['href']))
print()

# Standardized Baselines Used
print("Standardized baseline used: N/A")
print()

# Amount of Reductions
reductionInfo = tr[8].find("td")
print("Amount of Reductions:")
print(" ".join(reductionInfo.string.split()))
print()

# Fee Level
fee = " ".join(str(tr[9].find("td").text).split())
print("Fee level:")
print(fee)
print()

# Validation Report
print("Validation Report:")
for a in tr[10].find_all("a", href=True):
	string = str(a.text)
	link = str(a['href'])
	print(string + " " + link)
print()

# Modalities of Communication. NB, need to write code for validation dates!!!
print("Modalities of Communication: ")
for a in tr[11].find_all("a", href=True):
	string = str(a.text)
	link = str(a['href'])
	print(string + " " + link)
print()

# Registration Date
date = str(tr[12].find("span").text)
print("Registration Date:")
print(date)
print()

# Crediting Period
text = tr[13].find("td").text
print("Crediting Period:")
print(" ".join(text.split()))
print()

# Requests for Issuance and Related Documentation. INCOMPLETE, does not scrape the values!!!
print("Requests for Issuance and Related Document:")
a = tr[14].find_all("a", href=True)
b = tr[14].find_all("b")
indA = int(0)
indB = int(0)
while True:
	try:
		print(str(b[indB].text) + ": " + str(a[indA]['href']))
		print(str(b[indB + 1].text))
		print(str(b[indB + 2].text))
		print(str(b[indB + 3].text))
		print("Full view and history -> " + str(a[indA + 1]['href']))
		indA += 2
		indB += 4
	except IndexError:
		break