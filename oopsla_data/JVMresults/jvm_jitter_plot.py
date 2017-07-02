def read_file(fn):
    with open(fn) as f:
        return [float(x) / 1000000 for x in f.readlines()]

import sys
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(15, 4))

c4  = read_file(sys.argv[1])
cms = read_file(sys.argv[2])
g1  = read_file(sys.argv[3])
par = read_file(sys.argv[4])

# N = 64000
x = np.arange(0, len(c4))
# slices = len(orca) / N
# print slices

# for s in range(0, slices):
ax1.plot(x, c4, '.', color='black')

# for s in range(0, slices):
ax2.plot(x, cms, '.', color='black')

# for s in range(0, slices):
ax3.plot(x, g1, '.', color='black')

# for s in range(0, slices):
ax4.plot(x, par, '.', color='black')

# plt.yscale('log')
# plt.margins(0.07)


# plt.savefig(prefix + '.png', format='png', pad_inches=0, bbox_inches='tight')

all_max=(max(c4), max(cms), max(g1), max(par))
ax1.set_title('C4', fontsize=16)
# ax1.set_xticks(x)
ax1.xaxis.set_visible(False)
ax1.set_ylim(0, max(all_max))
ax1.tick_params(labelsize=15)


ax2.set_title('CMS')
ax2.set_ylim(0, max(all_max))
# ax2.set_xticks(x)
ax2.xaxis.set_visible(False)
# ax2.grid(True)
ax2.set_yticklabels([])

ax3.set_title('G1GC')
ax3.set_ylim(0, max(all_max))
# ax3.set_xticks(x)
ax3.xaxis.set_visible(False)
# ax3.grid(True)
ax3.set_yticklabels([])

ax4.set_title('Parallel')
ax4.set_ylim(0, max(all_max))
# ax3.set_xticks(x)
ax4.xaxis.set_visible(False)
# ax3.grid(True)
ax4.set_yticklabels([])

plt.tight_layout()
plt.savefig('jvm_jitter.png', format='png', pad_inches=0, bbox_inches='tight')