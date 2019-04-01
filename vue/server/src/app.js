const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')

const app = express()
app.use(morgan('combine'))
app.use(bodyParser.json())
app.use(cors())

// get, put, post, patch, delete
app.get('/status', (req, res) => {
    res.send({
        message: 'Hello World'
    })
})

app.post('/register', (req, res) => {
    res.send({
        message: `Your user was registered! Hello ${req.body.email}!`
    })
})

app.listen(process.env.PORT || 8081)
