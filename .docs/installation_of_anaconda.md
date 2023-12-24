# Installation of Anaconda on Ubuntu

[Reference](https://docs.anaconda.com/free/anaconda/install/linux/)

## GUI Packages Update

```sh
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

## Anaconda Installer

```sh
# Get installer
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

# Verify installer's integrity

# Include the bash command even if you aren't using the Bash shell
# Replace ~/Downloads with your actual path
# Replace the .sh file name with the name of the file you downloaded
bash ./Anaconda3-2020.05-Linux-x86_64.sh

```
