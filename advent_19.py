import re 
import numpy as np
def clean(x):
    y = []
    for xx in x:
        if '\"' in xx:
            y.append((re.sub('\"','', xx), 1))
        else:
            y.append((int(xx),0))
    return y

def check_rules(string, rule, rules):
    if type(rule) == str:
        if len(string) == 0:
            return None
        if string[0] == rule:
            return string[1:]
        else:
            return None
    elif type(rule) == list:
        if len(rule) == 1:
            return check_rules(string, rule[0], rules)
        else:
            ret = check_rules(string, rule[0], rules)
            if ret is not None:
                return check_rules(ret, rule[1:], rules)
            else:
                return None
    elif type(rule) == tuple:
        if rule[1] == 1:
            return check_rules(string, rule[0], rules)
        else:
            if len(rules[rule[0]]) == 1:
                return check_rules(string, rules[rule[0]], rules)
            else:
                for kor in rules[rule[0]]:
                    ret = check_rules(string, kor, rules)
                    if ret is not None:
                        return ret 
                return None


dat = open('data_19.txt').read().split('\n')

tocheck = []
ruledic = {}
for ll in dat:
    if ':' in ll:
        lsip = ll.split(':')
        k = int(lsip[0])
        if '|' in lsip[1]:
            lsips = lsip[1].split('|')
            rule1 = lsips[0].strip().split(' ')
            rule2 = lsips[1].strip().split(' ')
            rules = [clean(rule1), clean(rule2)]
        else:
            rules = [clean(lsip[1].strip().split(' '))]
        ruledic[k] = rules
    elif len(ll)<1:
        continue
    else:
        tocheck.append(ll)
        

print("Part 1")
cntr = 0
for check in tocheck:
    ret = check_rules(check, ruledic[0], ruledic)
    if ret is not None and len(ret) == 0:
        cntr+=1
print(cntr)


print("Part 2")
cntr = 0
for check in tocheck:
    for ip2 in range(1,13):
        broken = False
        for ip in range(1,13):
            my_rule = []
            for i in range(ip2+ip):
                my_rule.append((42,0))
            
            for i in range(ip2):
                my_rule.append((31,0))

            ret = check_rules(check, [my_rule], ruledic)
            if ret is not None and len(ret) == 0:
                cntr+=1
                broken = True
                break
        if broken:
            break
print(cntr)

