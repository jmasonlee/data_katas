#Foo needs to read the dataframe and contain a single column, "brand" that contains both Brand
# and brand values from the original json
from main import read_and_deduplicate_columns


def test_foo(spark):
    assert read_and_deduplicate_columns(spark, "test_1.json").columns == ["brand"]

def test_foo2(spark):
    assert read_and_deduplicate_columns(spark, "test_1.json").rdd.take(1)[0]["brand"] == ["one", "two"]

def test_fo03(spark):
    assert type(read_and_deduplicate_columns(spark, "test_1.json")) == type(spark.createDataFrame([[1]]))

