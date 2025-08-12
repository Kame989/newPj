import math

n = int(input())
c = int(input())

com = math.comb(n, c)


print(com)
'''In Python, the combination formula, which calculates the number of ways to choose k items from a set of n items without repetition and without regard to order, can be implemented using the math.comb() method. This method is available in the math module and was added in Python 3.8.                The mathematical formula for combinations is:                \(C(n,k)=\frac{n!}{k!(n-k)!}\)      .f5cPye .WaaZC:first-of-type .rPeykc.uP58nb:first-child{font-size:var(--m3t3);line-height:var(--m3t4);font-weight:400 !important;letter-spacing:normal;margin:0 0 10px 0}.rPeykc.uP58nb{font-size:var(--m3t5);font-weight:500;line-height:var(--m3t6);margin:20px 0 10px 0}.f5cPye ul{font-size:var(--m3t7);line-height:var(--m3t8);margin:10px 0 20px 0;padding-inline-start:24px}.f5cPye .WaaZC:first-of-type ul:first-child{margin-top:0}.f5cPye ul.qh1nvc{font-size:var(--m3t7);line-height:var(--m3t8)}.f5cPye li{padding-left:4px;margin-bottom:8px;list-style:inherit}.f5cPye li.K3KsMc{list-style-type:none}.f5cPye ul>li:last-child,.f5cPye ol>li:last-child,.f5cPye ul>.bsmXxe:last-child>li,.f5cPye ol>.bsmXxe:last-child>li{margin-bottom:0}          where:      \(n\) is the total number of items in the set. \(k\) is the number of items to be selected from the set. \(!\) denotes the factorial operation.'''