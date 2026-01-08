# Enterprise AI Project Optimizer

## Overview

AI system to optimize enterprise projects by predicting:

* Project duration (`/predict`)
* Project delay risk (`/predict_delay`)
* Project cost (`/predict_cost`)

## Structure

```
enterprise-ai-project-optimizer
├── data/generate_data.py
├── ml/train.py
├── ml/train_classification.py
├── ml/train_cost.py
├── ml/predict.py
├── ml/api.py
├── projects.csv
├── requirements.txt
└── README.md
```

## Quick Start

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Generate data:

```
python data/generate_data.py
```

3. Train models:

```
python ml/train.py
python ml/train_classification.py
python ml/train_cost.py
```

4. Run API:

```
python -m uvicorn ml.api:app --reload
```

5. Access docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

* **POST /predict** → Predict project duration
* **POST /predict_delay** → Predict delay risk
* **POST /predict_cost** → Predict project cost
