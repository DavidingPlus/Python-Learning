mystr = "万过薪月,员序程马黑来,nohtyp学"

target = "黑马程序员"
newmystr = mystr[::-1]
index = newmystr.index(target)
print(newmystr[index:index+len(target)])
