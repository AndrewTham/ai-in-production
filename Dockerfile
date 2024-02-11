FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

ENV PORT=8000

COPY requirements.txt .

RUN python -m pip install --upgrade pip &&\
    pip install --upgrade --force-reinstall -r requirements.txt

WORKDIR /code

COPY . .

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "/code/entrypoint.sh" ]