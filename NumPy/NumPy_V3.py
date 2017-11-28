import numpy as np


def read_height_weight():
    list_hw = []
    for k in range(int(input())):
        h, w = input().split()
        list_hw.append((int(h), int(w)))
    return np.array(list_hw)


def cm_to_m(x):
    return x / 100


def cal_bmi(hw):
    height_in_m = cm_to_m(hw[:, 0])
    return hw[:, 1] / height_in_m ** 2


def main():
    hw = read_height_weight()
    bmi = cal_bmi(hw)
    avg_bmi = np.sum(bmi) / np.size(bmi)
    count_underweight = len(bmi[np.where(bmi < 18.5)])
    print('average bmi =', avg_bmi)
    print('#bmi < 18.5 =', count_underweight)


exec(input().strip())
