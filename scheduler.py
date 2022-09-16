import backup
import render
import schedule
import time
import utils

def run_task(name, task):
    utils.log(f"Starting scheduled task {name}...")
    task()
    utils.log(f"Done with scheduled task {name}!")

def backup_process():
    run_task("backup", backup.backup)
    run_task("upload", backup.upload)

def render_process():
    run_task("render", render.render_main)

def main():
    #schedule.every(3).days.at("04:00").do(backup_process)  # midnight in EST
    schedule.every(1).days.at("05:00").do(render_process)  # 1 AM
    utils.log("Task scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
