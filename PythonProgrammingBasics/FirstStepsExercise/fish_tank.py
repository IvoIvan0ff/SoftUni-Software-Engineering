length = int(input())
width = int(input())
hight = int(input())
percent = float(input())

obem = length * width * hight
obem_v_l = obem * 0.001
covered_space = percent / 100

nujni_litri = obem_v_l * (1 - covered_space)
print(nujni_litri)