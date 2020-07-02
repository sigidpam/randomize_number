2. Imagine a server with the following specs:

- 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
- 64GB of ram
- 2 tb HDD disk space
- 2 x 10Gbit/s nics
 
The server is used for SSL offloading and proxies around 25000 requests per second.


Please let us know which metrics are interesting to monitor in that specific case and how would you do that?  What are the challenges of monitoring this?

What to Monitor
1. HTTP/HTTPS Load
   we can use Apache Bench to test, since it's stable for testing from endpoint, and also provides beautiful summary.
   - Latency
   - Time per request
   - Number of failed request
   - Request per second
   
2. Since the server is close to be a HAProxy, so we could monitor the performance using Ganglia. 
   It can monitor some important events from our server;
   - memory: the amount of RAM being used by the system
   - network: the network bandwith consumption because of the packets being sent over the wire.
   - TCP established: This tells us the total number of tcp connections established on the system, usually the sum of both inbound and outbond connections.
   - packet sent and received: we can see the total number of tcp packets being sent and received by our HAProxy machine
   - bytes sent and received: shows us the total data that we sent and received by the machine.
   
