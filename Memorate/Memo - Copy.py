from verse2 import Verse2
text = input()
final_text = Verse2(text)
for each_line in final_text:
    each_line = each_line.replace('[', '')
    each_line = each_line.replace(']', '')
    each_line = each_line.replace("'", '')
    each_line = each_line.replace(',', '')
    each_line = each_line.replace('''"''', '')
    print(each_line)