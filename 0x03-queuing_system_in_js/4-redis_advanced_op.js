import pkg from 'redis';
const { createClient, print } = pkg;

// Enable legacyMode for callback support
const client = createClient({ legacyMode: true });

async function main() {
  await client.connect();
  console.log('Redis client connected to the server');

  // First, delete the existing ALX key if it exists
  client.del('ALX', (err, reply) => {
    if (err) {
      console.error('Error deleting key:', err);
    } else {
      console.log('Deleted existing ALX key');

      // Create Hash using hset with callbacks and redis.print
      client.hset('ALX', 'Portland', '50', print);
      client.hset('ALX', 'Seattle', '80', print);
      client.hset('ALX', 'New York', '20', print);
      client.hset('ALX', 'Bogota', '20', print);
      client.hset('ALX', 'Cali', '40', print);
      client.hset('ALX', 'Paris', '2', print);

      // Display Hash using hgetall
      client.hgetall('ALX', (err, reply) => {
        if (err) {
          console.error('Error getting hash:', err);
        } else {
          console.log(reply);
        }
      });
    }
  });
}

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

main();
