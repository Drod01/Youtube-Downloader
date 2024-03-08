# YouTube Video Downloader

This Python script allows users to download both video and audio from a YouTube URL using the pytube library.

## Features

- Downloads both video and audio from a given YouTube URL.
- Selects the highest resolution video and highest bitrate audio available.
- Displays download progress using tqdm.

## Prerequisites

- Python 3.x installed.
- Required libraries installed (`pytube`, `tqdm`).

## Usage

1. Clone the repository or download the `youtube_downloader.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `youtube_downloader.py`.
4. Run the script using the command: `python youtube_downloader.py`.
5. Enter the YouTube video URL when prompted.
6. The script will download the video and audio into the current directory.

## Example

$ python youtube_downloader.py
Enter YouTube video URL: [https://www.youtube.com/watch?v=QSbfetvb-8Y]


## Notes

- Ensure the provided YouTube URL is accessible and valid.
- Internet connection is required for downloading.
- The downloaded files will be saved in the current directory.
- Make sure you have sufficient disk space for downloading large files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

