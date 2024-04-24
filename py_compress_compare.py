import json
import redis
import time
import zlib
import lz4.frame
import brotli
import zstandard as zstd
import numpy as np

# Read JSON file
with open('sample_data.json', 'r') as file:
    data = json.dumps(json.load(file))
data_bytes = data.encode('utf-8')

# Initialize Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Define compression libraries
compressors = {
    'zlib': (zlib.compress, zlib.decompress),
    'lz4': (lz4.frame.compress, lz4.frame.decompress),
    'brotli': (brotli.compress, brotli.decompress),
    'zstandard': (zstd.ZstdCompressor().compress, zstd.ZstdDecompressor().decompress)
}

# Define metrics dictionary
metrics = {key: {'compression_ratio': [], 'total_compress_time': [], 'total_decompress_time': []} for key in compressors}

# Benchmarking
num_compress = 1000
num_decompress = 10000

for name, (comp_func, decomp_func) in compressors.items():
    print(f"Testing {name}...")
    # Compression
    start_time = time.time()
    for _ in range(num_compress):
        compressed_data = comp_func(data_bytes)
        r.set('compressed_data', compressed_data)
    total_compress_time = time.time() - start_time
    compression_ratio = len(data_bytes) / len(compressed_data)
    
    # Decompression
    start_time = time.time()
    for _ in range(num_decompress):
        retrieved_data = r.get('compressed_data')
        decompressed_data = decomp_func(retrieved_data)
    total_decompress_time = time.time() - start_time
    
    # Record results
    metrics[name]['compression_ratio'].append(compression_ratio)
    metrics[name]['total_compress_time'].append(total_compress_time)
    metrics[name]['total_decompress_time'].append(total_decompress_time)

# Calculate average compression ratio
for comp in metrics:
    metrics[comp]['compression_ratio'] = np.mean(metrics[comp]['compression_ratio'])

# Output results
print(json.dumps(metrics, indent=4))

# Save results to JSON file
with open('compression_results.json', 'w') as outfile:
    json.dump(metrics, outfile, indent=4)
