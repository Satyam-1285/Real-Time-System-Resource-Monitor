import psutil
import time
import os

def get_progress_bar(percent, width=30):
    
    filled_width = int(width * percent / 100)
    bar = "█" * filled_width + "-" * (width - filled_width)
    return f"|{bar}| {percent}%"

def clear_screen():
    """Clears the terminal screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_monitor():
    try:
        print("Starting System Monitor... Press Ctrl+C to stop.")
        time.sleep(1)
        
        while True:
            clear_screen()
            
            # Gather Data
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Header
            print("="*45)
            print(f"{'SYSTEM RESOURCE DASHBOARD':^45}")
            print("="*45)
            
            # CPU Section
            print(f"\nCPU Usage:")
            print(get_progress_bar(cpu_usage))
            
            # Memory Section
            print(f"\nMemory Usage (RAM):")
            print(get_progress_bar(memory.percent))
            print(f" Used: {memory.used // (1024**2)}MB / Total: {memory.total // (1024**2)}MB")
            
            # Disk Section
            print(f"\nDisk Usage (Main Drive):")
            print(get_progress_bar(disk.percent))
            
            # Footer
            print("\n" + "="*45)
            print("Update Frequency: 1.0s     [Ctrl+C to Exit]")
            
    except KeyboardInterrupt:
        print("\nMonitor stopped. Stay productive!")

if __name__ == "__main__":
    main_monitor()
