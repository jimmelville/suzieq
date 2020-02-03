#!/usr/bin/env python3

# Copyright (c) Dinesh G Dutt
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#

import typing

from suzieq.sqobjects import basicobj


class topcpuObj(basicobj.SqObject):

    def __init__(self, engine: str = '', hostname: typing.List[str] = [],
                 start_time: str = '', end_time: str = '',
                 view: str = 'latest', datacenter: typing.List[str] = [],
                 columns: typing.List[str] = ['default'],
                 context=None) -> None:
        super().__init__(engine, hostname, start_time, end_time, view,
                         datacenter, columns, context=context, table='topcpu')
        self._sort_fields = ['datacenter', 'hostname']
        self._cat_fields = []


if __name__ == '__main__':
    try:
        import fire
        fire.Fire(topcpuObj)
    except ImportError:
        pass



    