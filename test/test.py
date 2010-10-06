#!/usr/bin/env python

import unittest
import sys
import parsing, destinations, lifecycle
import logging

def run_unittests():
    emodules = ['parsing', 'destinations', 'lifecycle', 'transactions', 'ack']
    modules = ['destinations']
    
    suite = unittest.TestSuite()
    for m in modules:
        mod = __import__(m)
        for name in dir(mod):
            obj = getattr(mod, name)
            if name.startswith("Test") and issubclass(obj, unittest.TestCase):
                suite.addTest(unittest.TestLoader().loadTestsFromTestCase(obj))

    ts = unittest.TextTestRunner().run(unittest.TestSuite(suite))
    if ts.errors or ts.failures:
        sys.exit(1)

if __name__ == '__main__':
    run_unittests()


