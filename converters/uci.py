#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 16/7/30 下午8:49

@author: caoweiquan
"""
from converters import DataConverterBase
from converters import helper


class UciConverter(DataConverterBase):
    """
    This converter converts [UCI dataset](http://archive.ics.uci.edu/ml/datasets.html) into ARFF format.
    """
    def __init__(self):
        super(UciConverter, self).__init__()
        self.uci_to_arff = {
            'continuous': 'numeric',
        }

    def convert(self, input_file_path, output_file_path=None):
        helper.check_not_null_empty('input_file_path', input_file_path)
        train_file = input_file_path + '.data'
        helper.check_file_exists('train_file', train_file)
        test_file = input_file_path + '.test'
        helper.check_file_exists('test_file', test_file)
        names_file = input_file_path + '.names'
        helper.check_file_exists('names_file', names_file)
        if output_file_path is None or output_file_path == '':
            output_file_path = input_file_path

        # The attribute definition.
        attr_names, attr_values = self._parse_attributes(names_file)
        helper.log_debug('Attribute names:')
        helper.log_debug(str(attr_names))
        helper.log_debug('Attribute values:')
        helper.log_debug(str(attr_values))
        self._convert_data(train_file, output_file_path + '_train.ARFF', attr_names, attr_values)
        self._convert_data(test_file, output_file_path + '_test.ARFF', attr_names, attr_values)

    def _parse_attributes(self, names_file):
        # No parameter validation since this is a private method.
        attr_names = []
        attr_values = []
        with open(names_file, 'r') as fin:
            parsed_target = False
            for line in fin:
                line = line.strip()
                if line.startswith('|') or line == '':  # Comments.
                    continue

                if parsed_target:  # Known attributes.
                    parts = line.split(':')
                    attr_name = parts[0].strip()
                    attr_value = self._convert_attribute_format(parts[1].strip())
                    attr_names.append(attr_name)
                    attr_values.append(attr_value)
                else:  # Target attributes.
                    target_attr_value = self._convert_attribute_format(line)
                    parsed_target = True
            attr_names.append('target_attr')
            attr_values.append(target_attr_value)
        return attr_names, attr_values

    def _convert_attribute_format(self, uci_attr):
        if uci_attr.endswith('.'):
            uci_attr = uci_attr[0:-1]
        lower_uci_attr = uci_attr.lower()
        if lower_uci_attr in self.uci_to_arff:
            return self.uci_to_arff[lower_uci_attr]
        return '{%s}' % uci_attr

    def _convert_data(self, input_path, output_path, attr_names, attr_values):
        helper.check_int_equal('#attr_names/#attr_values', len(attr_names), len(attr_values))
        with open(output_path, 'w') as fout:
            # The header.
            fout.write('@RELATION unnamed\n\n')
            for i in range(0, len(attr_names)):
                fout.write('@ATTRIBUTE %s %s\n' % (attr_names[i], attr_values[i]))

            # The data.
            fout.write('\n@DATA\n\n')
            with open(input_path, 'r') as fin:
                for line in fin:
                    line = line.strip()
                    if line.endswith('.'):
                        line = line[0:-1]
                    if line.startswith('|') or line == '':
                        continue
                    fout.write(line)
                    fout.write('\n')

