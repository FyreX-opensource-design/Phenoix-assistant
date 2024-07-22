#~/bin/bash

## distro functions
apt_install(){
    sudo apt install espeak ffmpeg libespeak1
}

pacman_install (){
    sudo pacman -S espeak ffmpeg libespeak1 python-pipenv
}

#checks distro
. /etc/os-release
if [$ID == "ubuntu" || "debian"]; then
    apt_install
else if [$ID == "arch"]; then
    pacman_install
else
    echo "unsupported distro $ID"
fi

cp "phenoix assistant.desktop" /usr/local/share/applications/ #adds desktop image. works for GNOME and KDE
cp "phenoix assistant.desktop" /etc/xdg/autostart/

curl -fsSL https://install.julialang.org | sh -s --yes #installs julia and pkgs to system
juliaup update release
julia -e 'import Pkg && Pkg.add("JustSayIt")'
python3 -m venv phenoix #setups pyvenv
phenoix/bin/pip3 install pyttsx3 playaudio whatnow requests geocoder
