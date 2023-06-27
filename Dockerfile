FROM python:3.10.12-alpine3.17
ENV PYTHONUNBUFFERED=1

#en que directorio queremos trabajar
WORKDIR /app

#actualizar e instalar paquetes y actualizar pip
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip


#copiar los archivos para preparar el equipo
COPY ./requirements.txt ./

#instalar la librerias 
RUN pip  install -r requirements.txt

#copiar el proyecto 
COPY ./projectConsulta ./

#ejecutar el proyecto
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]