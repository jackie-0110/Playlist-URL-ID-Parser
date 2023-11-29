def url_extraction():
    import pytube as tube
    from pytube import Playlist
    from pytube import extract
    p = Playlist(input("Please input a playlist URL \n"))
    for url in p.video_urls:
        id = extract.video_id(url)
        print(id)
url_extraction()