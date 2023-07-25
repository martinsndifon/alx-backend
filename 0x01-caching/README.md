## Caching
Caching is a technique used in computer science and software engineering to store frequently accessed or expensive-to-compute data in a fast and accessible location. The purpose of caching is to improve the performance and efficiency of applications by reducing the need to repeatedly fetch or compute data from the original source.

The basic idea behind caching is to temporarily store data in a cache (a high-speed memory or storage) so that subsequent requests for the same data can be served faster. Caching is commonly used to minimize the latency or processing time associated with data retrieval or computation, especially when the data or computation is time-consuming or resource-intensive.

### There are various types of caching, including:

Memory Caching: Data is cached in RAM (Random Access Memory) for quick access. Commonly used in web servers, databases, and programming languages to store frequently accessed variables, objects, or results.

Disk Caching: Data is cached on disk, usually in the form of files or temporary storage, to reduce disk read/write operations and improve file access times.

Web Caching: In the context of the internet, web caching involves storing web content (HTML, images, CSS, etc.) on local servers or proxy servers to reduce the load on the original web server and speed up content delivery to clients.

Database Caching: In database systems, caching is used to store frequently accessed data or query results in memory, reducing the need to fetch data from disk on subsequent queries.

### Cache Replacement policies
FIFO
LIFO
LRU
MRU
LFU
