## PyramidCola13 Routine
# Pull data from attachment

# Unzip data
unzip /data/data.zip
# Weather determination
python3 weather.py
# Add metadata
python3 metadata.py
# Image processing
python3 corona.py
# Zip post data
zip /post/post*.png post
# Send final analysis to student email
mutt spencer.riley@student.nmt.edu -s "Post Analysis Images" \
                                   -a /data/post.zip  < main_pc.txt
