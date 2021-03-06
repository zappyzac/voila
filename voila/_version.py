#############################################################################
# Copyright (c) 2018, Voila Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

version_info = (0, 2, 0, 'alpha', 1)

_specifier_ = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc', 'final': ''}

__version__ = '%s.%s.%s%s' % (version_info[0], version_info[1], version_info[2],
                              '' if version_info[3] == 'final' else _specifier_[version_info[3]] + str(version_info[4]))
