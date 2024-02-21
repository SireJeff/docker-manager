import subprocess
import schedule
def stop_and_remove_containers():
    # Stop and remove all running Docker containers excluding the current container
    container_ids = subprocess.check_output(['docker', 'ps', '-q']).decode('utf-8').split()
    if container_ids:
        subprocess.run(['docker', 'stop'] + container_ids)
    all_container_ids = subprocess.check_output(['docker', 'ps', '-aq']).decode('utf-8').split()
    if all_container_ids:
        subprocess.run(['docker', 'rm'] + all_container_ids)

def pull_and_run_images():
    # Pull and run the new set of Docker images
    images = [
        'sandmanshiri/single-ip:hu1d',
        'sandmanshiri/single-ip:ch1un',
        'sandmanshiri/single-ip:4umtp',
        'sandmanshiri/single-ip:2ua',
        'sandmanshiri/single-ip:gh1u',
        'sandmanshiri/pvc:fdm',
        'rainmanov/org:zeta',
    ]
    for image in images:
        subprocess.run(['docker', 'pull', image])
        subprocess.run(['docker', 'run', '-d', image])

def job():
    print("Running job...")
    stop_and_remove_containers()
    pull_and_run_images()

if __name__ == "__main__":
    # Run the job immediately upon script execution
    job()

    # Schedule the job to run every 8 hours
    schedule.every(3).minuets.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)