#!/bin/bash
set -eo pipefail

pytest -s $@

node test_chart.js