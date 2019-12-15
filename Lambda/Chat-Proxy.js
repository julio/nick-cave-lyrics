'use strict';

var AWS = require('aws-sdk');

var S3 = new AWS.S3();

var bucket = 'moretime-io-nick-cave-lyrics';

exports.handler = function (event, context, callback) {

    const done = function (err, res) {
        callback(null, {
            statusCode: err ? '400' : '200',
            body: err ? JSON.stringify(err) : JSON.stringify(res),
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'http://moretime-io-nick-cave-lyrics.s3-website-us-west-1.amazonaws.com'
            }
        });
    };

    var path = event.pathParameters.proxy;

    if (path === 'albums') {
        S3.getObject({
            Bucket: bucket,
            Key: 'data/albums.json'
        }, function (err, data) {
            done(err, err ? null : JSON.parse(data.Body.toString()));
        });
    } else if (path.startsWith('albums/')) {
        var id = path.substring('albums/'.length);
        S3.getObject({
            Bucket: bucket,
            Key: 'data/albums/' + id + '.json'
        }, function (err, data) {
            done(err, err ? null : JSON.parse(data.Body.toString()));
        });
    } else {
        done('No cases hit');
    }
};