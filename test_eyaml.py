#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pprint
from unittest import TestCase

import eyaml

__author__ = 'Marco Bartel'


class TestEyaml(TestCase):
    def test_load(self):
        pp = pprint.PrettyPrinter(indent=4)
        config = eyaml.load(r"examples/config.yaml")
        print json.dumps(config, sort_keys=True, indent=4)
        # pp.pprint(eyaml.load(r"e:\svnwork\esgento\conf\AmazonReportRequester_test.yaml"))




