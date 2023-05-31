import argparse

def parse_transcript(file_path):
    with open(file_path, 'r') as file: lines = file.readlines()
    transcript = ''
    for line in lines:
        # Skip metadata lines (WEBVTT, speaker tags) and empty lines
        if line.strip() == '' or line.strip().isdigit() or line.strip().startswith("WEBVTT") or line.strip().startswith("<") or '-->' in line:
            continue
        # Add the line to the transcript, removing trailing newlines and adding a space
        transcript += line.strip() + ' '
    return transcript

def save_transcript(output, transcript): 
    with open(output, 'w') as file: file.write(transcript)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--fpath", type=str, required=True)
    args.add_argument("--output", default="output.txt", type=str, required=True)
    args = args.parse_args()
    transcript = parse_transcript(args.fpath)
    save_transcript(args.output, transcript)
