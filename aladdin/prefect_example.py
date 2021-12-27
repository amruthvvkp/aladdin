import time

from prefect import task, flow
from prefect.task_runners import DaskTaskRunner

@task
def print_values(values):
    for value in values:
        time.sleep(0.5)
        print(value, end="\r")

@flow(task_runner=DaskTaskRunner())
def parallel_flow():
    print_values(["AAAA"] * 15)
    print_values(["BBBB"] * 10)

if __name__ == "__main__":
    parallel_flow()
