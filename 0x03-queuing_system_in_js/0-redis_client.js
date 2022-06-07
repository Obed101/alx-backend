// import { createClient } from 'redis';
async function reddis() {
    createClient = require('redis')
    createClient = createClient.createClient;
    const client = createClient();
    client.on('error', () => console.log('An error occured'));
    await client.connect();
    await client.set('name', 'Obed Amoako');
    console.log(await client.get('name'));
}
reddis()
