from Summarizer import summary
# from select_file import open_file
# text = open_file()
# print("Okay 👍")
# strength = int(input("Enter the strength of summarizing the text between 1 to 9"))
# save_as = input("Save as (only enter the name of the file don't put any extension)")
# from Verse import verse
#
# # sum = summary(input("Enter your text"),int(input("Enter a number between 1 to 10")))
# final_text = verse(input())
# # print("ji")
# for each_line in final_text:
#     each_line = each_line.replace('[', '')
#     each_line = each_line.replace(']', '')
#     each_line = each_line.replace("'", '')
#     each_line = each_line.replace(',', '')
#     each_line = each_line.replace('''"''', '')
#     print
text = input()
from Summarizer import summary
sum = summary(text)
# from verse2 import Verse2
# ver = Verse2(sum)
print(sum)