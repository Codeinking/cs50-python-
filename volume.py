import wave,audioop
import os,sys
import winsound

#winsound.PlaySound("waves.wav",winsound.SND_FILENAME)
def volume(input,output,factor):
    winsound.PlaySound(input,winsound.SND_FILENAME)
    
    with wave.open(input,"rb") as wav_in:
        params = wav_in.getparams()
        sample_width = wav_in.getsampwidth()
        raw_frames = wav_in.readframes(wav_in.getnframes())
        
    modified_frames = audioop.mul(raw_frames, sample_width, float(factor))
    
    with wave.open(output, "wb") as wav_out:
        wav_out.setparams(params)
        wav_out.writeframes(modified_frames)
        
    winsound.PlaySound(output,winsound.SND_FILENAME)
        
    
volume(sys.argv[1], sys.argv[2], sys.argv[3])