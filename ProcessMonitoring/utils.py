import psutil
from datetime import datetime

def get_processes():
    """
    Retrieves the list of system processes with relevant details.
    This function iterates through all running processes and collects information such as process ID (PID), name, user, CPU usage percentage, memory usage (in MB),and the process start time.

    Returns:
        list: A list of dictionaries, each containing details of a process. Each 
              dictionary contains the following keys:
              - "pid": Process ID
              - "name": Process name
              - "user": Username running the process
              - "cpu": CPU usage percentage of the process
              - "memory": Memory usage in MB (rounded to two decimal places)
              - "start_time": Start time of the process in YYYY-MM-DD HH:MM:SS format
    """
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time']):
        try:
            proc_info = {
                "pid": process.info['pid'],
                "name": process.info['name'],
                "user": process.info['username'],
                "cpu": process.info['cpu_percent'],
                "memory": round(process.info['memory_info'].rss / (1024 * 1024), 2),
                "start_time": datetime.fromtimestamp(process.info['create_time']).strftime("%Y-%m-%d %H:%M:%S"),
            }
            processes.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes
