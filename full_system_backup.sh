sudo rsync -aAXv --delete / --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/home/*",/root/.cache/go-build} /home/broyojo/system_backup
