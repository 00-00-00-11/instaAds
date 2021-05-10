const sqlite3 = require('sqlite3')
const { open } = require('sqlite')
const { IgApiClient } = require('instagram-private-api');
const { sample } = 'lodash';
const ig = new IgApiClient();

const message = 'https://instagram.com/nightfuryofficials';
const username = 'the_realxlana';
const password = 'Siktir4961';
let users
let limit = 32
let offset = 0

// send
open({
  filename: '../Data.db',
  driver: sqlite3.Database
}).then(async db => {
    // login
    await ig.state.generateDevice(username);
    await ig.account.login(username, password);

    // send
    while (true) {
        users = await db.all(`SELECT * FROM Users WHERE send = 0 LIMIT ${limit} OFFSET ${offset}`)
        if (!users.length) break

        await ig.entity.directThread(users.map(user => user.uID)).broadcastText(message)

        await db.exec(`UPDATE Users SET send = ${1} LIMIT ${limit} OFFSET ${offset}`)

        offset += limit
    }
})

