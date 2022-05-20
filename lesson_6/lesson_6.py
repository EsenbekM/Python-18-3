import re

examole_list = [
    'AV Analytics Vidwya wV',
    'fV ABalytics Vidhya AV',
    'AV AnBlytwcs Vidhya AV',
    'BVwAnalytics VidBya Aw',
    'AV Analytics Vidhya AV',
    'Ab AnaBytics Vidhya wV',
    'AV Analyticw Vidhya AV',
]

# for i in examole_list:
#     if re.match(r"AV", i) is not None:
#         print(i)


#
# text = 'AV Analytics Vidhya AV'
#
# result = re.match(r"AV", text) ищет в начале строки
#
# result = re.search(r'Analytics', text) ищет расположение
#
# result = re.findall(r'AV', text) ищет все
#
# result = re.split(r'a', text) делит по указанному символу
#
# result = re.sub(r' ', ' - ', text) заменяет
#
#
#
# print(result)
#
#


with open("test_regs.txt", "r", encoding="utf-8") as file:
    content = file.read()
    # print(content)

    print(re.findall(r"fruits\[\d\]", content))
    print(re.findall(r"log\d*.txt", content))
    print(re.findall(r"\+996 [57]0[0-9 ]+", content))