import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from math import ceil
from datetime import date
import glob

stats = {
        'label' : [],
        'Average position' : [],
        'Click through rate' : [],
        'Clicks' : [],
        'Cost' : []
        }

n = 1
for file in glob.glob('*.txt'):
    stats['label'].append('day'+str(n))
    with open(file) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    for i in data:
        if 'average position' in i or 'Average position' in i or 'Average Position' in i:
            stats['Average position'].append(float(i.split()[2]))
        elif 'Click through rate' in i or 'Click Through Rate' in i or 'click through rate' in i:
            stats['Click through rate'].append(float(i.split()[3]))
        elif 'Clicks' in i or 'clicks' in i:
            stats['Clicks'].append(int(i.split()[1]))
        elif 'Cost' in i or 'cost' in i:
            stats['Cost'].append(float(i.split()[1]))
    n+=1

#print(stats)

pp = PdfPages('Report_' + str(date.today()) + '.pdf')

for i in stats.keys():
    y = stats[i]
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle(i, fontsize=20)
    if i != 'label':
        plt.pie(stats[i],labels=stats['label'],autopct='%1.2f',startangle=90)
    else:
        continue
    pp.savefig(fig)
    plt.close(fig)
pp.close()