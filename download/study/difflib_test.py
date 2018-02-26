import os
import difflib
import sys



def compare():
    argument1 = "bug1.py"
    argument2 = "bug2.py"
    f1 = open(argument1,"r")
    f1_list = f1.readlines()

    f1.close()
    f2 = open(argument2,"r")
    f2_list = f2.readlines()
    f2.close()

    d = difflib.HtmlDiff()
    html = d.make_file(f1_list, f2_list)
    # print(html)
    with open("diff.html","w") as  f:
        f.write(html)

def diff2(text1_lines,text2_lines):
    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    print(join(diff))



if __name__ == '__main__':
    compare()
