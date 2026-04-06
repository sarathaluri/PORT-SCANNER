import socket
import threading
import argparse
from queue import Queue

# Shared resources
port_queue = Queue()
open_ports = []
lock = threading.Lock()


def print_banner():
    print("=" * 60)
    print("        ADVANCED PORT SCANNER - CYBER TOOL")
    print("=" * 60)


def scan_port(target, timeout):
    while not port_queue.empty():
        port = port_queue.get()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"

                # Banner grabbing
                try:
                    sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                    banner = sock.recv(1024).decode(errors="ignore").split("\n")[0]
                except:
                    banner = banner.split("\n")[0]

                output = f"[OPEN] Port {port} ({service}) | {banner}"

                with lock:
                    print(output)
                    open_ports.append(output)

            sock.close()

        except:
            pass

        port_queue.task_done()


def run_scanner(target, start_port, end_port, threads, timeout, output_file):
    print_banner()
    print(f"\nScanning target: {target}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Threads used: {threads}")
    print(f"Timeout: {timeout}s\n")

    # Fill queue
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    # Start threads
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=scan_port, args=(target, timeout))
        t.start()
        thread_list.append(t)

    # Wait for completion
    for t in thread_list:
        t.join()

    print("\n--- SCAN COMPLETE ---")

    # Summary
    print("\n--- SUMMARY ---")
    print(f"Total open ports: {len(open_ports)}")

    # Save results
    if output_file:
        with open(output_file, "w") as f:
            for line in open_ports:
                f.write(line + "\n")
        print(f"\nResults saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Advanced Port Scanner")

    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("-to", "--timeout", type=float, default=1, help="Timeout in seconds")
    parser.add_argument("-o", "--output", help="Output file (optional)")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("Error: Invalid target")
        return

    run_scanner(target_ip, args.start, args.end, args.threads, args.timeout, args.output)


if __name__ == "__main__":
    main()