import { createClient } from 'redis';
async function _reddis () {
  const client = createClient();
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  await client.connect();
  client.on('connect', () => console.log('Redis client connected to the server'));
}
_reddis();

function publishMessage (message, time) {
  if (time) {
    console.log(`About to send ${message}`);
  }
}
