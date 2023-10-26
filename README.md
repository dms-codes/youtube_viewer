# YouTube Video Processing with Python and Selenium

This Python script demonstrates how to use Selenium and Pandas to process a list of YouTube video URLs from a CSV file. The script mutes the audio and plays each video for 10 minutes before closing the browser window.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python
- Selenium
- Chrome WebDriver
- Pandas

You can install the required Python packages using pip:

```bash
pip install selenium pandas
```

You also need to download the Chrome WebDriver compatible with your Chrome browser version and make sure it's in your system's PATH.

## Usage

1. Place your CSV file containing video IDs in the same directory as this script. The CSV file should have a header row, and the 'Content' column should contain the video IDs.

2. Edit the script to specify the correct file name if it's different from 'data.csv'.

3. Run the script using the following command:

```bash
python youtube_video_processor.py
```

The script will process each video in the CSV file one by one.

## Script Explanation

1. The script reads the CSV file into a Pandas DataFrame and extracts the 'Content' column.

2. Chrome options are configured to mute audio during video playback.

3. The script then iterates through the video IDs, opening each video in a Chrome browser window.

4. It waits for the 'Play' button to become clickable and clicks it.

5. After playing the video for 10 minutes, it waits for the 'Replay' button to become clickable.

6. Any errors encountered during processing are printed to the console.

## Disclaimer

This script is for educational and demonstration purposes. Please ensure you comply with YouTube's terms of service and respect copyright and content usage restrictions when using such automation.

Happy video processing!
```

Make sure to customize the README.md with your project-specific information and directory structure.
