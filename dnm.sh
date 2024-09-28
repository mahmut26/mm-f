
sudo apt install cmake 
sudo apt install valac 
sudo apt install libwebkit2gtk-4.0-dev 
sudo apt install libgcr-3-dev 
sudo apt install libpeas-dev 
sudo apt install libsqlite3-dev 
sudo apt install libjson-glib-dev 
sudo apt install libarchive-dev 
sudo apt install intltool 
sudo apt install libxml2-utils
curl -O -L https://github.com/midori-browser/core/releases/download/v9.0/midori-v9.0.tar.gz
cd midori-v9.0
mkdir _build
cd _build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make
sudo make install
