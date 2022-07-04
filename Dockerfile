FROM python:3.9.1
WORKDIR /src
RUN pip install pillow
RUN pip install numpy
COPY . .
EXPOSE 80
CMD ["python", "convert_topographic_map.py"]
 