#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 16/7/30 下午9:27

@author: caoweiquan
"""
import os
import os.path

LOG_DEBUG = 0
LOG_INFO = 1
LOG_WARN = 2
LOG_ERROR = 3
LOG_CRASH = 4
log_level = LOG_DEBUG


def log_message(msg, level):
    if level >= log_level:
        print(msg)


def log_debug(msg):
    log_message('DEBUG: ' + msg, LOG_DEBUG)


def log_info(msg):
    log_message('INFO: ' + msg, LOG_INFO)


def log_warn(msg):
    log_message('WARN: ' + msg, LOG_WARN)


def log_error(msg):
    log_message('ERROR: ' + msg, LOG_ERROR)


def log_crash(msg):
    log_message('CRASH: ' + msg, LOG_CRASH)


def check_val_range(name, val, inf, sup):
    if val < inf or val > sup:
        raise ValueError('%s value %.3f is out of range [%.3f, %.3f].' % (name, val, inf, sup))


def check_non_negative(name, val):
    if val < 0.0:
        raise ValueError('%s value %.3f is negative.' % (name, val))


def check_int_equal(name, val, expected):
    if isinstance(val, long):
        val = int(val)
    check_type(name, val, int)
    if val != expected:
        raise ValueError('%s value is expected to be %d but got %d.' % (name, expected, val))


def check_type(name, val, val_type):
    if type(val) is not val_type:
        raise TypeError('Variant %s is expected to be a(n) %s, but got %s.' % (name, val_type, type(val)))


def check_not_null_empty(name, val):
    if val is None or val.strip() == '':
        raise ValueError('%s must not be null nor empty.' % name)


def check_file_exists(name, val):
    check_not_null_empty(name, val)
    if not os.path.exists(val):
        raise ValueError('The file %s does not exist.' % val)


def file_size(file_name):
    try:
        return os.stat(file_name).st_size
    except Exception, e:
        log_error('Error occurs in file_size(): %s' % str(e))
        return 0
