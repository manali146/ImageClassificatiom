from bing_image_downloader import downloader
downloader.download("human being", limit=50, output_dir='images', adult_filter_off='True')
downloader.download("robot", limit=50, output_dir='images', adult_filter_off='True')

