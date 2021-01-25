echo 'welcome to the alias setup for PyQMDline (.bashrc edition)'
echo 'setup will start soon (ctrl + c to cancel)'
sleep 5s
echo 'starting the setup, press ctrl + c to cancel any time'

read -p "what is your username on your host computer >> " username_pyQMD
read -p "what is your python alias [exs. python3.9] >> " python_alias
read -p "where is the pyQMD folder located [ path/to/pyqmd ] >> " pyQMD_folder
echo 'writing the alias to /home/'$username_pyQMD

sudo echo "alias pyQMD='cd "$pyQMD_folder "&& "$python_alias $pyQMD_folder"/__main__.py'" >> '/home/'$username_pyQMD'/.bashrc'
echo "please make a new bash window for changed to take"
sleep 10s