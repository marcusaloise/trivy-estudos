'use strict';

const twit = require('twit');
const moment = require('moment')

require('dotenv').config();

exports.handler = (event, context, callback) => {
  const config = {
    consumer_key: process.env.CONSUMER_KEY,
    consumer_secret: process.env.CONSUMER_SECRET,
    access_token: process.env.ACCESS_TOKEN,
    access_token_secret: process.env.ACCESS_TOKEN_SECRET
  }

  const Twitter = new twit(config);

  const currentDate = moment();
  const nextDate = moment(process.env.THE_DATE, "DD-MM-YYYY HH:mm");

  const daysLeft = nextDate.diff(currentDate, 'days');

  let message = '';

  if (daysLeft > 1) {
    message = `te vejo em ${daysLeft} dias`;
  } else if (daysLeft === 1) {
    message = 'te vejo amanhã';
  }

  if (message != '') {
    Twitter.post('/statuses/update', { status: message }, function(err, data, response) {
      if (err) {
        console.log(`Tweet was not posted. Errorcode: ${err}`)
      } else {
        console.log('Tweet posted.')
      }
    });
  }
}