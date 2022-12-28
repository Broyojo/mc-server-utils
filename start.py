import minecraft
import tmux
import utils


def start(dir):
    for server in minecraft.servers(dir):
        utils.log(f"Starting {server}...")
        tmux.new_session(server)
        tmux.send_keys(server, f"cd {dir}{server}")
        tmux.send_keys(server, "./start.sh")


if __name__ == "__main__":
    start(minecraft.MAIN)
    start(minecraft.EXTRA)

    tmux.new_session("webserver")
    tmux.send_keys("webserver", "cd /home/broyojo/webserver")

    tmux.new_session("backup")
    tmux.send_keys("backup", "cd /home/broyojo/utils")
    tmux.send_keys("backup", "python3 scheduler.py")
