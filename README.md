# wyg-music

Music Wherever You Go is a self-hosted music service. I pretend to do the server with python and then with golang.

# Project time-line

<dl>

<dt> <b>20 / 11 / 2022</b> </dt>

<dd> Create app
<dd> Design structure of folders and files
<dd> Create home and user page (just files, not design)

<dt> <b>22 / 11 / 2022</b> </dt>

<dd> Added music bar
<dd> Music bar still sound while changing between home and user page

<dt> <b>23 / 11 / 2022</b> </dt>

<dd> Divide app file in different files for modularity
<dd> Created search bar (just html, not working)
<dd> Redis database diagram (probably not final)

<dt> <b>28 / 11 / 2022</b> </dt>

<dd> Search bar working with key 'Enter' or with button (not visual finished)
<dd> Change pure AJAX functions in javascript to HTMX

<dt> <b>5 / 12 / 2022</b> </dt>

<dd> Updated <a href="install.sh">install.sh</a> script to automate installation of packages and tools

<dt> <b>8 / 12 / 2022</b> </dt>

<dd> Added 'Upload' endpoint and a select files to upload songs (not working)
<dd> Init of Redis database and begining of documentation to familiarized with the functions
<dd> Added <a href="server/app_conf.py">configuration file</a> for Redis (probably for more than just Redis in a future)

<dt> <b>11 / 12 / 2022</b> </dt>

<dd> Added 'login' endpoint (working but not final version)
<dd> Improvement of Redis Databases Structure
<dd> Added more params to the <a href="server/app_conf.py">configuration file</a>
<dd> Session token for users who are logged

</dl>

# Redis database diagram

![Redis diagram](redis-diagram.png)
