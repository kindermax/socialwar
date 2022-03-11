# SocialWar

Send messages to ok.ru users.

**`Caution:` this project created only to show example how to use tools to work with social sites. Do not use it under any circumstances.**


## activate virtual env

$ python3.8 -m venv env <br>
$ ./env/bin/python -m pip install -r ./requirements.txt <br>
$ chmod +x env/bin/activate <br> 
$ source env/bin/activate <br>
$ pytest -s --headless

## run tests in parallel
pytest -s -n $num_of_threads --headless 

## how to run

`pytest -s test_generate_cookies` - will login and generate cookies for all accounts. This will save some time since we do not need to login every time we want to send message.

But you can use `self.login_by_password` if you want to login for each message.

Next, run `test_send_message` test. It will read cookies (or accounts) and will try to send messages to users located in `files/ok_files/users.txt` (each line is user id). Then

At each iteration `move_user_cursor` will be called and store user id in either `files/ok_files/users_done.txt` or `files/ok_files/users_failed.txt`.

Test will send `get_users()[:3]` for each cookie and then stop.
This means not more than 3 messages from one session otherwise account can be blocked.
