FROM UserXTester/Man_Userbot:buster

RUN git clone -b Man_Userbot https://github.com/UserXTester/Man_Userbot /home/manuserbot/ \
    && chmod 777 /home/manuserbot \
    && mkdir /home/manuserbot/bin/

COPY ./sample_config.env ./config.env* /home/manuserbot/

WORKDIR /home/manuserbot/

CMD ["python3", "-m", "userbot"]
