#!/usr/bin/python

import argparse

def find_max_profit(prices):
  mx_prf = -10
  for i in range(len(prices)): #O(n)
    cur_pri = prices[i]
    for j in range(i+1, len(prices)): #O(n)
      nxt_pri =  prices[j]
      profit = nxt_pri - cur_pri
      if profit > mx_prf:
        mx_prf = profit
      j = j + 1
  i = i + 1
  return mx_prf


print(find_max_profit([10, 7, 5, 8, 11, 9]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

