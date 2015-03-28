

def main1():
    with open('./keylog.txt') as f:
        l = f.readlines()
        li = map(int, l)
        print li
        ans = []
        for i in l:
            a,b,c = i.rstrip()
            print a,b,c
            ai, bi, ci = -1,-1,-1
            if a not in ans: ans.append(a)
            else: ai = ans.index(a)
            
            if b not in ans: ans.append(b)
            else: bi = ans.index(b)

            if c not in ans: ans.append(c)
            else: ci = ans.index(c)

            if ai <= bi and bi <= ci: continue
            
            if ai > bi and bi > ci :
                print a,b,c
                print ans
                ans.append(b)
                ans.append(c)
                pass
        print ans

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 

def main():
    with open('./keylog.txt') as f:
        l = f.readlines()
        ans = ''
        for i in l:
            # add new elements, nothing more to do here
            a,b,c = i.rstrip()
            #print a,b,c
            bbi = []
            ai, bi, ci = -1,-1,-1
            if a not in ans: ans += a
            else: 
                #ai = ans.rfind(a)
                ai = min(find_all(ans, a))
            
            if b not in ans: ans += b
            else: 
                #bi = ans.rfind(b)
                bbi = list( find_all(ans,b) )
                #print bi

            if c not in ans: ans += c
            else: 
                #
                ci = max(find_all(ans,c))

            #print ai,bi,ci
            if len(bbi) == 1: bi = bbi[0]
            
            #if ai > bi and bi > ci :
                #ans += b
                #ans += c
 
            if ai <= min(bbi) and bi <= ci: continue
            else: 
                print a,b,c, bi

        print ans


main()
