# -*- coding: utf-8 -*-

#Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Reading data of new born babies weights in Kilograms
new_borns_wt = np.genfromtxt('data2.csv', delimiter=' ').astype(float)

#Creating Distribution of my data
hist, edges = np.histogram(new_borns_wt, bins=13)

#Finding Distribution centres and Probability of the Distribution
centres = 0.5*(edges[1:]+edges[:-1])
widths = edges[1:]-edges[:-1]
prob = hist/np.sum(hist)

print('Weight Distribution centres', '\n', centres, '\n')
print('Weight Distribution probability', '\n', prob, '\n')

#Finding Average Weight of New Born babies
W = np.sum(centres*prob)
print('Average Weight of distribution - W is', f'{W.round(2)}Kg', '\n')

#Finding fraction of babies born weighting between W and 1.2W
X_weights = prob*((centres > W) & (centres < 1.2*W))
X = (np.sum(X_weights)).round(2)
print('Fraction of babies born weighting between W and 1.2W - X is', f'{X}')

#Plotting the outputs in a single plot
fig = plt.figure()

plt.bar(centres, prob, width=0.9*widths, color='c',
        label='Probability Distribution')

plt.plot([W, W], [0., np.max(prob)+0.005], 'b--', label='Average Weight W')
plt.text(W, np.max(prob)+0.005, f'Average Weight W is {W.round(2)}')

plt.bar(centres, X_weights, width=0.9*widths,
        color='m', label='Weights between W and 1.2*W \n' +
        'that is in X fraction')
plt.text(1.2*W+0.01, 0.08, 'Fraction of Weights' + '\n'
         + 'between W and \n1.2*W '+f'- X is {X}')

plt.xlabel('Weight of Newborns in Kg')
plt.ylabel('Probability')
plt.title('Newborn Weight Probability Distribution')
plt.legend(title='Legend', bbox_to_anchor=(1, 0.75))
plt.savefig('22028322.png', bbox_inches='tight', dpi=300)
plt.show()
