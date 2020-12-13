#Run camera in video mode, and pipe output to VLC media plater
raspivid -o - -t 0 -hf -vf -w 640 -h 360 -fps 25 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264
