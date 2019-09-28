# PITNEY BOWES HACKATHON POS SERVER

## INSTRUCTIONS TO DEPLOY

- Make sure you are using `python 3.6` or higher.
- Run the following commands from the project directory
  
  ```sh
  pip install -r requirements.txt
  python main.py
  ```

- The server uses an mongoDB cluster hosted on Atlas, we will be destroying the cluster after 30 days of ending of the challenge.

- Change the `mongoDB URI` if you want to use your own mongoDB instance.

- The server also contains an `app.yaml` file, which can be used to deploy server on Google App Engine.

- Live Demo: https://anuragintern.appspot.com/static/index.html
- Youtube Web Demo Link: https://www.youtube.com/playlist?list=PLYWP1d3eBUheAbjyR600oQOhIV2nYTcNP
