FROM node:12

WORKDIR /usr/src/udk

COPY package.json yarn.lock ./

RUN yarn install --production=false

COPY . .

EXPOSE 8080

CMD ["yarn", "serve"]
