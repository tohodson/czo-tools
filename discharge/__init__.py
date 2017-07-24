# -*- coding: utf-8 -*-
"""This is a module to process HOBO pressure logs 
This module does stuff.
"""

__version__ = '0.0.1'
__author__ = 'Tim Hodson'

import sys, os, glob
import pandas as pd

import rating


LOG_COLS = ['datetime','pressure', 'temp']
DF_COLS  = ['pressure','temp']
H3O_COLS = ['stage']

def process_atm( in_dir, out_dir, atm_log ):
    """This is a function

	Args:
		in_dir (str): Directory containing new HOBO csv logs.
		out_dir (str): Directory were the processed csv logs are archived.
        atm_log (str): pickle containing atmospheric pressure

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

def process_h2o_log( h2o_log, atm_log ):
    """
    """
    h2o_df = read_hobo(h2o_log)
    atm_df = pd.read_pickle(atm_log)
    station = get_station_name(h2o_log)

    if not is_station(station):
       return

    else:
       offset  = get_station_offset(station)

       h2o_df['depth'] = calc_depth(h2o_df, atm_df)
       h2o_df['stage'] = calc_stage(h2o_df, offset)

       return h2o_df

def process_h2o( in_dir, out_dir, atm_log):
    """
    """
    h2o_logs = glob.glob(in_dir + os.sep + "*h2o.csv")

    for h2o_log in h2o_logs:
        station = get_station_name(h2o_log)
        out_log = out_dir + os.sep + station + '.csv'

        h2o_df = process_h2o_log(h2o_log, atm_log)

        if not h2o_df:
            continue

        elif h2o_df['temp'].notnull().sum > h2o_df['stage'].notnull().sum +
        30
        # if more than 2 hrs missing; also add -f parameter to force
        processing
            continue

        elif os.path.exists(out_log):
            h2o_df.to_csv( out_log, mode='a', header=False, columns=H2O_COLS)

        else:
            h2o_df.to_csv( out_log, columns=H2O_COLS)

        basename = os.path.basename(h2o_log)
        os.rename(h2o_log, out_dir + os.sep + basename)


def read_hobo(hobo_csv):
    """Read a HOBO csv and return a pandas dataframe.

	This function is a wrapper around pd.read_csv


	Args:
        hobo_csv (str): The first parameter.

    Returns:
        dataframe: The return value. True for success, False otherwise.
    """

    df = pd.read_csv(hobo_csv, skiprows=[0,1], usecols=[1,2,3], index_col=[0],
                                            parse_dates=[0], names=LOG_COLS)
    return df


def calc_depth(h2o_df, atm_df):
    """

    """

    df = pd.merge_asof(h2o_df.sort_values(by='datetime'),
                       atm_df.sort_values(by='datetime'),
                       allow_exact_matches=True,
                       on='datetime',
                       suffixes=('_h2o', '_atm'),
                       tolerance=pd.Timedelta('7 minutes') )

    df['rel_pressure_h2o'] = df['pressure_h2o'] - df['pressure_atm']

    #df['rho'] = calc_rho(df)
    rho = 1
    depth = df['rel_pressure_h2o']/ (rho * 9.81)

    return depth

def calc_stage(h2o_df, offset):
    """
    offset = datum - offset
    """
    stage = 100 - offset + h2o_df['depth']
    return stage

def get_station_name(input_log):
    """
    TODO: replace dumb return with regex that extracts numeral date string and
    .csv
    """
    name = os.path.basename()
    return name[0:-13]

def get_offset(station):
    pass
