# -*- coding: utf-8 -*-
"""This is a module to process stream discharge 
This module does stuff.
"""

__version__ = '0.0.1'
__author__ = 'Tim Hodson'

import sys, os, glob
import pandas as pd

from discharge.rating import get_rating


def process_csv(in_file, station):
    """
    Args:
    returns header,df
    """
    if station == '148':
        header, df = process_148(in_file)
        return header, df

def process_148(in_file):

    try:
        f = open(in_file)
        header = f.readline().strip('\n')
        columns = f.readline().strip('\n')
        units   = f.readline().strip('\n')
        measurements = f.readline().strip('\n')

        df = pd.read_csv(f, sep=',', names = columns.split(',') )
    except IOError:
        print('Not a valid input file for station 148')

    rate = get_rating('148')
    df['"Discharge"'] = rate( df['"DepthUP"'])
    header = header + '\n' + columns + ',"Discharge"\n' + units + ',"meters^3/second"\n' + measurements + ',"Smp"\n'
    f.close()
    return header, df


def write_discharge(out_file, df, header=''):

    if not os.path.exists(out_file):
        try:
            f = open(out_file, 'w')
            f.writelines(header)
            f.close()
        except IOError as e:
            print("error({0}):{1}".format(e.errno, e.strerror))

    df.to_csv( out_file, header=False, index=False, mode='a' )

def process_stage(in_file, out_file, station):

    header, df = process_csv(in_file, station)
    write_discharge(out_file, df, header)
