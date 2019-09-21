FROM python:3-onbuild
EXPOSE 8080
ENV FLASK_APP app.py

RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "-p", "8080"]