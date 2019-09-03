#original source is from stackoverflow discussions

from IPython.display import clear_output
from matplotlib import pyplot as plt
import collections
%matplotlib inline

#define how the plot is presented
def live_plot(data_dict, figsize=(7,5), title=''):
    clear_output(wait=True)
    plt.figure(figsize=figsize)
    for label,data in data_dict.items():
        plt.plot(data, label=label)
    plt.title(title)
    plt.grid(True)
    plt.xlabel('epoch')
    plt.legend(loc='center left') # the plot evolves to the right
    plt.show();

#define the data
data = collections.defaultdict(list)
scope_limit=20  #how much data is remained in the view

for i in range(100):
    data['foo'].append(np.random.random())
    data['bar'].append(np.random.random())
    data['baz'].append(np.random.random())
    if len(data['foo'])>scope_limit: data['foo'].pop(0)
    if len(data['bar'])>scope_limit: data['bar'].pop(0)
    if len(data['baz'])>scope_limit: data['baz'].pop(0)
    live_plot(data)
