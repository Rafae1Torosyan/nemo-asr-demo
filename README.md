```markdown
# NeMo ASR Demo

A minimal hands-on project demonstrating speech-to-text inference  
using **NVIDIA NeMo** and **PyTorch**.

This repository showcases a simple end-to-end ASR (Automatic Speech Recognition) pipeline
with a pretrained model, focused on practical usage rather than training.

---

## 🚀 Overview

In this project, I:

- Loaded a pretrained ASR model from NVIDIA NeMo
- Performed speech-to-text inference on short audio samples
- Explored the structure and outputs of NeMo ASR pipelines

The goal of the project is to gain hands-on experience with NeMo and understand
how speech models are used in practice.

---

## 📁 Project Structure

```

nemo-asr-demo/
├── asr_demo.py         # main ASR inference script
├── README.md           # project description
├── requirements.txt    # Python dependencies
├── sample1.wav         # example audio file
├── sample2.wav         # example audio file

````

---

## 🛠 Requirements

- Python 3.9+
- PyTorch
- NVIDIA NeMo (ASR)

Install dependencies:

```bash
pip install -r requirements.txt
````

`requirements.txt`:

```
torch
nemo_toolkit[asr]
```

---

## ▶️ Usage

1. Place `.wav` audio files in the project directory
2. Update the `audio_files` list in `asr_demo.py` if needed
3. Run the script:

```bash
python asr_demo.py
```

The script will download a pretrained model (if not cached) and print
the transcribed text for each audio file.

---

## 🧪 Model Details

* Framework: NVIDIA NeMo
* Model: `stt_en_quartznet15x5`
* Task: Automatic Speech Recognition (ASR)
* Mode: Inference only (no training or fine-tuning)
* Hardware: CPU-compatible

---

## 💡 Example Output

```
sample1.wav:
many animals of even complex structure which live parasitically within others are wholly devoid of an elementary cavity

sample2.wav:
the examination and testimony of the experts enabled the commission to conclude that five shots may have been fired
```

---

## 🧠 Key Takeaways

* Hands-on experience with NVIDIA NeMo ASR models
* Understanding of pretrained speech models and inference pipelines
* Practical use of PyTorch-based deep learning frameworks

---

## 📌 Notes

This project is intended as a small applied demo and learning exercise.
It can be extended to include custom datasets, fine-tuning, or evaluation metrics.

---
