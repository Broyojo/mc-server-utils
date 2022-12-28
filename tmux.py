import os


def send_keys(session, command):
    os.system(f'tmux send-keys -t {session} "{command}" ENTER')


def new_session(name):
    os.system(f"tmux new-session -d -s {name}")
