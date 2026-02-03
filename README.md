# PTSD Prediction and Analysis – Colossus 2024

This project is a machine learning–based PTSD prediction and analysis system developed using Django and Random Forest models. It analyzes user responses related to psychological symptoms and predicts trauma severity levels along with recommended therapy types. The system is currently based on text and questionnaire-based inputs, with future plans to integrate EEG-based physiological analysis.

The project uses trained machine learning models to classify trauma levels and therapy recommendations based on user-provided mental health indicators. It is designed as a web-based application for easy accessibility and real-time predictions.

---

## Features

- PTSD severity prediction using Random Forest models
- Therapy recommendation system
- Web-based interface using Django
- Kaggle-based dataset integration
- Real-time prediction through backend processing
- Modular and scalable architecture
- Future scope for EEG signal analysis

---

## Technologies Used

- Python
- Django
- Scikit-learn
- NumPy
- Joblib
- HTML/CSS
- SQLite
- Machine Learning (Random Forest)

---

## Hardware Requirements

- Minimum 4 GB RAM (8 GB recommended)
- Dual-core processor or higher
- No GPU required for current implementation
- GPU recommended for future EEG deep learning models
- Minimum 5 GB free disk space

---

## Dataset and Models

- Dataset Source: Kaggle (PTSD-related survey and psychological assessment data)
- Input Features:
  - Nightmare frequency
  - Flashbacks
  - Avoidance behavior
  - Hypervigilance
  - Emotional numbing
  - Anxiety levels

- Trained Models:
  - `random_forest_therapy_model.joblib` (Therapy prediction)
  - `random_forest_trauma_model.joblib` (Trauma severity prediction)

- Trauma Levels:
  - Mild
  - Moderate
  - Severe

- Therapy Types:
  - CBT
  - Exposure Therapy
  - Others

---

## System Architecture

User Input Form → Django Backend → ML Model Prediction → Result Display

1. User enters psychological indicators
2. Django processes form data
3. Trained Random Forest models are loaded
4. Predictions are generated
5. Results are displayed on the web interface

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/krharitej/PTSD-Prediction-and-analysis-Colossus-2024-.git
```

```bash
cd PTSD-Prediction-and-analysis-Colossus-2024-/collosus
```

Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

```bash
source venv/bin/activate      # Linux / Mac
```

```bash
venv\Scripts\activate         # Windows
```

Install Dependencies

```bash
pip install django scikit-learn numpy joblib
```

Apply Migrations

```bash
python manage.py migrate
```

Run the Server

```bash
python manage.py runserver
```

Open in browser:

```cpp
http://127.0.0.1:8000/
```

## Making Predictions

1. Open the home page
2. Navigate to the prediction form
3. Enter values for:
   Nightmare
   Flashback
   Avoidance
   Hypervigilance
   Emotional Numbing
   Anxiety
4. Submit the form
5. View predicted trauma level and therapy recommendation

Prediction Endpoint:

```bash
POST /predict/
```

## Sample Inputs and Outputs

Example Input:

| Feature           | Value |
| ----------------- | ----- |
| Nightmare         | 3     |
| Flashback         | 4     |
| Avoidance         | 2     |
| Hypervigilance    | 5     |
| Emotional Numbing | 3     |
| Anxiety           | 4     |

Example Output:

```yaml
Trauma Level: Moderate
Recommended Therapy: CBT
```

## Future Enhancements

- EEG signal integration for physiological analysis
- Deep learning models for time-series EEG data
- Mobile application integration
- REST API for external access
- Clinical data validation
