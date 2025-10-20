from pyspark.sql import SparkSession

# Create Spark session with PostgreSQL JDBC driver
# The driver is downloaded automatically via spark.jars.packages
spark = SparkSession.builder \
    .appName("PostgresSparkIntegration") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.4") \  # Latest PostgreSQL JDBC driver as of 2025
    .master("local[*]") \  # Standalone mode using all local cores
    .getOrCreate()

# JDBC connection properties
jdbc_url = "jdbc:postgresql://db:5432/mydatabase"  # 'db' is the Docker service name
connection_properties = {
    "user": "admin",  # Your Postgres username
    "password": "examplepassword",  # Your Postgres password
    "driver": "org.postgresql.Driver"
}

# Read data from a Postgres table (replace 'users' with your table name)
df = spark.read.jdbc(url=jdbc_url, table="users", properties=connection_properties)

# Show the raw data
df.show()

# Perform a sample transformation (e.g., filter and select columns)
transformed_df = df.filter(df["id"] > 0).select("id", "username")  # Example: Filter IDs > 0 and select columns

# Show the transformed data
transformed_df.show()

# Optional: Write transformed data back to Postgres (to a new table)
transformed_df.write.jdbc(url=jdbc_url, table="transformed_users", mode="overwrite", properties=connection_properties)

# Stop the Spark session when done
spark.stop()