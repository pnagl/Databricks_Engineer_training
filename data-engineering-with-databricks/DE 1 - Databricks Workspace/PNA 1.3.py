# Databricks notebook source
name = "John"
print(f"Hello {name}")
full_name = f"{name} Doe"
print(f"Welcome back {full_name}")

# COMMAND ----------

full_name = f"{name} Doe ssss"
print(full_name)
print(f"{full_name} sda")
print(f"asda {full_name}")

# COMMAND ----------

#my_name = "asda"
#v pamati sa drzi vsetko co sa uz vykonalo, az do resetu servera - predpokladam
assert my_name is not None, "Name is still None"
print(my_name)

# COMMAND ----------

# MAGIC %run ./ExampleSetupFolder/example-setup

# COMMAND ----------

files = dbutils.fs.ls(f"{DA.paths.datasets}/nyctaxi-with-zipcodes/data")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`${DA.paths.datasets}/nyctaxi-with-zipcodes/data`

# COMMAND ----------

files = dbutils.fs.ls(f"{DA.paths.datasets}/nyctaxi-with-zipcodes/data")
display(files)

# COMMAND ----------

print(my_name)
