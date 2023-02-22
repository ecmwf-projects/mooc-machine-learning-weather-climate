#!/usr/bin/env python3
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
from __future__ import annotations

import os

import climetlab as cml
from climetlab import Dataset
from climetlab.decorators import normalize

__version__ = "0.1.0"


class Main(Dataset):
    name = None
    home_page = "-"
    # The licence is the licence of the data (not the licence of the plugin)
    licence = "-"
    documentation = "-"
    citation = "-"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://github.com/john_doe/"
        "climetlab-my-plugin/"
        "blob/main/LICENSE. "
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    @normalize("parameter", ["soil_temperature", "forecast_error"])
    def __init__(self, parameter):
        self.source = cml.load_source("file", parameter + ".csv")
