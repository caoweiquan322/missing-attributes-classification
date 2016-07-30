#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 16/7/30 下午8:48

@author: caoweiquan
"""


class DataConverterBase(object):
    """
    This is the abstract class that converts any data formats into the standard weka-ARFF format.
    """
    def __init__(self):
        super(DataConverterBase, self).__init__()

    def convert(self, *args):
        pass
