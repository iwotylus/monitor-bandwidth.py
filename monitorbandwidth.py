import sys
import time
import psutil
from psutil._common import bytes2human

def main():
	total_bytes_recv = 0
	total_bytes_sent = 0
	total_packets_recv = 0
	total_packets_sent = 0

	try:
		initial_io_stats = psutil.net_io_counters()

		while(True):
			old_io_stats = psutil.net_io_counters()

			time.sleep(1)

			new_io_stats = psutil.net_io_counters()

			bytes_recv = new_io_stats.bytes_recv - old_io_stats.bytes_recv
			bytes_sent = new_io_stats.bytes_sent - old_io_stats.bytes_sent
			packets_recv = new_io_stats.packets_recv - old_io_stats.packets_recv
			packets_sent = new_io_stats.packets_sent - old_io_stats.packets_sent

			total_bytes_recv += bytes_recv
			total_bytes_sent += bytes_sent
			total_packets_recv += packets_recv
			total_packets_sent += packets_sent

			print(f"Received: {bytes2human(bytes_recv):>10}, Sent: {bytes2human(bytes_sent):>10}, "
            	f"Packets sent: {packets_sent:>8}, Packets received: {packets_recv:>8}")
	
	except KeyboardInterrupt:
		print("\n")
		print(f"Total received: {bytes2human(total_bytes_recv):>10}, Total sent: {bytes2human(total_bytes_sent):>10}, "
       		f"Total packets received: {total_packets_recv:>8}, Total packets sent: {total_packets_sent:>8}")

if __name__ == '__main__':
	main()
