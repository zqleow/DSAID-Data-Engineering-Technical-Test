import json
import re
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


api_url = "https://api.covid19api.com/total/country/singapore/status/confirmed?from=2021-01-01T00:00:00Z&to=2021-08-08T00:00:00Z"
response = requests.get(api_url)

# responseBody = response.json()

covidCases = json.loads(response.text)
# print(covidCases)

caseNumList = []
dateConfirmedList = []


for case in covidCases:
    # print(case)

    # print(case["Cases"])

    caseNumList.append(case["Cases"])


    dateConfirmed = re.search(r'\d{4}-\d{2}-\d{2}', case["Date"])
    # print(dateConfirmed.group())
    dateConfirmedList.append(dateConfirmed.group())


print(caseNumList)
print(dateConfirmedList)

dict = {'caseNum': caseNumList, 'dateConfirmed': dateConfirmedList}
df = pd.DataFrame(dict)
# df.dateConfirmed = df.dateConfirmed.squeeze()
print(df)

chart = sns.lineplot(x = 'dateConfirmed', y = 'caseNum', data=df)
# chart = sns.lineplot(data=df)
# plt.xlabel("Date of Confirmation")
# plt.ylabel("Case Number")
# plt.plot('caseNum', 'dateConfirmed', data=df)
plt.show()


# plt.show()