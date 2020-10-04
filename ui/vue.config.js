// vue.config.js

const webpackConfig = {
  module: {
    rules: [
      {
        test: /\.pug$/,
        loader: 'pug-plain-loader',
      },
    ],
  },
}

module.exports = {
  configureWebpack: webpackConfig,
}
