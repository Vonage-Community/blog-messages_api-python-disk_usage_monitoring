## Disk usage monitoring system

### To setup this project:
 - clone this repository: `git clone git@github.com:Psycadelik/Disk-usage-monitor.git`
 - cd Disk-usage-monitor
 - create a .env file: `cp .env.sample .env`
   NB: Modify the .env values approriately with your own vonage credentials.
 - create a python virtual environment: `python3 -m venv .venv`
 - install dependecies: `source .venv/bin/activate && pip3 install -r requirements.txt`
 - run the script: `python3 monitor.py`
 - You can have this as a cronjob that runs once a day:
   edit the crontab entry: `sudo crontab -e`
   add the following entry : `0 6 * * * cd <project_directory> && .venv/bin/python3 monitor.py`

   The disk usage monitor will run everyday at 6:00 AM
