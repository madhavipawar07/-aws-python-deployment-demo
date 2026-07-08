import paramiko

HOST = "35.154.133.229"
USERNAME = "ubuntu"          # Use "ubuntu" because your EC2 instance is Ubuntu
KEY = r"C:\Users\madha\Downloads\gitKey.pem"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("Connecting to EC2...")

client.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=KEY
)

commands = [
    "cd ~/aws-python-deployment-demo && git pull",
    "cd ~/aws-python-deployment-demo && python3 app.py"
]

for command in commands:
    print(f"Running: {command}")

    stdin, stdout, stderr = client.exec_command(command)

    print(stdout.read().decode())

    error = stderr.read().decode()
    if error:
        print(error)

client.close()

print("Deployment Completed")
