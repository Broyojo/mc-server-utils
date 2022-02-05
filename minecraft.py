import tmux
import os

MAIN = "/home/broyojo/main/"
EXTRA = "/home/broyojo/extra/"
MISC = "/home/broyojo/misc/"
BACKUPS = "/home/broyojo/backups/"


def servers(dir):
    return [server for server in os.listdir(dir)]


def say(server, msg):
    tmux.send_keys(
        server, f"tellraw @a {{\'text\':\'{msg}\',\'color\':\'red\',\'bold\':true}}")


def save_off(server):
    tmux.send_keys(server, "save-off")
    tmux.send_keys(server, "save-all")


def save_on(server):
    tmux.send_keys(server, "save-on")
