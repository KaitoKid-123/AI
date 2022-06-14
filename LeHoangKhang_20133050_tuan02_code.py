# %%
"""1. Cho numpy array có các phần tử: [-2 6 3 10 15 48], viết lệnh (không sử dụng vòng lặp) để lấy ra 
các bộ phần tử: [3 15], [6 10 48], [10 15 48], [48 15 10]. Gợi ý: slicing Python.
"""
import numpy as np
Arr = np.array([-2, 6, 3, 10, 15, 48])
print(Arr[2:5:2])
print(Arr[1::2])
print(Arr[3:])
print(Arr[-1:-4:-1])
# %%
"""2. Tạo một 2D numpy array và thử dùng các hàm max(), max(0), max(1) để để thấy sự khác biệt. 
Cú pháp: ten_mang.max().
"""
import numpy as np
Arr2D = np.random.random((5, 5))
print(Arr2D)
print(Arr2D.max())
print(Arr2D.max(0))
print(Arr2D.max(1))
# %%
"""3. Viết hàm giải phương trình bậc 1 và bậc 2. Các hệ số của phương trình là tham số của hàm. 
Yêu cầu: Thiết kế hàm sao cho người dùng nhập vào phương trình bậc 1 hay bậc 2 đều được và 
tự động giải phương trình tương ứng. 
"""
from math import sqrt
def GiaiPT(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Vo so nghiem"
            else:
                return "Vo nghiem"
        else:
            return f"x = {-c/b}"
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            return "Vo nghiem"
        elif delta == 0:
            return f"x1 = x2 = {-b/2*a}"
        else:
            x1 = (-b + sqrt(delta))/(2*a)
            x2 = (-b - sqrt(delta))/(2*a)
            return f"x1 = {x1}, x2 = {x2}"
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
GiaiPT(a, b, c)
# %%
"""5. Viết hàm có hai tham số là một mảng số bất kỳ và một tham số boolean tên SapXepTang. 
Nếu tham số SapXepTang có giá trị True thì sắp xếp mảng tăng dần, có giá trị False thì sắp giảm dần. Yêu cầu: dùng for sắp xếp mảng, 
dùng numpy array để chứa mảng. Nếu người dùng không nhập SapXepTang thì mặc định là sắp tăng dần.
Gợi ý: Dùng hàm array() để tạo mảng, và dùng thuộc tính size để biết số phần tử mảng, ví dụ:
mang = numpy.array([4,3,5,6])
mang.size # tra ve 4
"""
def sort(lis, SapXepTang = True):
    if SapXepTang == True:
        for i in range(len(lis) - 1):
            for j in range(i + 1, len(lis)):
                if lis[i] > lis[j]:
                    temp = lis[i]
                    lis[i] = lis[j]
                    lis[j] = temp
    else:
        for i in range(len(lis) - 1):
            for j in range(i + 1, len(lis)):
                if lis[i] < lis[j]:
                    temp = lis[i]
                    lis[i] = lis[j]
                    lis[j] = temp
    return lis

arr = [1, 2, 3, 4, 5]
sort(arr, False)