import argparse

class VTT:
    def __init__(self, lines): 
        self.lines = lines

    def parse(self, lines=None):
        lines = self.transcript.splitlines() if lines is None else lines
        transcript = ''
        for line in lines:
            # Skip metadata lines (WEBVTT, speaker tags) and empty lines
            if line.strip() == '' or line.strip().isdigit() or line.strip().startswith("WEBVTT") or line.strip().startswith("<") or '-->' in line:
                continue
            # Add the line to the transcript, removing trailing newlines and adding a space
            transcript += line.strip() + ' '
        return transcript
    
    def save(self, output, transcript):
        with open(output, 'w') as file: file.write(transcript)
    
    @classmethod
    def from_file(cls, fpath):
        with open(fpath, 'r') as file: lines = file.readlines()
        return cls(lines)
    
    @classmethod
    def from_string(cls, transcript): 
        return cls(transcript)

