xset s off
xset -dpms
xset s noblank
cd /
cd home/pi/DNCLogger
python Logger.py &
sudo wvdial
exit 0
cd /
