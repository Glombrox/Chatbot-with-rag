FROM python:3.12-slim

WORKDIR /app

COPY requierments.txt requierments.txt
RUN pip install --no-cache-dir -r requierments.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
