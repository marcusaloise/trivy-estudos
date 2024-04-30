const path = require('path');

module.exports = {
    entry: './handler.js',
    output: {
      path: path.resolve(__dirname, './dist'),
      filename: 'handler.js',
      libraryTarget: 'commonjs'
    },
    target: 'node',
    mode: 'production'
}