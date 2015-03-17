from __future__ import division

def distribute_votes(l, tot):
    """ distributes 'tot' votes among members of l """
    votes = []
    for p in l: 
        votes.append( ((sum(l) + tot)/len(l) - p) / tot)
    return votes
    

def Is_Safe(v,l, tot):
    votes =  distribute_votes(l, tot)
    if votes:
        return v >= l[0] + votes[0]*tot, votes
    return False, []
    

def solve(v):
    ans = []
    tot = sum(v)
    vs = sorted(v)
    for e in vs[1:]:
        safety, distribution = Is_Safe(e, vs[:vs.index(e)], tot)
        if safety: break
    else:
        return [d*100 for d in distribute_votes(v,tot)]

    for e in v:
        try:
            ans.append(distribution[vs.index(e)]*100)
        except IndexError:
            ans.append(0)
    return ans
        
        

def main():
    with open("small.in") as f:
        number_lines = int(f.readline())
        for n in xrange(number_lines):
            vals = map(int, f.readline().split(" ")[1:])
            ans_string = []
            
            print "Case #" + str(n+1) + ":",
            for ans in solve(vals):
                print "%.10f" % ans, 
            print ""
main()
