import nemo.collections.asr as nemo_asr

print("Loading model...")

model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="stt_en_quartznet15x5"
)


print("Model loaded.")

audio_files = ["sample1.wav", "sample2.wav"]

print("Running inference...")

transcriptions = model.transcribe(audio_files)

print("Results:")
for fname, hyp in zip(audio_files, transcriptions):
    print(f"{fname}:")
    print(hyp.text)
    print("-" * 40)

