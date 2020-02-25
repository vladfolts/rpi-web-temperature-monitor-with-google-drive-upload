# Overview

Raspberry Pi based temperature monitor with web server and uploading data to google drive.
- The data is collected using DS18B20 temperature sensor (connected to Raspberry Pi).
- You can see the latest data as a chart in a real time in a browser (from anywhere).
- The data is automatically uploaded to your Google Drive.


# Running the tests

- Raspberry Pi or other linux: `cd test && ./run.sh`
- windows: run `run.cmd` from `test` subfolder
- using docker: `docker build -f test/Dockerfile .`
