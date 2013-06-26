#!/usr/bin/env python

import timeit

s3_set = timeit.Timer(
"""
for i in range(1000):
    s3_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

s3_cache = cache.get_cache('default')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

ecs_set = timeit.Timer(
"""
for i in range(1000):
    elasticache_small.set(i, MyObject)
"""
,
"""
from django.core import cache

elasticache_small = cache.get_cache('ElastiCacheSmall')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

ecl_set = timeit.Timer(
"""
for i in range(1000):
    elasticache_large.set(i, MyObject)
"""
,
"""
from django.core import cache

elasticache_large = cache.get_cache('ElastiCacheLarge')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

s3_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = s3_cache.get(i)
"""
,
"""
from django.core import cache

s3_cache = cache.get_cache('default')
"""
)

ecs_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = elasticache_small.get(i)
"""
,
"""
from django.core import cache

elasticache_small = cache.get_cache('ElastiCacheSmall')
"""
)

ecl_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = elasticache_large.get(i)
"""
,
"""
from django.core import cache

elasticache_large = cache.get_cache('ElastiCacheLarge')
"""
)
