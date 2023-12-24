# Solutions to Problems I've Encountered

## [Unable to get Video feed from D-Link DCS 932L using openCv](https://stackoverflow.com/questions/20610479/unable-to-get-video-feed-from-d-link-dcs-932l-using-opencv)

```c++
#include <opencv/cv.h>
#include <opencv/highgui.h>
using namespace cv;

int main(int argc, char *argv[])
{
Mat frame;
namedWindow("video", 1);
String url = "http://admin:admin@172.32.20.55:80/image/jpeg.cgi";
VideoCapture cap(url);
/*   VideoCapture cap(0);*/
while ( cap.isOpened() )
{
    cap >> frame;
    if(frame.empty()) break;

    imshow("video", frame);
    if(waitKey(30) >= 0) break;
}

return 0;
```

I solved my problem. The problem was with URL. I changed the URL and it worked smooth..! The URL i used was as follows.

```c++
"http://USER:PWD@IPADDRESS:8088/mjpeg.cgi?user=USERNAME&password=PWD&channel=0&.mjpg";
```
