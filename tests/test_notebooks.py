#!/usr/bin/env python3
# (C) Copyright 2022 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os
import re
import glob

try:
    import nbformat
    import pytest
    from nbconvert.preprocessors import ExecutePreprocessor
except ImportError:
    raise Exception(
        "Test tools packages need to be installed to run the tests: pip install nbformat nbconvert ipykernel"
    )

# See https://www.blog.pythonlibrary.org/2018/10/16/testing-jupyter-notebooks/


def notebooks_list():
    notebooks = []
    for path in glob.glob('*.ipynb'):
        # ignore notebooks starting with '_'
        if re.match(r"[^_].*\.ipynb$", path):
            if "Copy" not in path:  # ignore notebook including 'Copy'
                notebooks.append(path)

    return sorted(notebooks)

class MyExecutePreprocessor(ExecutePreprocessor):
    def preprocess_cell(self, cell, resources, index):
        print(cell)
        if cell['source'] == 'gan.fit(dataset, epochs=30)':
            cell['source'] = 'gan.fit(dataset, epochs=1)'
        return super().preprocess_cell(cell, resources, index)

@pytest.mark.parametrize("path", notebooks_list())
def test_notebook(path):
    print(path)
    dir_path = os.path.dirname(path)

    with open(path) as f:
        nb = nbformat.read(f, as_version=4)

    proc = MyExecutePreprocessor(timeout=60 * 60, kernel_name="python3")
    proc.preprocess(nb, {"metadata": {"path": dir_path}})


if __name__ == "__main__":
    for k, f in sorted(globals().items()):
        if k.startswith("test_") and callable(f):
            print(k)
            f()
