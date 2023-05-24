import argparse
import os
from audio import m3u8ToMP4, split_audio, load_file_as_bytes
from whisper import transcribe_audio_chunks

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--url", type=str, required=True)
    argparse.add_argument("--output", default="output.txt", type=str, required=True)
    argparse.add_argument("--verbose", default=True, type=bool, required=False)

    args = argparse.parse_args()

    # Download the m3u8 file
    if args.verbose: print("Downloading m3u8 file...")
    m3u8_file_path = m3u8ToMP4(args.url)

    # load the m3u8 file as a byte stream
    if args.verbose: print("Loading m3u8 file as a byte stream...")
    m3u8_file = load_file_as_bytes(m3u8_file_path)

    # Split the audio into chunks
    if args.verbose: print("Splitting the audio into chunks...")
    audio_chunks = split_audio(m3u8_file, input_audio_format="mp4", output_audio_format="mp3", chunk_duration=60, min_duration_for_chunking=300)

    # Transcribe the audio chunks
    if args.verbose: print("Transcribing the audio chunks...")
    transcription = transcribe_audio_chunks(audio_chunks)

    # Write the transcription to a file
    if args.verbose: print("Writing the transcription to a file...")
    with open(args.output, "w") as f: f.write(transcription)

    # delete video file
    if args.verbose: print("Deleting the video file...")
    os.remove("./_temp/output.mp4")

