# -*- coding: utf-8 -*-

import logging as log

def get_logger(name) -> log.Logger:
    l = log.getLogger(name)
    l.setLevel(log.DEBUG)
    ch = log.StreamHandler()
    ch.setLevel(log.DEBUG)
    formatter = log.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    l.addHandler(ch)
    return l
