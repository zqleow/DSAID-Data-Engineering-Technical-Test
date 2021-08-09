import json
import re
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


api_url = "https://api.covid19api.com/total/country/singapore/status/confirmed?from=2021-01-01T00:00:00Z&to=2021-08-08T00:00:00Z"
response = requests.get(api_url)
covidCases = json.loads(response.text)

caseNumList = []
dateConfirmedList = []


for case in covidCases:
    caseNumList.append(case["Cases"])

    dateConfirmed = re.search(r'\d{4}-\d{2}-\d{2}', case["Date"])

    dateConfirmedList.append(dateConfirmed.group())


print(caseNumList)
print(dateConfirmedList)

dict = {'caseNum': caseNumList, 'dateConfirmed': dateConfirmedList}
df = pd.DataFrame(data=dict, columns=['caseNum', 'dateConfirmed'])

# Convert date format to simplified (MMM DD)
dt = pd.to_datetime(df['dateConfirmed'])
dt = dt.apply(lambda x: x.strftime('%b %d'))
print(dt)
df['dateConfirmed'] = dt
print(df)


chart = sns.lineplot(x='dateConfirmed', y='caseNum', data=df).set_title(
    'Trend of increase in number of COVID-19 cases in Singapore by months (2021)')
# chart = sns.lineplot(data=df)
plt.xlabel("Period")
plt.ylabel("Case Number")

X = plt.gca().xaxis
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')

# Adjust x axis to display just months
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)

plt.show()
