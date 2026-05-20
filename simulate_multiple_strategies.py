#!/usr/bin/env python3

"""
Simulate many turns of Shut the Box using the default decision methods.
Output the score for each turn to the command line.
"""

import shutthebox
import numpy as np
from matplotlib import pyplot as plt

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# pylint: disable=invalid-name

box = shutthebox.Box()
dice = shutthebox.Dice()

turn = shutthebox.ComputerTurn(box, dice)

#ngames = 100000
ngames = 1000

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using default decisions
result_default = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with defualt strategy")
for n in range(0, ngames):
    result_default[n] = turn.perform_turn()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using two dice option
result_default_2D = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with default two dice strategy")
for n in range(0, ngames):
    result_default_2D[n] = turn.perform_turn(num_dice_decision_method=turn.make_num_dice_decision_always_all)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using HIGHEST strategy
result_highest = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with HIGHEST strategy")
for n in range(0, ngames):
    result_highest[n] = turn.perform_turn(flap_decision_method=turn.make_flap_decision_highest)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using HIGHEST 2dice stategy
result_highest_2D = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with HIGHEST two dice strategy")
for n in range(0, ngames):
    result_highest_2D[n] = turn.perform_turn(flap_decision_method=turn.make_flap_decision_highest,num_dice_decision_method=turn.make_num_dice_decision_always_all)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using LOWESEST strategy
result_lowest = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with LOWEST strategy")
for n in range(0, ngames):
    result_lowest[n] = turn.perform_turn(flap_decision_method=turn.make_flap_decision_lowest)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using LOWEST 2dice stategy
result_lowest_2D = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with LOWEST two dice strategy")
for n in range(0, ngames):
    result_lowest_2D[n] = turn.perform_turn(flap_decision_method=turn.make_flap_decision_lowest,num_dice_decision_method=turn.make_num_dice_decision_always_all)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using LOWESEST strategy
result_bills = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with Bill Butler strategy")
for n in range(0, ngames):
    result_bills[n] = turn.perform_turn(flap_decision_method=turn.make_flap_decision_bill)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#go through n games and calc result using LOWESEST strategy
result_bills_2D = np.zeros(ngames).astype(int)
print("Doing " + str(ngames) + " games with Bill Butler two dice strategy")
for n in range(0, ngames):
    result_bills_2D[n] = turn.perform_turn(flap_decision_method=turn.make_flap_decision_bill_2D)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#use convention that perfect score is 45 not zero
result_default = 45-result_default
result_default_2D = 45-result_default_2D
result_highest = 45-result_highest
result_highest_2D = 45-result_highest_2D
result_lowest = 45-result_lowest
result_lowest_2D = 45-result_lowest_2D
result_bills = 45-result_bills
result_bills_2D = 45-result_bills_2D
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#count results and plot
plt.figure()
counts_default = np.bincount(result_default)
counts_default_2D = np.bincount(result_default_2D)
counts_highest = np.bincount(result_highest)
counts_highest_2D = np.bincount(result_highest_2D)
counts_lowest = np.bincount(result_lowest)
counts_lowest_2D = np.bincount(result_lowest_2D)
counts_bills = np.bincount(result_bills)
counts_bills_2D = np.bincount(result_bills_2D)
bins = np.arange(46)
plt.plot(bins,100.*counts_default/n, label='default'+' win perc. '+f'{100.*counts_default[45]/n:.2f}')
plt.plot(bins,100.*counts_default_2D/n, label='default 2D6'+' win perc. '+f'{100.*counts_default_2D[45]/n:.2f}')
plt.plot(bins,100.*counts_highest/n, label='highest'+' win perc. '+f'{100.*counts_highest[45]/n:.2f}')
plt.plot(bins,100.*counts_highest_2D/n, label='highest 2D6'+' win perc. '+f'{100.*counts_highest_2D[45]/n:.2f}')
plt.plot(bins,100.*counts_lowest/n, label='lowest'+' win perc. '+f'{100.*counts_lowest[45]/n:.2f}')
plt.plot(bins,100.*counts_lowest_2D/n, label='lowest 2D6'+' win perc. '+f'{100.*counts_lowest_2D[45]/n:.2f}')
plt.plot(bins,100.*counts_bills/n, label='Bill Butler'+' win perc. '+f'{100.*counts_bills[45]/n:.2f}')
plt.plot(bins,100.*counts_bills_2D/n, label='Bill Butler'+' win perc. '+f'{100.*counts_bills_2D[45]/n:.2f}')
plt.title('Shut the box strategies')
plt.xlabel('score (45 is a win)')
plt.ylabel('probablity (%)')
plt.legend()
plt.savefig('stb_9_multiple_strategies')
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("Strategy Summary")
print("Note that unless specified can always use 1 dice if up flap total <=6")
print("Default      strategy - bases flap choice on remaining flap probabilities")
print("Default 2D   strategy - as above but always use 2 dice")
print("highest      strategy - always closes highest single flap -then combo with highest ")
print("highest 2D   strategy - as above but always use 2 dice")
print("lowest       strategy - always closes lowest single flap -then combo with lowest ")
print("lowest 2D    strategy - as above but always use 2 dice")
print("Bill Butler  strategy - See Bill Butlers webpage")
print("Bill Butler2Dstrategy - as above but always use 2 dice")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("TO DO - IMPORT BILL BUTLERS OPTIMAL 2D STRATEGY AND SEE IF DIFFERENT")
print("TO DO - DOES SAVING THE 1 WHEN POSSIBLE HELP the HIGHEST strategy?")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



