import pkg from 'redis';
const { createClient } = pkg;

const subscriber = createClient();

subscriber.on('connect', async () => {
  console.log('Redis client connected to the server');
  
  try {
    // Subscribe to the ALXchannel using the modern API
    await subscriber.subscribe('ALXchannel', (message) => {
      console.log(message);
      
      // If the message is KILL_SERVER, unsubscribe and quit
      if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('ALXchannel');
        subscriber.quit();
      }
    });
  } catch (err) {
    console.error('Error subscribing:', err);
  }
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to Redis
subscriber.connect();
