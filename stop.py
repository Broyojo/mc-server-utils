import minecraft
import utils
import tmux
import time


def stop(dir):
    for server in minecraft.servers(dir):
        utils.log(f"Stopping {server}...")
        tmux.send_keys(server, "stop")
        time.sleep(5)
        tmux.send_keys(server, "C-c")  # may or may not work


if __name__ == "__main__":
    stop(minecraft.MAIN)
    stop(minecraft.EXTRA)
