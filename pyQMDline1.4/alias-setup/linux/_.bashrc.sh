echo 'BE AWARE OF THE RISK THAT YOUR .bashrc MIGHT GET DESTROYED'
echo 'THIS SCRIPT WILL BACK YOUR .bashrc FILE IN YOUR DESKTOP'

echo 'welcome to the alias setup for PyQMDline (.bashrc edition)'
echo 'setup will start soon (ctrl + c to cancel)'
sleep 5s
echo 'starting the setup, press ctrl + c to cancel any time'

read -p "what is your python alias [exs. python3.9] >> " python_alias
read -p "where is the pyQMD folder located [ path/to/pyqmd ] >> " pyQMD_folder
echo 'writing the pyQMD alias to /home/'$USER

echo 'making a backup of bash_profile'
cp /home/$USER/.bashrc /home/$USER/Desktop/bashrc_backup.txt

sudo echo "alias pyQMD='cd "$pyQMD_folder "&& "$python_alias $pyQMD_folder"/__main__.py'" >> '/home/'$USER'/.bashrc'
echo "please make a new bash window for changed to take"
sleep 5s