## Blind Eye data transfer
# Take images from the camera module

# Zips data
zip /data/raw*.png raw

# Data transfer
mutt pharaohcola13@PyramidCola13 -s "Blind Eye Data Transfer" \
                                   -a ./data/raw.zip  < main_be.txt
# Notification
mutt spencer.riley@student.nmt.edu -s "Blind Eye Transfer Notification" \\
      < notification.txt
