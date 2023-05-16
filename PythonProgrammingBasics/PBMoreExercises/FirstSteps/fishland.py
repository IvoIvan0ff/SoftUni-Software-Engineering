price_skum = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_seashell = int(input())

price_palamun = price_skum + (price_skum * 0.6)
total_palamud = price_palamun * kg_palamud
price_safrid = price_caca + (price_caca * 0.8)
total_safrid = price_safrid * kg_safrid
seashell_price = 7.50
seashell_total = kg_seashell * seashell_price
total_sum = total_palamud + total_safrid + seashell_total
print("%.2f" % total_sum)