#!/usr/bin/env python
"""

"""
import handler


def test_solve_components(fi="json_files/pllcalc.json"):
    """
    """
    fi = open(fi, 'r')
    dat = fi.read()
    # request = package_data(d)
    res = handler.solveComponents({'body':dat}, 'my context')
    return res 

def test_sim_pll(fi="json_files/simpll.json"):
    """
    """
    fi = open(fi, 'r')
    dat = fi.read()
    # request = package_data(d)
    res = handler.callSimulatePll({'body':dat}, 'my context')
    return res 

def test_interp_pn(fi="json_files/interp.json"):
    """
    """
    fi = open(fi, 'r')
    dat = fi.read()
    # request = package_data(d)
    res = handler.callInterpolatePhaseNoise({'body':dat}, 'my context')
    return res 

def test_sim_pn(fi="json_files/simpn.json"):
    """
    """
    fi = open(fi, 'r')
    dat = fi.read()
    # request = package_data(d)
    res = handler.callSimulatePhaseNoise({'body':dat}, 'my context')
    return res 
