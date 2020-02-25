#!/bin/bash
set -exo pipefail

pytest -s $@

node test_chart.js