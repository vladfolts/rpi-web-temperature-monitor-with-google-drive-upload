#!/bin/bash
set -eo pipefail

SCRIPTDIR=`dirname "$0"`
export PYTHONPATH=$SCRIPTDIR/..:$PYTHONPATH
pytest -s $@

node test_chart.js