# str = raw_input()
# n = input()
# opts = []
# for i in range(n):
#     opt = map(int, raw_input().split())
#     opts.append(opt)
#
# for i in opts:
#     cut_str = str[i[0]:i[0]+i[1]]
#     cut_str = cut_str[::-1]
#     str = str[0:i[0]+i[1]] + cut_str + str[i[0]+i[1]:]
# print str


# n, s, l = map(int, raw_input().split())
# capacity = (l + 1) / (s + 1)
# if capacity % 13 == 0:
#     capacity -= 1
#
# cd_need = n / float(capacity)
# if cd_need - int(cd_need) != 0:
#     cd_need = int(cd_need) + 1
#
# if cd_need == 1 and n % 13 == 0:
#     cd_need += 1
#
# #condidering the songs in the last cd
# if cd_need > 1:
#     last_cd = n - (cd_need-1)*capacity
#     if last_cd%13==0 and (capacity-1)%13==0:
#         cd_need += 1
#
# print int(cd_need)

x, k = map(int, raw_input().split())
res = []
y = 1
#while len(res)<k:
while y<10000:
    if x+y==x|y:
        res.append(y)
    y += 1

print len(res)