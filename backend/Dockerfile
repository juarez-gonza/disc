FROM python:3
EXPOSE 8000
WORKDIR /pedidos
COPY /pedidos/requirements.txt /pedidos
RUN pip install -r requirements.txt
COPY /pedidos/ /pedidos/
ENTRYPOINT ./changes_n_run.sh
