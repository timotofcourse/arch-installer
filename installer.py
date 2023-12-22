import os
import argparse


parser = argparse.ArgumentParser(description='Arch Linux Install Tool', epilog='This Arch Installer has Super Cow powers')
parser.add_argument('--lang', '-l', type=str, help='Set the system language')
parser.add_argument('--keyboard', '-kbd', type=str, help='Set the keyboard')
parser.add_argument('--disk', '-dsk', type=str, help='Select the disk you want to install the system to (IT WILL WIPE THE DRIVE)')
parser.add_argument('--user', '-u', type=str, help='Set the username for your user')
parser.add_argument('--password', '-p', type=str, help='Set the password for your user')



args = parser.parse_args()

country = 'test'


os.system('timedatectl')

if args.lang:
    
    os.system() # Run the commands needed

# Disks logic
    
def partition_disk(disk_name):
    commands = [
        f'parted /dev/{disk_name} mklabel gpt',
        f'parted /dev/{disk_name} mkpart ESP fat32 1MiB 501MiB',
        f'parted /dev/{disk_name} set 1 boot on',
        f'parted /dev/{disk_name} mkpart primary ext4 501MiB 100%'
        f'mkfs.fat -F32 {disk_name}1'
        f'mkfs.ext4 {disk_name}2' 
    ]
    for cmd in commands:
        os.system(cmd)

if args.disk:

    partition_disk(args.disk)

    efi_partition = f'/dev/{args.disk}1'
    root_partitiln = f'/dev/{args.disk}2'
    

# Mount partitions
    
os.system(f'mount {root_partitiln} /mnt')
os.system(f'mount --mkdir {efi_partition} /mnt/boot')


# Select mirrors

os.system('reflector --country "{country}" --age 5 --protocol https --sort rate --save /etc/pacman.d/mirrorlist')

# Install packages

os.system("sed -i '/\[multilib\]/,/Include/s/^#//g' /etc/pacman.conf")
os.system("sed -i 's/#ParallelDownloads = 5/ParallelDownloads = 16/g' /etc/pacman.conf")
os.system("sed -i '/# Misc options/a ILoveCandy' /etc/pacman.conf")

# I'll make this lists later to make it faster to me to install Arch Linux with diffrent Desktops. Anyway i'll make the common packages to give me the packages i'll always install


# kde_packages = ['bluedevil' 'breeze-gtk' 'discover' 'drkonql' 'kde-gtk-config' 'kdeplasma-addons' 'kgamma' 'khotkeys' 'kinfocenter' 'kscreen' 'ksshaskpass' 'kwallet-pam' 'kwayland-integration' 'kwrited' 'oxygen' 'oxygen-sounds' 'plasma-browser-integration' 'plasma-desktop' 'plasma-disks' 'plasma-firewall' 'plasma-nm' 'plasma-pa' 'plasma-thunderbolt' 'plasma-vault' 'plasma-welcome' 'plasma-workspace-wallpapers' 'powerdevil' 'sddm-kcm' 'xdg-desktop-portal-kde' 'flatpak-kcm 'packagekit-qt5' 'packagekit-qt6']
# gnome_packages = ['baobab' 'cheese' 'evince' 'gdm' 'gnome-backgrounds' 'gnome-calculator' 'gnome-calendar' 'gnome-characters' 'gnome-clocks' 'gnome-color-manager' 'gnome-control-center' 'gnome-font-viewer' 'gnome-keyring' 'gnome-menus' 'gnome-music' 'gnome-photos' 'gnome-session' 'gnome-gnome-settings-daemon' 'gnome-shell' 'gnome-shell-extensions' 'gnome-software' 'grilo-plugins' 'gvfs' 'gvfs-goa' 'gvfs-google' 'gvfs-gphoto2' 'gvfs-mtp' 'gvfs-nfs' 'gvfs-smb' 'nautilus' 'orca' 'rygel' 'sushi' 'xdg-desktop-portal-gnome' 'xdg-user-dirs-gtk' 'gnome-packagekit']
# hyprland_packages = ['hyprland' 'hyprpaper' 'waybar']
# xfce_packages = ['exo' 'thunar' 'ristretto' 'xdg-desktop-portal-xapp' 'xfce4-appfinder' 'xfce4-artwork' 'xfce4-battery-plugin' 'xfce4-clipman-plugin' 'xfce4-datetime-plugin' 'xfce4-mount-plugin' 'xfce4-mpc-plugin' 'xfce4-notes-plugin' 'xfce4-notifyd' 'xfce4-panel' 'xfce4-power-manager' 'xfce4-screensaver' 'xfce4-session' 'xfce4-settings' 'xfce4-taskmanager' 'xfce4-whiskermenu-plugin' 'xfce4-xkb-plugin' 'xfdesktop' 'xfwm4' 'xfwm4-themes']
# cinnamon_packages = ['cinnamon' 'cinnamon-control-center' 'cinnamon-desktop' 'cinnamon-screensaver' 'cinnamon-session' 'cinnamon-settings-daemon' 'cinnamon-translations' 'cjs' 'muffin' 'nemo' 'xdg-desktop-portal-xapp']
# lxqt_packages = ['liblxqt' 'lximage-qt' 'lxqt-about' 'lxqt-admin' 'lxqt-archiver' 'lxqt-config' 'lxqt-globalkeys' 'lxqt-notificationd' 'lxqt-menu-data' 'lxqt-openssh-askpass' 'lxqt-panel' 'lxqt-policykit' 'lxqt-powermanagement' 'lxqt-qtplugin' 'lxqt-runner' 'lxqt-session' 'lxqt-themes' 'pcmanfm-qt' xdg-desktop-portal-lxqt']
# deepin_packages = []
# budgie_packages = []
# cosmic_packages = []

common_packages = ['base' 'linux' 'linux-firmware' 'git' 'go' 'base-devel' 'pacman-contrib' 'dosfstools' 'btrfs-progs' 'e2fsprogs' 'ntfs-3g' 'udftools' 'xfsprogs' 'apparmor' 'networkmanager' 'nano' 'vivaldi' 'flatpak' 'packagekit' 'sl' 'wireplumber' 'virt-manager' 'ufw' 'tk' 'python-ruamel-yaml' 'plymouth' 'pipewire' 'pipewire-alsa' 'pipewire-pulse' 'pipewire-jack' 'opendesktop-fonts' 'fwupd' 'fwupd-efi' 'bitwarden' 'timeshift' 'archlinux-contrib' 'appimagelauncher' 'flameshot' 'alacritty' 'xdg-desktop-portal']


# Gen fs tab

# Time

# Locale gen

# Initramfs

# Add user

# 
