import subprocess

def get_wifi_password(ssid):
    try:
        # Run the netsh command to retrieve the Wi-Fi password
        command = f'netsh wlan show profile name="{ssid}" key=clear'
        output = subprocess.check_output(command, shell=True).decode('utf-8')

        # Find the line containing the Key Content (password)
        key_content_line = [line for line in output.split('\n') if "Key Content" in line][0]

        # Extract the password from the line
        password = key_content_line.split(":")[1].strip()

        return password
    except Exception as e:
        print("Error retrieving Wi-Fi password:", str(e))

# Provide the SSID (network name) for which you have consent to access the password
network_name = "Your Network Name"

# Call the function to retrieve the Wi-Fi password
password = get_wifi_password(network_name)

# Print the password
print("Wi-Fi Password:", password)
