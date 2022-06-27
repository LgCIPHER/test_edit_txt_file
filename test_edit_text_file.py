import os
from re import I
from unittest import result

# Path of this file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Put the name of your text file here
src_doc_name = "test"
src_doc_type = ".txt"
src_doc_f_name = src_doc_name + src_doc_type
src_doc_dir = os.path.join(dir_path, src_doc_f_name)
src_doc_list = []

res_doc_name = src_doc_name
res_doc_type = ".txt"
res_doc_f_name = res_doc_name + "_v2" + res_doc_type
res_doc_dir = os.path.join(dir_path, res_doc_f_name)
res_doc_list = []

with open(src_doc_dir, mode='r', encoding='utf-8-sig') as src_doc:
    for line in src_doc:
        src_doc_list += line

res_doc_list = src_doc_list[:]

try:
    i = 0

    for letter in res_doc_list:
        if (i-1) > 0:
            previous_letter = res_doc_list[i-1]

            next_line_cond = (letter == "\n")
            end_line_cond = (previous_letter == ".") or (
                previous_letter == "?")
            first_word_cond = next_line_cond and end_line_cond

            if next_line_cond == True:
                if (not first_word_cond):
                    res_doc_list[i] = " "

        i += 1
except:
    print("Can't format this doc, will return the original verion...")

with open(res_doc_dir, mode='w', encoding='utf-8-sig') as res_doc:
    for line in res_doc_list:
        res_doc.write(line)

print("\nFinish running!")
