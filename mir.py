import librosa
import pretty_midi

class mir:
    
    def __init__(self, input_wav):
        self.input = input_wav
        self.midi = []
        self.base_pitch = 0
        self.length = 0
        self.tempo = 0
    
    def get_tempo(self):
        return self.tempo

    def get_length(self):
        return self.length

    def get_base_pitch(self):
        return self.base_pitch

    def get_midi(self):
        return self.midi

    def get_onset(self):
        return librosa.onset.onset_detect(self.input)
    
    