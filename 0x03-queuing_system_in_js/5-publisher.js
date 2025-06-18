import pkg from 'redis';
const { createClient } = pkg;

const publisher = createClient();

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

async function publishMessage(message, time) {
  try {
    setTimeout(async () => {
      console.log('About to send MESSAGE');
      await publisher.publish('ALXchannel', message);
      console.log(`Message sent: ${message}`);
    }, time);
  } catch (err) {
    console.error('Error publishing message:', err);
  }
}

// Example usage
publisher.connect().then(() => {
  // Publish some test messages
  publishMessage("ALX Student #1 starts course", 100);
  publishMessage("ALX Student #2 starts course", 200);
  publishMessage("KILL_SERVER", 300);
  publishMessage("ALX Student #3 starts course", 400);
});

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('Shutting down publisher...');
  publisher.quit();
  process.exit(0);
});
