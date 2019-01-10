import os
import logging


def safe_open_dir(dirpath):
    if not os.path.isdir(dirpath):
        logging.info("Directory %s does not exist, creating it" % dirpath)
        os.makedirs(dirpath)
    return dirpath


def safe_create_file(filepath):
    dirpath = os.path.dirname(filepath)
    dirpath = safe_open_dir(dirpath)
    return filepath


def get_model_path(run_id):
    return os.path.join(safe_open_dir("../models/"), str(run_id) + ".h5")


def get_plot_path(run_id):
    return os.path.join(safe_open_dir("../plots/"), str(run_id) + ".png")


def get_submission_path(run_id):
    return os.path.join(safe_open_dir("../submissions/"), str(run_id) + ".csv")


def get_cv_path(run_id):
    return os.path.join(safe_open_dir("../cv/"), str(run_id) + ".csv")


def get_prediction_path(run_id):
    return os.path.join(safe_open_dir("../predictions/"), str(run_id) + ".csv")


def rchop(s, *ends):
    for end in ends:
        endlen = len(end)
        if s[-endlen:] == end:
            return s[:-endlen]
    return s
