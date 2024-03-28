import re
# 匹配账号,只能由字母和数字组成,长度限制为6-10位
r = "^[a-zA-Z0-9]{6,10}$"  # ^ $表示从头开始匹配到尾部!!!
s = "1234567_"
print(re.findall(r, s))

# 匹配QQ号,要求纯数字,长度5-11,第一位不为0
r = "^[1-9][0-9]{4,10}$"
s = "012345678"
print(re.findall(r, s))

# 匹配邮箱地址,只允许qq,163,gmail这三种邮箱地址
r = r"(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)"
s = "a.b.c.d.e.f.g@qq.com.a.b.c.d.e"
print(re.findall(r, s))
