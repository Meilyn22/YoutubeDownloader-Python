from urllib.request import urlopen
from fyouTube_video_downloader import audio_formater, video_resolution, get_link, video_downloader, audio_downloader
import pytest
import os.path


def test_get_link():
    #Please input a link to the video in order to test
    url = get_link("https://www.youtube.com/watch?v=Z0ajuTaHBtM")
    status = urlopen(url).getcode()
    assert status == 200
    
def test_video_resolution():
    #Please input a link to the video in order to test
    link =  get_link("https://www.youtube.com/watch?v=Z0ajuTaHBtM")
    assert video_resolution(link)
    
def test_audio_formater():
    #Please input a link to the video in order to test
    link =  get_link("https://www.youtube.com/watch?v=Z0ajuTaHBtM")
    assert audio_formater(link)
    
def test_audio_downloader():
    #Please input a link to the video in order to test
    link_video =  get_link("https://www.youtube.com/watch?v=Z0ajuTaHBtM")
    #Input a path on your computer. Please use two backslashes to make program recognize. 
    # For example C:\\Users\\hp\\OneDrive\\CSE111
    save_file = "C:\\Users\\samso\\Desktop\\python-last"
    assert os.path.exists(save_file)
    assert audio_downloader(link_video, save_file)
    
def test_video_downloader():
    #Please input a link to the video in order to test
    link_video =  get_link("https://www.youtube.com/watch?v=Z0ajuTaHBtM")
    #Input a path on your computer. Please use two backslashes to make program recognize. 
    # For example C:\\Users\\hp\\OneDrive\\CSE111
    save_file = "C:\\Users\\samso\\Desktop\\python-last"
    assert os.path.exists(save_file)
    assert video_downloader(link_video, save_file)
    

pytest.main(["-v", "--tb=line", "-rN", __file__])