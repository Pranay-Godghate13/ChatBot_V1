# 1. Use a lightweight Python image
FROM python:3.11-slim

# 3. Set working directory
WORKDIR /app

# 5. Copy requirements first (for caching)
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 7. Copy application code
COPY . .

# 8. Expose port (if using FastAPI / Streamlit)
EXPOSE 8000

# 9. Run the app
CMD ["python", "app.py"]
