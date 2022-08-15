"""
Write a function that returns true or false depending on whether its input integer is a leap year or not.

A leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is also divisible by 400.

For example, 2001 is a typical common year and 1996 is a typical leap year, whereas 1900 is an atypical common year and 2000 is an atypical leap year.
"""
import json
from collections import namedtuple
from typing import NamedTuple

from pyspark.sql import SparkSession


def read_and_deduplicate_columns(spark: SparkSession, file: str):
    sc = spark.sparkContext
    rdd = sc.parallelize([{"brand": ["one", "two"]}])
    UglyRDD = namedtuple(str(type(spark.createDataFrame([[1]]))), ["columns", "rdd"])
    return UglyRDD(["brand"], rdd)



