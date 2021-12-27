FROM python:3.9.1
WORKDIR /src
RUN pip install pillow
COPY . .
EXPOSE 80
CMD ["python", "convert_topographic_map.py"]
 
# docker build -t civ4-map-from-topography .
# docker run -it --rm --name civ4-map-from-topography -v "C:\Users\<user>\git\civ4-map-from-topography\output:/src/output" civ4-map-from-topography