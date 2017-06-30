# -*- coding: utf-8 -*-
"""This is the example module.abs
This module does stuff.
"""

__version__ = '0.0.1'
__author__ = 'Tim Hodson'

import sys, os, glob
import pandas as pd


LOG_COLS = ['datetime','pressure', 'temp']
DF_COLS  = ['pressure','temp']

def process_atm( in_dir, out_dir, atm_log=False ):
    """This is a function

	Args:
		in_dir (str): Directory containing new HOBO csv logs.
		out_dir (str): Directory were the processed csv logs are archived.


    """
    if os.path.exists(atm_log):
        try:
            a = pd.read_pickle(atm_log)
        except IOError:
                print('Atmospheric pressure log file not valid')
                sys.exit(1)
	else:
		a = pd.DataFrame( columns=DF_COLS)

    atm_files = glob.glob(in_dir + os.sep + '*_atm_*.csv')


    for f in atm_files:
        # read file
        temp = read_hobo(f) 

		# append file to appriopriate pickle
        a.append(temp)

        # move file to out directory
        basename = os.path.basename(f)
        os.rename(f, out_dir + os.sep + basename)

    a.to_pickle(atm_log)

def process_h2o( in_dir, out_dir, atm_log):

    h2o_files = glob.glob(in_dir + os.sep + "*h2o.csv")
    pass


def read_hobo(hobo_csv):
    """Read a HOBO csv and return a pandas dataframe.

	This function is a wrapper around pd.read_csv


	Args:
        hobo_csv (str): The first parameter.

    Returns:
        dataframe: The return value. True for success, False otherwise. 
    """

    pd.read_csv(file, skiprows=[0,1], usecols=[1,2,3], index_col=[0],
                                            parse_dates=[0], names=LOG_COLS)


