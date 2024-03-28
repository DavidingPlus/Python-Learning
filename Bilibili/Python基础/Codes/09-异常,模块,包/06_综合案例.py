from my_utils import str_util
from my_utils import file_util

print(str_util.str_reserse("hello"))
print(str_util.substr("  hello  ", 2, 7))

Pathname = "/mnt/d/Code/Python/Bilibili/异常,模块,包/test.txt"
file_util.print_file_info(Pathname)
file_util.append_to_file(Pathname, "hello")
