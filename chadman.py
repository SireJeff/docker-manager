import subprocess
import schedule
import time

def stop_and_remove_containers():
    try:
        # Stop and remove containers with specific names
        containers_to_remove = [
            'sandmanshiri-single-ip-srsh',
            'sandmanshiri-single-ip-msz',
            'sandmanshiri-single-ip-kfkfua',
            'sandmanshiri-single-ip-tiwan07',
            'sandmanshiri-single-ip-mdfwood',
            'sandmanshiri-single-ip-Eh1u',
            'sandmanshiri-single-ip-kafafus',
            'sandmanshiri-single-ip-gh1u',
            'sandmanshiri-single-ip-mtpphys'
        ]
        subprocess.run(['docker', 'stop'] + containers_to_remove)
        #time.sleep(60)
        all_container_ids = subprocess.check_output(['docker', 'ps', '-aq']).decode('utf-8').split()
        if all_container_ids:
            subprocess.run(['docker', 'rm'] + containers_to_remove)
    except subprocess.CalledProcessError as e:
        print(f"Error during container stop and removal: {e}")
        
    

def pull_and_run_images():
    try:
        # Pull and run the new set of Docker images
        images = [
            'sandmanshiri/single-ip:srsh',
            'sandmanshiri/single-ip:msz',
            'sandmanshiri/single-ip:kfkfua',
            'sandmanshiri/single-ip:tiwan07',
            'sandmanshiri/single-ip:mdfwood',
            'sandmanshiri/single-ip:Eh1u',
            'sandmanshiri/single-ip:kafafus',
            'sandmanshiri/single-ip:gh1u',
            'sandmanshiri/single-ip:mtpphys'
        ]
        for image in images:
            image_name, image_version = image.split(':')
            repo ,ver=image_name.split('/')
           # subprocess.run(['docker', 'pull', image])
            subprocess.run(['docker', 'run', '-d', '--name', f'{repo}-{ver}-{image_version}', image])
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
    schedule.every(25).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
