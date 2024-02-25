import subprocess
import schedule
import time

def stop_and_remove_containers():
    try:
        # Stop and remove all running Docker containers excluding the current container
        container_ids = subprocess.check_output(['docker', 'ps', '-q']).decode('utf-8').split()
        if container_ids:
            subprocess.run(['docker', 'stop'] + container_ids)
        
        all_container_ids = subprocess.check_output(['docker', 'ps', '-aq']).decode('utf-8').split()
        if all_container_ids:
            subprocess.run(['docker', 'rm'] + all_container_ids)
    except subprocess.CalledProcessError as e:
        print(f"Error during container stop and removal: {e}")

def pull_and_run_images():
    try:
        # Pull and run the new set of Docker images
        images = [
            'sandmanshiri/single-ip:hu1d',
            'sandmanshiri/single-ip:ch1un',
            'sandmanshiri/single-ip:4umtp',
            'sandmanshiri/single-ip:2ua',
            'sandmanshiri/single-ip:gh1u',
            'sandmanshiri/pvc:fdm',
            'rainmanov/org:zeta',
            'sandmanshiri/single-ip:bh1u',
            'sandmanshiri/single-ip:hpl2',
            'sandmanshiri/single-ip:srsh',
            'sandmanshiri/single-ip:msz',
            'sandmanshiri/single-ip:kfkfua'
        ]
        for image in images:
            subprocess.run(['docker', 'pull', image])
            subprocess.run(['docker', 'run', '-d', image])
    except subprocess.CalledProcessError as e:
        print(f"Error during image pull and run: {e}")

def job():
    print("Running job...")
    stop_and_remove_containers()
    pull_and_run_images()

if __name__ == "__main__":
    # Run the job immediately upon script execution
    job()

    # Schedule the job to run every 8 hours
    schedule.every(4).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
