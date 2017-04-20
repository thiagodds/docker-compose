FROM node:4.8.2

LABEL adminmongo="MongoAdmin"
LABEL version="1.0"

RUN mkdir /etc/app
RUN git clone https://github.com/mrvautin/adminMongo.git /etc/app
RUN cd /etc/app && npm install

WORKDIR /etc/app

CMD ["npm", "start"]