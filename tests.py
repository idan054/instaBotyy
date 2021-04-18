_string = """
https://www.instagram.com/king____shoes/
https://instagram.com/ed.shoes.co.il?igshid=vlmlvjyyknu0
https://instagram.com/captain_shoes_il?igshid=1xyg3vx2me8zk
https://instagram.com/mrshoesil?igshid=y75zk6g99ddx
https://instagram.com/shoezwebstore?igshid=rjdcol463dqn
https://instagram.com/shoes_x_?igshid=1rh5lrxrxbln7
https://instagram.com/top_shoes.il?igshid=1l7m65pcqvo64
https://instagram.com/shoesonline.co.il?igshid=1gkj0ba0zabam
https://instagram.com/hypeshoes.il?igshid=1ezd79asn6hm2
https://instagram.com/professor_shoes_il?igshid=77oba6wg2nl3
https://instashoe_il?igshid=166q0t376bpdu
https://instagram.com/shose_plus.il?igshid=1hsqsfzxb62p7
https://instagram.com/style_shoes_il?igshid=ccxfietof5sk
https://instagram.com/romi__shoes?igshid=1gybr67cgsq7k
https://instagram.com/shoeline_il?igshid=xee341yjf1nx
https://instagram.com/uglyshuz.il?igshid=ggcfgx2itbby
https://instagram.com/sneakertube.il?igshid=10iddya9ncuaf
https://instagram.com/sup_shoes_il?igshid=sm3yfw9xx3fn
https://instagram.com/outlet_shoes_il?igshid=4p2cal7b4z87
https://instagram.com/queen.shoes.il?igshid=11iagyxxs8af3
https://instagram.com/shoesandmore.il?igshid=1qjd08og203av
https://instagram.com/aldoshoes_il?igshid=14t44fmy6qprv
https://instagram.com/shoes.original.il?igshid=1qw8kyiycm1ov
https://instagram.com/premium_shoes_il?igshid=20io3irm7gso
https://instagram.com/onshoes.il?igshid=l7t18q31t3l5
https://instagram.com/friday_shoes.il?igshid=xdt8dcwkxrkn
https://instagram.com/royal_shoes.il?igshid=mizescoz3te5
https://instagram.com/royaltybrands.il?igshid=1udly7n4h7p6m
https://instagram.com/shoes_il?igshid=1r9839n0vkdlu
https://instagram.com/style_shoes_israell?igshid=1cuboia1z64d
https://instagram.com/gal__shoes?igshid=1146qpjxffe4z
https://instagram.com/worldshoes.il?igshid=1ivi7pqqbqlzq
https://instagram.com/1234.shoes?igshid=1609t7457bdro
https://instagram.com/nx_shoes?igshid=yiv75z6o633q
https://instagram.com/royal_shoes_isr?igshid=1u5595146toow
https://instagram.com/nextshoes.il?igshid=9i4rv5kno7t
https://instagram.com/shoes_factorry?igshid=hzazks3i76sg
https://instagram.com/shoeshu.co.il?igshid=1dj0tce9gl4to
https://instagram.com/adamshoes.co.il?igshid=y43rxilindue
https://instagram.com/black_monkey_shoes?igshid=fywx7ojawx8e
https://instagram.com/brandshoes.il?igshid=1u9iezn2psfic
https://instagram.com/trend_shoes_?igshid=76a8m3zyqpgt
https://instagram.com/mastershoes.il?igshid=avf0az0ixj00
https://instagram.com/shoesaddict_il?igshid=1v1u7858x1354
https://instagram.com/shoesit.il?igshid=fdlhao5818ol
https://instagram.com/melody.il.shoes?igshid=185ryyhzdmlc8
https://instagram.com/shoester.il?igshid=1asxs0pn9oj19
https://instagram.com/shoesoriginal.co.il?igshid=eug3jh5tp50p
https://instagram.com/super_shoes.il?igshid=1vgejypnobkmb
https://instagram.com/shoes4israel?igshid=1mgluuy44r46z
https://instagram.com/israel_shoes_seller?igshid=jswh0an2pb6r
https://instagram.com/city____shoes?igshid=1rhwovrfjuuh1
https://instagram.com/me_shoes_il?igshid=nep1569top2h
https://instagram.com/shoes___israel?igshid=19pgp0usolqus
https://instagram.com/slogan_shoes?igshid=4dcv0xfzurb5
https://instagram.com/mallshoes12?igshid=rhzzonp8de3p
https://instagram.com/shoesterminal_?igshid=1x7de4gze9w4n
https://instagram.com/il.intro?igshid=1s2sknarrxwro
https://instagram.com/trand.il?igshid=1n7pdsehmdngg
"""

My_list = _string.split()
# print(My_list)
new_list = []
for item in My_list:
    x = item.replace("https://instagram.com/", "")
    x2 = x.split("?")
    new_list.append(x2[0])

# print(new_list)

for item in new_list:
    counter = new_list.count(item)
    if counter != 1:
        print(item)


