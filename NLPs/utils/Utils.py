# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def print_shape(v):
    print(v.get_shape().as_list())


def epoch_to_step(epoch, total_size, batch_size):
    return int(total_size / batch_size * epoch)


def step_to_epoch(step, total_size, batch_size):
    return int(step * batch_size / total_size)
