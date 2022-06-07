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

    tmux.new_session("webserver")
    tmux.send_keys("cd webserver")
    tmux.send_keys("sudo ./start.sh")

    tmux.new_session("backup")
    tmux.send_key("cd utils")
    tmux.send_keys("python3 scheduler.py")
