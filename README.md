# Dashboard Model Prediksi Penyakit Jantung
## Setup Virtual Environment


1. **Setup Environment Anaconda**:
    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    pip install -r requirements.txt
    ```

2. **Setup Environment - Shell/Terminal**:
    ```bash
    mkdir heart_disease_dashboard
    cd heart_disease_dashboard
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```
