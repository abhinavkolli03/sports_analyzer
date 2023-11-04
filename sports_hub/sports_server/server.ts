import express from 'express';
import path from 'path';
import 'dotenv/config';
import { fileURLToPath } from 'url';

const filename = fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);
const app = express();

const PORT = 3000;

app.use(express.static(path.join(dirname, '../client/build')));

app.get('/api', (req, res) => {
    res.json({ message: 'Hello from the server!' });
});

app.get('*', (req, res) => {
    res.sendFile(path.join(dirname+'../client/build/index.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}/`);
});
