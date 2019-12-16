#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']
  def find_outcome(rds_lft, rst):
    if rds_lft == 0: 
      outcomes.append(rst)
      return
    for play in plays: 
      find_outcome(rds_lft - 1, rst + [play])
 
  find_outcome(n, [])
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

    #accumulator 