# 0x03-queuing_system_in_js

This project demonstrates the use of Redis and Kue for building queuing systems, job processing, and pub/sub messaging in Node.js.

## Table of Contents

- [Setup](#setup)
- [Scripts Overview](#scripts-overview)
- [Pub/Sub Examples](#pubsub-examples)
- [Job Queue Examples (Kue)](#job-queue-examples-kue)
- [Testing](#testing)
- [Notes](#notes)

---

## Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Ensure Redis is running** on your system (default port 6379).

3. **Run scripts** using:
   ```bash
   npm run dev <script.js>
   ```

---

## Scripts Overview

### Redis Basics

- **0-redis_client.js**  
  Connects to Redis and logs connection status.

- **1-redis_op.js**  
  Demonstrates basic Redis SET/GET operations.

- **2-redis_op_async.js**  
  Async/await version of basic Redis operations.

- **4-redis_advanced_op.js**  
  Demonstrates Redis hash operations (HSET/HGETALL) using callbacks.

### Pub/Sub Examples

- **5-publisher.js**  
  Publishes messages to the `ALXchannel` channel.

- **5-subscriber.js**  
  Subscribes to `ALXchannel`, logs messages, and exits on `KILL_SERVER`.

### Job Queue Examples (Kue)

- **6-job_creator.js**  
  Creates a single notification job in the `push_notification_code` queue and logs job events.

- **7-job_creator.js**  
  Creates multiple notification jobs in the `push_notification_code_2` queue and logs job events.

- **7-job_processor.js**  
  Processes jobs from the `push_notification_code_2` queue, simulates sending notifications, and handles blacklisted numbers.

- **8-job.js**  
  Exports a function to create push notification jobs in bulk.

- **8-job.test.js**  
  Mocha/Chai tests for job creation logic.

- **9-stock.js**  
  Example of using Redis to track stock/reservations for products.

- **100-seat.js**  
  Advanced example (details in file) for seat reservation logic.

---

## Pub/Sub Usage

1. **Start the subscriber:**
   ```bash
   npm run dev 5-subscriber.js
   ```
2. **Start the publisher (in another terminal):**
   ```bash
   npm run dev 5-publisher.js
   ```
3. **You should see messages appear in the subscriber terminal.**
   - When `KILL_SERVER` is published, the subscriber will exit.

---

## Job Queue Usage

1. **Create a job:**
   ```bash
   npm run dev 6-job_creator.js
   ```
   - Logs job creation and completion/failure.

2. **Create multiple jobs:**
   ```bash
   npm run dev 7-job_creator.js
   ```

3. **Process jobs:**
   ```bash
   npm run dev 7-job_processor.js
   ```

4. **Test job logic:**
   ```bash
   npm test
   ```

---

## Notes

- **Kue** is used for job queueing. Jobs are stored in Redis and can be monitored via the Kue web UI (see Kue docs for details).
- **Redis** is used for both simple key-value storage and pub/sub messaging.
- **All scripts assume Redis is running locally.**
- **For more details, see comments in each script.**

---

## Author

- Project for ALX Backend specialization
