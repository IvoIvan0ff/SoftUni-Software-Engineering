deposit = float(input())
months = int(input())
yearly_rate = float(input())




total_sum = deposit + months * ((deposit * yearly_rate / 100) / 12)
print(total_sum)