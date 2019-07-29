# backup-config-sw
This program copies the configuration from a cisco network device to a .txt file. 
I know this is not the best way to backup a network device, and cisco has built in tools that already does that, or there are FTP servers for this, but it was interesting if I could create a script that captures the device configuration to a .txt from a SSH connection and save it to a server or a computer. 
You have to take into account the possibility that there may be a firewall preventing the access to a network device from SSH. The server/computer that has this script must have access to the network devices (switches/routers/firewall).

This program uses cisco commands like "sh run" and "term len 0". If you have another vendor you may need to change this.

This program is designed for educational purposes only. It is not intended to be used in production and as a backup script. The security of the devices may be compromised if this script is accessed. Use it at your own risk.
