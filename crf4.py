#!/usr/bin/python
"""
	This program can be used to generate a CNF
	to verify that every set of n points contains a 4-crossing family
	(c) 2021 Manfred Scheucher <scheucher@math.tu-berlin.de>
"""


from itertools import combinations, permutations
from sys import *

n = int(argv[1]) 
N = range(n)


all_variables = []
all_variables += [('trip',I) for I in permutations(N,3)]
all_variables += [('ab_sep_cd',I) for I in permutations(N,4)]
all_variables += [('ab_crs_cd',I) for I in permutations(N,4)]

all_variables_index = {}

_num_vars = 0
for v in all_variables:
	all_variables_index[v] = _num_vars
	_num_vars += 1

def var(L):	return 1+all_variables_index[L]
def var_trip(*L): return var(('trip',L))
def var_ab_sep_cd(*L): return var(('ab_sep_cd',L))
def var_ab_crs_cd(*L): return var(('ab_crs_cd',L))

constraints = []




print "(1) Alternating axioms",len(constraints)
for a,b,c in combinations(N,3):
	for sgn in [+1,-1]:
		constraints.append([sgn*var_trip(a,b,c),-sgn*var_trip(b,c,a)])
		constraints.append([sgn*var_trip(a,b,c),-sgn*var_trip(c,a,b)])
		constraints.append([sgn*var_trip(a,b,c),sgn*var_trip(c,b,a)])
		constraints.append([sgn*var_trip(a,b,c),sgn*var_trip(b,a,c)])
		constraints.append([sgn*var_trip(a,b,c),sgn*var_trip(a,c,b)])


print "(2) Valid signature",len(constraints)
# forbid invalid configuartions in the signature
for I4 in combinations(N,4):
	I4_triples = list(combinations(I4,3))
	for t1,t2,t3 in combinations(I4_triples,3): 
		# for any three lexicographical ordered triples t1 < t2 < t3
		# the signature must not be "+-+" or "-+-"
		for sgn in [+1,-1]:
			constraints.append([sgn*var_trip(*t1),-sgn*var_trip(*t2),sgn*var_trip(*t3)])



print "(3) Sorted around first points",len(constraints)
# without loss of generality, points sorted around 0
for b,c in combinations(range(1,n),2):
	constraints.append([var_trip(0,b,c)])



print "(4) edge separations",len(constraints)
for I in permutations(N,4):
	[a,b,c,d] = I
	constraints.append([-var_ab_sep_cd(*I),+var_trip(a,b,c),+var_trip(a,b,d)])
	constraints.append([-var_ab_sep_cd(*I),-var_trip(a,b,c),-var_trip(a,b,d)])

	constraints.append([var_ab_sep_cd(*I),+var_trip(a,b,c),-var_trip(a,b,d)])
	constraints.append([var_ab_sep_cd(*I),-var_trip(a,b,c),+var_trip(a,b,d)])


print "(5) edge crossings",len(constraints)
for I in permutations(N,4):
	[a,b,c,d] = I
	constraints.append([-var_ab_crs_cd(a,b,c,d),+var_ab_sep_cd(a,b,c,d)])
	constraints.append([-var_ab_crs_cd(a,b,c,d),+var_ab_sep_cd(c,d,a,b)])
	constraints.append([+var_ab_crs_cd(a,b,c,d),-var_ab_sep_cd(a,b,c,d),-var_ab_sep_cd(c,d,a,b)])


print "(6) no 4-crossing families",len(constraints)
for I in combinations(N,8):
	for a1,a2,a3,a4 in combinations(I,4):
		J = [i for i in I if i not in {a1,a2,a3,a4}]
		for b1,b2,b3,b4 in permutations(J):
			if a1<b1 and a2<b2 and a3<b3 and a4<b4:
				segments = [(a1,b1),(a2,b2),(a3,b3),(a4,b4)]
				constraints.append([-var_ab_crs_cd(ai,bi,aj,bj) for (ai,bi),(aj,bj) in combinations(segments,2)])




print "Total number of constraints:",len(constraints)


fp = "instance_crf4_"+str(n)+".in"
f = open(fp,"w")
f.write("p cnf "+str(_num_vars)+" "+str(len(constraints))+"\n")
for c in constraints:
	f.write(" ".join(str(v) for v in c)+" 0\n")
f.close()

print "Created CNF-file:",fp


