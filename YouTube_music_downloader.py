from pytube import YouTube

def download_audio(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Extract the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download the audio
        audio_stream.download(output_path='D:\YouTubeDownloader', filename_prefix='audio_')
        
        print(f"Audio downloaded successfully: {audio_stream.title}")
    except Exception as e:
        print(f"An error occurred: {e}")

    

# Replace 'your_video_url_here' with the YouTube video URL
download_audio('https://youtu.be/JGUVB19e13s') 
