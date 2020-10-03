FROM node:12

# RUN npm install -g --force yarn
# RUN yarn set version berry
# RUN yarn global add @vue/cli

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

EXPOSE 8080

CMD ["yarn", "serve"]
