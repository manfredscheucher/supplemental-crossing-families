# On 4-Crossing-Families in Point Sets and an Asymptotic Upper Bound

This repository provides programs to verify the computer-assisted results from our paper "On 4-Crossing-Families in Point Sets and an Asymptotic Upper Bound" which is joint work with Oswin Aichholzer, Jan Kyncl, and Birgit Vogtenhuber.

## Abstract of the paper

A $k$-crossing family in a point set $S$ in general position is a set of $k$ segments spanned by points of $S$ such that all $k$ segments mutually cross. In this short note we present two statements on crossing families which are based on sets of small cardinality:
(1) Any set of at least 15 points contains a crossing family of size 4.
(2) There are sets of $n$ points which do not contain a crossing family of size larger than $4\lceil \frac{n}{20} \rceil < \frac{n}{5}+4$. 
Both results improve the previously best known bounds.

## Short description of the programs

We provide a python program "crf4.py" to formulate a SAT instance to verify that every set of 15 points contains a 4-crossing family. To execute the program, run

```python crf4.py 15```

The SAT instance is written to a cnf-file, which then can be solved using a SAT solver such as [cadical](http://fmv.jku.at/cadical/).  
We also provide the programs "crf3.py" and "crf5.py" which can be used to test the existance without 3-crossing families and 5-crossing families, respectively. In particular, "crf3.py" can be used to verify that every set of 10 points contains a 3-crossing family (a result by Aichholzer and Krasser from 2001).
