FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY ./RedOrange /code/
WORKDIR /code
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host https://pypi.tuna.tsinghua.edu.cn
