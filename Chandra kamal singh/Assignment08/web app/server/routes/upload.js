const express = require('express');
const router = express.Router();
const upload = require('../middleware/multer');

router.post('/', upload.array('files[]', 12), (req, res) => {
    const files = req.files;
    const fileNames = files.map((file) => file.originalname);

    res.json({ files: fileNames });
});

module.exports = router;