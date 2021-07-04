# init venv
sudo apt install -y python3-venv
mkdir venv
cd venv
python3 -m venv my-env
cd ..

# python bash
. ./python-bash.sh

# install libraries
pip install -r requirements.txt

# # go to src
cd justext

# # run main
python main.py

