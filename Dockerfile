FROM python:3.9.1
WORKDIR /src
RUN pip install pillow
COPY . .
EXPOSE 80
CMD ["python", "pixel-rgb.py"]

# docker run -it --rm --name rgb -v "C:\Users\<user>\git\pixel-rgb\output:/src/output" rgb