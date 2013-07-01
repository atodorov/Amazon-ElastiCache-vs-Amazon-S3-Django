#!/usr/bin/env python

import timeit

s3_set = timeit.Timer(
"""
for i in range(1000):
    my_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('default')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

pymc_set = timeit.Timer(
"""
for i in range(1000):
    my_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('python-memcached')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

libmc_set = timeit.Timer(
"""
for i in range(1000):
    my_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('pylibmc')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

libmc_large_set = timeit.Timer(
"""
for i in range(1000):
    my_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('pylibmc-large')

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
    MyObject = my_cache.get(i)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('default')
"""
)

pymc_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = my_cache.get(i)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('python-memcached')
"""
)

libmc_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = my_cache.get(i)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('pylibmc')
"""
)

libmc_large_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = my_cache.get(i)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('pylibmc-large')
"""
)
