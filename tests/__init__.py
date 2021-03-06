#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
stati.tests
~~~~~~~~~~~

Unittests for stati

:copyright: (c) 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

import unittest

from mock import Mock
import socket


#socket.create_connection = Mock()

from .http import HTTPTestCase
from .client import ClientTestCase
from .udp import UDPTestCase
from .tcpip import TCPIPTestCase

def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(HTTPTestCase))
    suite.addTest(unittest.makeSuite(ClientTestCase))
    suite.addTest(unittest.makeSuite(TCPIPTestCase))
    suite.addTest(unittest.makeSuite(UDPTestCase))

    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="suite")
