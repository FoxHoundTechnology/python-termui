# main.py
import sys
import asyncio
import ipaddress
from reboot import reboot_device

class MinerManager:
    def __init__(self):
        self.commands = {
            'reboot': self.reboot_command,
            'sleep': self.sleep_command,
            'normal': self.normal_command
        }

    def print_header(self):
        print("\n===== Foxhound Miner Management =====")
        print(f"\nhashrate: ")
        print(f"machines: \n")
        print("=====================================")
        # print("Command format: cmd ip_start-ip_end")
        print("Type 'help' for available commands or 'exit' to quit")

    def print_help(self):
        print("\nAvailable commands:")
        print("reboot ip_start-ip_end - Reboot miners in the specified IP range")
        print("sleep ip_start-ip_end - Put miners in sleep mode (not implemented)")
        print("normal ip_start-ip_end - Set miners to normal mode (not implemented)")
        print("low ip_start-ip_end - Set miners to low power mode (not implemented)")
        print("exit - Exit the program")

    async def reboot_command(self, start_ip, end_ip):
        print(f"Rebooting miners from {start_ip} to {end_ip}")
        await self.process_ip_range(start_ip, end_ip, 'reboot')

    async def sleep_command(self, start_ip, end_ip):
        print(f"Sleep command not implemented. IP range: {start_ip} to {end_ip}")

    async def normal_command(self, start_ip, end_ip):
        print(f"Normal command not implemented. IP range: {start_ip} to {end_ip}")

    async def process_ip_range(self, start_ip, end_ip, action):
        start = ipaddress.ip_address(start_ip)
        end = ipaddress.ip_address(end_ip)
        
        tasks = []
        current = start
        while current <= end:
            if action == 'reboot':
                tasks.append(reboot_device(str(current)))
            current += 1

        await asyncio.gather(*tasks)

    async def run(self):
        self.print_header()

        while True:
            command = input().strip().lower()
            if command == 'exit':
                print("Exiting...")
                sys.exit(0)
            elif command == 'help':
                self.print_help()
            else:
                try:
                    cmd, ip_range = command.split(' ', 1)
                    start_ip, end_ip = ip_range.split('-')
                    
                    if cmd in self.commands:
                        await self.commands[cmd](start_ip, end_ip)
                    else:
                        print(f"Unknown command: {cmd}")
                except ValueError:
                    print("Invalid command format. Use: cmd ip_start-ip_end")
                except Exception as e:
                    print(f"Error processing command: {e}")

async def main():
    manager = MinerManager()
    await manager.run()

if __name__ == "__main__":
    asyncio.run(main())