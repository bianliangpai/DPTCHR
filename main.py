#
#
#  Preparation
#
#

import os
import sys
import json


def prepare():
  # change working directory
  current_file_dir = os.path.dirname(os.path.realpath(__file__))
  expected_working_dir = current_file_dir
  os.chdir(expected_working_dir)

  # make source files in 'src' can be imported
  sys.path.append("{}/src".format(expected_working_dir))


if __name__ == '__main__':
  prepare()

#
#
#  Core logic
#
#

from keys import Keys
from database import Database


def main():
  with open("config/conf.json") as conf_file:
    config = json.load(conf_file)

  keys = Keys(config["keysfile"])
  database = Database(config["datafile"])

  database.set_filter(keys)
  result = '\n'.join([data for data in database])

  with open(config["resultfile"], 'w') as rf:
    rf.write(result)


if __name__ == '__main__':
  main()
