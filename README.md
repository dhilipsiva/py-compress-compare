# py-compress-compare

Compression algorithm comparisions for python libraries

This test took ~1MB sample_data.json and did this:

1. 1000 compress calls with write to redis
2. 10000 decompress calls after reading from redis
3. The time is in seconds 

```json
{
    "zlib": {
        "compression_ratio": 27.836415022034874,
        "total_compress_time": [
            7.408879518508911
        ],
        "total_decompress_time": [
            12.890191793441772
        ]
    },
    "lz4": {
        "compression_ratio": 18.226421603989586,
        "total_compress_time": [
            0.1690382957458496
        ],
        "total_decompress_time": [
            0.8626720905303955
        ]
    },
    "brotli": {
        "compression_ratio": 64.77683647307992,
        "total_compress_time": [
            206.5796468257904
        ],
        "total_decompress_time": [
            1.4284749031066895
        ]
    },
    "zstandard": {
        "compression_ratio": 43.421729059254275,
        "total_compress_time": [
            0.19399118423461914
        ],
        "total_decompress_time": [
            0.7609338760375977
        ]
    }
}
```
