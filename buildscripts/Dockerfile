FROM python:3-onbuild
EXPOSE 8080
ENV FLASK_APP ../app/app.py

RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run"]
