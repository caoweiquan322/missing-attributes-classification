#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 16/7/30 下午8:53

@author: caoweiquan
"""
from converters.uci import UciConverter
from converters import helper


if __name__ == '__main__':
    folder_path = '/Users/fatty/Papers/MissingClass/Adult'
    cvt = UciConverter()
    cvt.convert(folder_path + '/adult')
    helper.log_info('Job done!')
