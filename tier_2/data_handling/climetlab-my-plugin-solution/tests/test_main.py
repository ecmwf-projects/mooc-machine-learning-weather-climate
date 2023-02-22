#!/usr/bin/env python3
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

import climetlab as cml


def test_read():
    ds = cml.load_dataset(
        "my-plugin",
        year="2021",
        parameter="t2m",
    )
    xds = ds.to_xarray()
    print(xds)


if __name__ == "__main__":
    test_read()
