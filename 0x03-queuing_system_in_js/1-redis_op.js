import pkg from 'redis';
const { createClient, print } = pkg;

const client = createClient();

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  
  // Execute operations after connection is established
  try {
    await displaySchoolValue('ALX');
    await setNewSchool('ALXSanFrancisco', '100');
    await displaySchoolValue('ALXSanFrancisco');
  } catch (error) {
    console.error('Error during operations:', error);
  }
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to Redis
client.connect().catch((err) => {
  console.error('Failed to connect to Redis:', err);
});

/**
 * Set a new school value in Redis
 */
async function setNewSchool(schoolName, value) {
  try {
    const reply = await client.set(schoolName, value);
    console.log(`Reply: ${reply}`);
    return reply;
  } catch (err) {
    console.error(`Error setting school ${schoolName}:`, err);
    throw err;
  }
}

/**
 * Display the value for a school key from Redis
 */
async function displaySchoolValue(schoolName) {
  try {
    const reply = await client.get(schoolName);
    console.log(reply);
    return reply;
  } catch (err) {
    console.error(`Error getting school ${schoolName}:`, err);
    throw err;
  }
}
