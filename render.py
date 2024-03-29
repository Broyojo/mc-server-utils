import os
import time

import minecraft
import tmux
import utils


def render_main(server="survival"):
    utils.log(f"Rendering {server}...")

    minecraft.say(server, "Copying world file...")
    utils.log(f"Copying {server} world file...")
    minecraft.save_off(server)

    time.sleep(1)

    os.system(
        f"rsync -avz --delete /home/broyojo/main/{server}/world /home/broyojo/tmp"
    )

    minecraft.say(server, "Finished copying world!")
    utils.log(f"Done copying {server} world file!")
    minecraft.save_on(server)

    minecraft.say(server, "Starting render...")
    utils.log("Starting render...")

    os.system("overviewer.py --config=render_config.py")
    os.system("overviewer.py --config=render_config.py --genpoi")

    minecraft.say(server, "Render completed!")
    utils.log("Render completed!")


if __name__ == "__main__":
    render_main()
