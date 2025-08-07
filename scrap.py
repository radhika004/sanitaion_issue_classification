# from bing_image_downloader import downloader
# downloader.download("bad drainage water spread in india ",limit=3,output_dir="baddrainage")

from bing_image_downloader import downloader
import os

query = "brown tapwater supply in india".strip()

output_directory = "baddrainage"
os.makedirs(output_directory, exist_ok=True)

downloader.download(query, limit=500, output_dir=output_directory)
