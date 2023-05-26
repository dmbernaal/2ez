# 2ez 
## Overview
This is an Audio Transcription App built in Python. The application takes an m3u8 video link URL, downloads it, splits it into audio chunks, and transcribes the chunks into text. The final transcription is written to a text file. This application leverages the power of OpenAI's Whisper API for the audio transcription.

The main reason behind this app is simply to help students with transcribing video lectures from apps such as BlackBoard and others. I've noticed some lectures don't grant the ability to download lecture and that some of the other functionality within these apps are extremely buggy often not working.

## Features
- Download videos from URL.
- Convert downloaded videos to audios.
- Split the audio into chunks.
- Transcribe the audio chunks.
- Store the transcription in a text file.

# Installation
Make sure Python3 is installed. Clone the repository and navigate to the project directory. Install the required packages using the following command:

``` bash
pip install -r requirements.txt
```

## Environment Variables
For the application to run correctly, you must define the following environment variable:

- **OPENAI_API_KEY** - The OpenAI API Key is needed to make calls to the OpenAI Whisper API for audio transcription.

You can set it up in the .env file:

```bash
OPENAI_API_KEY=your-api-key
```

## Usage
Run the application using the command:

```bash
python main.py --url <url-of-the-video> --output <name-of-output-file>
```
Here, **<url-of-the-video>** should be replaced with the URL of the video that you want to transcribe. **<name-of-output-file>** should be replaced with the name of the output file where you want to store the transcription. If no output file is specified, the transcription will be written to output.txt by default.

You can also set the verbose flag to False if you do not want the step by step print statements:

```bash
python main.py --url <url-of-the-video> --output <name-of-output-file> --verbose False
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the terms of the MIT license.