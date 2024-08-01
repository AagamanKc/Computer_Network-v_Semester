const multer = require('multer');

const upload = multer({
    dest: './uploads/',
    limits: { fileSize: 1000000 }, // 1MB
    fileFilter(req, file, cb) {
        if (!file.originalname.match(/\.(jpg|jpeg|png)$/)) {
            return cb(new Error('Only image files are allowed!'));
        }
        cb(null, true);
    },
});

module.exports = upload;