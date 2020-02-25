# Overview

Raspberry Pi based temperature monitor with web server and uploading data to google drive.
- The data is collected using DS18B20 temperature sensor (connected to Raspberry Pi).
- You can see the latest data as a chart in real-time in a browser (from anywhere).
- The data is automatically uploaded to your Google Drive.


# Running the tests

- Raspberry Pi or other linux: `cd test && ./run.sh`
- windows: run `run.cmd` from `test` subfolder
- using docker: `docker build -f test/Dockerfile .`


# Configuration

## Logger

Configure [logger.py](./logger.py) to be run on startup. It will read temperature data and store it in a local database. Use `--db-path` argument to specify path to SQLite database file.


## Web service

Configure [web.py](./web.py) to be run on startup. It will serve `http://localhost:5000/temperature/chart.html` page to see temperature data in real-time. Use the same `--db-path` argument as for [logger](#logger).

## Backup

Configure [backup.py](./backup.py) to be run periodically to upload data to Google Drive. Use the same `--db-path` argument as for [logger](#logger).