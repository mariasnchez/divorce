FROM python:3.8
RUN pip install pandas scikit-learn streamlit
COPY src/app.py /app/
COPY model/divorce_model.pkl /app/model/divorce_model.pkl
COPY img/* /app/img/
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py" ]