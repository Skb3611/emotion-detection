# Emotion Detection using Deep Learning

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/atulapra/Emotion-detection.git
cd Emotion-detection
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Pre-trained Model
Download `model.h5` from [here](https://drive.google.com/file/d/1FUn0XNOzf-nQV7QjbBPA6-8GLoHNNgv-/view?usp=sharing) and place it in the `src/` folder.

### 5. Start the Project
```bash
cd src
python emotions.py --mode display
```

This will open your webcam and start real-time emotion detection.

## Project Overview
- Detects 7 emotions: angry, disgusted, fearful, happy, neutral, sad, surprised
- Uses CNN trained on FER-2013 dataset
- Real-time webcam-based emotion detection
- 63.2% test accuracy

## License
MIT License
