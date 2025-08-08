import os
import time

def get_cpu_temp():
    temp_str = os.popen("vcgencmd measure_temp").readline()
    return temp_str.replace("temp=", "").strip()

def get_voltage():
    volt_str = os.popen("vcgencmd measure_volts").readline()
    return volt_str.replace("volt=", "").strip()

def main():
    print("Raspberry Pi System Monitor")
    print("---------------------------")
    try:
        while True:
            temp = get_cpu_temp()
            voltage = get_voltage()
            print(f"CPU Temperature: {temp} | Core Voltage: {voltage}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting system monitor.")

if __name__ == "__main__":
    main()
