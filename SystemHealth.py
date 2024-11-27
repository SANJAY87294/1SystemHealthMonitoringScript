import psutil
import logging
from datetime import datetime

# Logging configuration
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Thresholds
CPU_THRESHOLD = 80  # Percent
MEMORY_THRESHOLD = 80  # Percent
DISK_THRESHOLD = 80  # Percent
PROCESS_COUNT_THRESHOLD = 200  # Number of processes

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f"High CPU usage: {cpu_usage}%"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        message = f"High Memory usage: {memory_usage}%"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"Memory usage is normal: {memory_usage}%")

def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        message = f"Low Disk Space: {disk_usage}% used"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"Disk space is normal: {disk_usage}% used")

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        message = f"High number of running processes: {process_count}"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"Running process count is normal: {process_count}")

def main():
    print(f"System Health Monitoring started at {datetime.now()}")
    logging.info("System Health Monitoring started")
    
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()
    
    print("System Health Monitoring completed.\n")
    logging.info("System Health Monitoring completed")

if __name__ == "__main__":
    main()
