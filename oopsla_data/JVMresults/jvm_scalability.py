#!/usr/bin/env python
import sys
import math
import pylab
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh') # ggplot
# # Create a figure of size 8x6 inches, 80 dots per inch
# plt.figure(figsize=(4, 3), dpi=80)

def f(x):
	return x
	#if x == 0.0:
	#	return x
	#else:
	#	return math.log(x, 10)

def cyclesToUS(x):
  return secToUS(x/2299946000)

def secToMS(x):
  return x*1000

def secToUS(x):
  return x*1000000

def usToMS(x):
  return x/1000

colors =['#1f77b4', '#e377c2', '#ff7f0e', '#d62728', '#2ca02c',
         '#9467bd',
         '#8c564b', '#7f7f7f',
         '#bcbd22', '#17becf']
patterns = ['o', '\\', 'x', '.', '-', 'O', '*', '+']


N = 5
name=sys.argv[1]

cores=(4,8,16,34,64)

c4Rest = [ f(secToUS(x)) for x in input() ]
c4Concurrent = [ f(secToUS(x)) for x in input() ]
c4STW = [ f(secToUS(x)) for x in input() ]

cmsRest = [ f(secToUS(x)) for x in input() ]
cmsConcurrent = [ f(secToUS(x)) for x in input() ]
cmsSTW = [ f(secToUS(x)) for x in input() ]

g1gcRest = [ f(secToUS(x)) for x in input() ]
g1gcConcurrent = [ f(secToUS(x)) for x in input() ]
g1gcSTW = [ f(secToUS(x)) for x in input() ]

parallelRest = [ f(secToUS(x)) for x in input() ]
parallelSTW = [ f(secToUS(x)) for x in input() ]

ind = np.arange(0, 0.5, 0.1)
width = 0.09

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)
cms1 = ax1.bar(
  ind,
  cmsRest,
  width,
  color=colors[0],
  edgecolor='black',
  hatch=patterns[0]
)
cms2 = ax1.bar(
  ind,
  cmsConcurrent,
  width,
  color=colors[2],
  edgecolor='black',
  hatch=patterns[2],
  bottom=cmsRest
)
cms3 = ax1.bar(
  ind,
  cmsSTW,
  width,
  color=colors[3],
  edgecolor='black',
  hatch=patterns[3],
  bottom=[x + y for x, y in zip(cmsConcurrent, cmsRest)]
)

g1gc1 = ax2.bar(
  ind,
  g1gcRest,
  width,
  color=colors[0],
  edgecolor='black',
  hatch=patterns[0])
g1gc2 = ax2.bar(
  ind,
  g1gcConcurrent,
  width,
  color=colors[2],
  edgecolor='black',
  hatch=patterns[2],
  bottom=g1gcRest)
g1gc3 = ax2.bar(
  ind,
  g1gcSTW,
  width,
  color=colors[3],
  edgecolor='black',
  hatch=patterns[3],
  bottom=[x + y for x, y in zip(g1gcConcurrent, g1gcRest)])


parallel1 = ax3.bar(
  ind,
  parallelRest,
  width,
  color=colors[0],
  edgecolor='black',
  hatch=patterns[0])
parallel3 = ax3.bar(
  ind,
  parallelSTW,
  width,
  color=colors[3],
  edgecolor='black',
  hatch=patterns[3],
  bottom=parallelRest)


c41 = ax4.bar(
  ind,
  c4Rest,
  width,
  color=colors[0],
  edgecolor='black',
  hatch=patterns[0]
)
c42 = ax4.bar(
  ind,
  c4Concurrent,
  width,
  color=colors[2],
  edgecolor='black',
  hatch=patterns[2],
  bottom=c4Rest
)
c43 = ax4.bar(
  ind,
  c4STW,
  width,
  color=colors[3],
  edgecolor='black',
  hatch=patterns[3],
  bottom=[x + y for x, y in zip(c4Concurrent, c4Rest)]
)

totalC4=[x+y+z for (x,y,z) in zip(c4Rest, c4Concurrent, c4STW)]
totalCMS=[x+y+z for (x,y,z) in zip(cmsRest, cmsConcurrent, cmsSTW)]
totalG1GC=[x+y+z for (x,y,z) in zip(g1gcRest, g1gcConcurrent, g1gcSTW)]
totalParallel=[x+y for (x,y) in zip(parallelRest, parallelSTW)]
all_max=(max(totalC4), max(totalCMS), max(totalG1GC), max(totalParallel))

ax1.set_title('CMS', fontsize=16)
ax1.set_xticks(ind + width/2)
ax1.set_xticklabels(cores, fontsize=16)
ax1.set_ylabel('Time (microsec)', fontsize=16)
ax1.set_ylim(0, max(all_max)+0.05*max(all_max))

ax2.set_title('G1GC')
ax2.set_xticks(ind + width/2)
ax2.set_xticklabels(cores, fontsize=16)
ax2.set_ylim(0, max(all_max)+0.05*max(all_max))
ax2.grid(True)
ax2.set_yticklabels([])

ax3.set_title('Parallel')
ax3.set_xticks(ind + width/2)
ax3.set_xticklabels(cores, fontsize=16)
ax3.set_ylim(0, max(all_max)+0.05*max(all_max))
# ax3.yaxis.set_visible(False)
ax3.grid(True)
ax3.set_yticklabels([])

ax4.set_title('C4')
ax4.set_xticks(ind + width/2)
ax4.set_xticklabels(cores, fontsize=16)
ax4.set_ylim(0, max(all_max)+0.05*max(all_max))
# ax3.yaxis.set_visible(False)
ax4.grid(True)
ax4.set_yticklabels([])


plt.tight_layout()
plt.savefig(name+'_scalability.pdf', format='pdf', bbox_inches='tight')


# figlegend = pylab.figure(figsize=(9, 0.5))
# figlegend.legend((cmsRest[0], cmsConcurrent[0], cmsSTW[0]),
#     ('mutator time', 'concurrent gc', 'stw gc'),
#     ncol=3)
# figlegend.savefig('legend.pdf', format='pdf', bbox_inches='tight')
