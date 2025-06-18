import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Create the job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test notification'
};

// Create the job in the queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
