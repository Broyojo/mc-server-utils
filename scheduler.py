import backup
import render
import schedule
import time
import utils


def run_task(name, task):
    utils.log(f"Starting scheduled task {name}...")
    task()
    utils.log(f"Done with scheduled task {name}!")


def daily_process():
    run_task("backup", backup.backup)
    run_task("render", render.render_main)


def main():
    schedule.every(1).day.at("05:00").do(daily_process)  # midnight in EST
    utils.log("Task scheduler started")
    while True:
        schedule.run_pending()
        time.sleep(5)
        print("tick")


if __name__ == "__main__":
    main()