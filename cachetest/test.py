#!/usr/bin/env python

import timeit
from django.core import cache

s3_cache = cache.get_cache('default')
elasticache_small = cache.get_cache('ElastiCacheSmall')
elasticache_large = cache.get_cache('ElastiCacheLarge')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}

t = timeit.Timer(
"""
for i in range(1000):
    s3_cache.set(1, MyObject)
"""
)

