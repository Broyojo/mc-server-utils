import os
import time
import minecraft
import utils


def backup(dir=minecraft.MAIN):
    for server in minecraft.servers(dir):
        utils.log(f"Backing up {server}...")
        minecraft.say(server, "Backing up server...")
        minecraft.save_off(server)

    time.sleep(2)

    os.system(
        f"tar -zcvf {minecraft.BACKUPS}\"$(TZ=America/New_York date +%Y-%m-%d).gz\" {dir}")  # TODO: add -C

    for server in minecraft.servers(dir):
        minecraft.say(server, "Backup complete!")
        minecraft.save_on(server)


def upload(bucket="s3://broyojo-minecraft"):
    utils.log("Uploading to AWS S3...")
    os.system(
        f"aws s3 sync /home/broyojo/backups {bucket} --storage-class=STANDARD_IA --profile=default")


if __name__ == "__main__":
    backup()
    upload()
