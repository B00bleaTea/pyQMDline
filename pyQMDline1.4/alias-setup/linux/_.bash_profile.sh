echo 'BE AWARE OF THE RISK THAT YOUR .bash_profile MIGHT GET DESTROYED'
echo 'THIS SCRIPT WILL BACK YOUR .bash_profile FILE IN YOUR DESKTOP'

echo 'welcome to the alias setup for PyQMDline (.bash_profile edition)'
echo 'setup will start soon (ctrl + c to cancel)'
sleep 5s
echo 'starting the setup, press ctrl + c to cancel any time'

read -p "what is your python alias [exs. python3.9] >> " python_alias
read -p "where is the pyQMD folder located [exs. /home/john] >> " pyQMD_folder
echo 'writing the alias to /home/'$USER

echo 'making a backup of bash_profile'
cp /home/$USER/.bash_profile /home/$USER/Desktop/bash_profile_backup.txt

echo 'making changes to bash_profile'
echo "alias pyQMD='cd "$pyQMD_folder "&& "$python_alias $pyQMD_folder"/__main__.py'" >> '/home/'$USER'/.bash_profile'
echo "please make a new bash window for changes to take"

sleep 5s