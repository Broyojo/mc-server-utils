#!/usr/bin/env python

import minecraft
import utils
import tmux


def start(dir):
    for server in minecraft.servers(dir):
        utils.log(f"Starting {server}...")
        tmux.new_session(server)
        tmux.send_keys(server, f"cd {dir}{server}")
        tmux.send_keys(server, "./start.sh")


if __name__ == "__main__":
    start(minecraft.MAIN)
    start(minecraft.EXTRA)
