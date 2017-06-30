#!/usr/bin/env python3
import sys, os, glob
import pandas as pd

def process_atm( in_dir, out_dir, atm_log=False ):
    
    if os.path.exists(atm_log):
        try:
            a = pd.read_picke( atm_log )
        except IOError:

                print('Atmospheric pressure log file not valid')
                sys.exit(1)


    atm_files = glob.glob(in_dir + os.sep + '*_atm_*.csv')

  
    for f in atm_files:
        # read file
        atm_data = pd.read_csv(f, sep=',')
        # append file to appriopriate pickle
        a.append(atm_data)

        # move file to out directory
        basename = os.path.basename(f)
        os.rename(f, out_dir + os.sep + basename)
    
    a.to_pickle(atm_log)

def process_h2o( in_dir, out_dir, atm_log):

    h2o_files = glob.glob(in_dir + os.sep + "*h2o.csv")
    pass





# main
# look in inbox

# process each file in inbox
