import argparse
import helpers
import os
import sys

from configparser import ConfigParser
from datetime import datetime
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random
from imblearn.over_sampling import SMOTENC
from imblearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold
import numpy as np
import pandas as pd

def evaluate(data, classifier):
    start_time = datetime.now()
    classifier.build_classifier(data)
    end_time = datetime.now()
    build_time = end_time - start_time

    evaluation = Evaluation(data)
    start_time = datetime.now()

    # Prepare for cross-validation with SMOTENC
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    smote_nc = SMOTENC(categorical_features=[data.attributes.index(attr) for attr in categorical_features], random_state=42)

    fold_results = []

    for train_index, test_index in skf.split(data.X, data.Y):
        X_train, X_test = data.X[train_index], data.X[test_index]
        y_train, y_test = data.Y[train_index], data.Y[test_index]

        # Apply SMOTENC to the training data
        X_resampled, y_resampled = smote_nc.fit_resample(X_train, y_train)

        # Create a new dataset for this fold
        fold_data = data.copy()
        fold_data.X = np.concatenate((X_resampled, X_test), axis=0)
        fold_data.Y = np.concatenate((y_resampled, y_test), axis=0)

        # Evaluate the classifier on this fold
        classifier.build_classifier(fold_data)
        fold_evaluation = Evaluation(fold_data)
        fold_results.append(fold_evaluation.crossvalidate_model(classifier, fold_data, 1, Random(42)))

    end_time = datetime.now()
    evaluation_time = end_time - start_time

    with open(f'{experiment_name}.log', 'w') as f:
        f.write(f"Classifier: {classname}\n")
        f.write(f"Options: {options if options else 'default'}\n")
        f.write(f"Classifier build time (HH:mm:ss): {build_time}\n")
        f.write(f"Evaluation time (HH:mm:ss): {evaluation_time}\n")
        f.write(f"\n")
        f.write(f"{classifier}\n")
        f.write(f"\n")
        f.write(f"{evaluation.summary()}\n")
        f.write(f"{evaluation.class_details()}\n")
        f.write(f"{evaluation.confusion_matrix}\n")
        f.write("\n")
        f.write(evaluation_class_summary(evaluation, 0))
        f.write(evaluation_class_summary(evaluation, 1))


def evaluation_class_summary(evaluation, class_index):
    return (
        f"Class {class_index} details\n"
        f"Area under ROC: {evaluation.area_under_roc(class_index)}\n"
        f"False negatives: {evaluation.num_false_negatives(class_index)}\n"
        f"True negatives: {evaluation.num_true_negatives(class_index)}\n"
        f"False positives: {evaluation.num_false_positives(class_index)}\n"
        f"True positives: {evaluation.num_true_positives(class_index)}\n\n"
    )


# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('indir', help="""
    A directory containing a config.ini file. All classifier results will be
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

        # Identify categorical features if needed
        categorical_features = []  # Set the list of categorical feature names

        for section in config:
            experiment_name = section

            # skip experiment if it has previously run
            # if os.path.exists(f'{experiment_name}.log'):
            #     continue
            
            experiment = config[section]
            classname = experiment.get('classname', None)
            if classname is None:
                continue
            options = experiment.get('options', "")
            split_string = r' \\ ' if r' \\ ' in options else ' '
            classifier = Classifier(
                classname=classname,
                options=options.split(split_string))
            evaluate(data, classifier)

except Exception as e:
    with open('error.log', 'w') as f:
        f.write(str(e))
    sys.exit(1)
