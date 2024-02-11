const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

app.post('/save_entry', (req, res) => {
    const { id, url } = req.body;

    fs.appendFile('log.txt', `${id}: ${url}\n`, (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error saving entry');
        } else {
            console.log('Entry saved');
            res.status(200).send('Entry saved');
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
