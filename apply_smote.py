# Original code from: https://github.com/bellaanderssen/thesis23/blob/main/evaluate.py

import argparse
import helpers
import os
import sys

from configparser import ConfigParser
from datetime import datetime
from weka.filters import Filter

def apply_smote(data, options):
    start_time = datetime.now()
    
    # Apply SMOTE. 
	# Note: -P specifies the percentage of SMOTE instance to create
    smote = Filter(classname="weka.filters.supervised.instance.SMOTE",
                   options=options)
    
    smote.inputformat(data)
    balanced_data = smote.filter(data)
    
    end_time = datetime.now()
    smote_time = end_time - start_time

    with open(f'logs/{experiment_name}.log', 'w') as f:
        f.write(f"Experiment: {experiment_name}\n")
        f.write(f"SMOTE time (HH:mm:ss): {smote_time}\n")
        f.write(f"\n")
        f.write(f"SMOTE applied successfully on dataset.\n")

    return balanced_data

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('indir', help="""
    A directory containing a config.ini file. All SMOTE results will be
    output to this file.
    """)
parser.add_argument('--max-heap-size', default=None)
args = parser.parse_args()
config_file = helpers.assert_dir_contains_config(args.indir)

try:
    config = ConfigParser()
    config.optionxform = str  # preserve case in config keys
    config.read(config_file)
    os.chdir(args.indir)  # treat contents of file relative to config.ini
    data_filepath = config['meta']['data_path']
    helpers.assert_file_exists(data_filepath)

    with helpers.JVM(max_heap_size=args.max_heap_size):
        data = helpers.load_csv(data_filepath)
        data = helpers.fill_na(data)
      
        for section in config:
            experiment_name = section
            # skip experiment if it has previously run
            # if os.path.exists(f'logs/{experiment_name}.log'):
            #     continue
            experiment = config[section]

            classname = experiment.get('classname', None)
            if classname is None:
                continue

            options = experiment.get('options', "")
            split_string = r' \\ ' if r' \\ ' in options else ' '

            # Apply SMOTE instead of a classifier
            balanced_data = apply_smote(data, options=options.split(split_string))
            helpers.save_csv(balanced_data, '../GeneratedData/ED_SMOTE.csv')

except Exception as e:
    with open('error.log', 'w') as f:
        f.write(str(e))
    sys.exit(1)
