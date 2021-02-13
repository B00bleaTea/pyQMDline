echo 'BE AWARE OF THE RISK THAT YOUR .bash_aliases MIGHT GET DESTROYED'
echo 'THIS SCRIPT WILL BACK YOUR .bash_aliases FILE IN YOUR DESKTOP'

echo 'welcome to the alias setup for PyQMDline (.bash_aliases edition)'
echo 'the setup will start soon (ctrl + c to cancel)'
sleep 5s
echo 'starting the setup, press ctrl + c to cancel any time'

read -p "what is your python alias [exs. python3.9] >> " python_alias
read -p "where is the pyQMD folder located >> " pyQMD_folder
echo 'writing the alias to /home/'$USER

echo 'making a backup of bash_aliases'
cp /home/$USER/.bash_aliases /home/$USER/Desktop/bash_aliases_backup.txt

echo 'making changes to bash_profile'
echo "alias pyQMD='cd "$pyQMD_folder "&& "$python_alias $pyQMD_folder"/__main__.py'" >> '/home/'$USER'/.bash_aliases'
echo "please make a new bash window for changes to take"

sleep 5s