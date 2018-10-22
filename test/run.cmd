SET PYTHONPATH=%~dp0/..;%PYTHONPATH%
pytest -s %*

node test_chart.js