const express = require('express');
const app = express();
const multer = require('multer');
const upload = multer({ dest: './uploads/' });

app.use(express.static('client'));

app.post('/upload', upload.array('files[]', 12), (req, res) => {
    const files = req.files;
    const fileNames = files.map((file) => file.originalname);

    res.json({ files: fileNames });
});

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});