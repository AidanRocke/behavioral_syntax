# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 07:28:51 2015

@author: Dell
"""

def Simple_compression(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result