
# RESTORE SCRIPT - Run this in a single cell on Thursday
from google.colab import drive
drive.mount('/content/drive')
import os
os.environ['PATH'] += os.pathsep + os.path.expanduser('~/.cargo/bin')

# Kill existing servers
os.system("pkill -f flask")
os.system("pkill -f python.*demo")

# Extract monorepo
os.system("tar -xzf /content/drive/MyDrive/monorepo_backup.tar.gz -C / 2>/dev/null")
print("✅ Restored monorepo")

# Copy demo file
os.system("cp /content/drive/MyDrive/demo_backup.py /content/demo_100_nodes_final.py 2>/dev/null")
print("✅ Restored demo file")

# Start the demo
os.chdir("/content/monorepo")
os.system("python /content/demo_100_nodes_final.py")
