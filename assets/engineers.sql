/* @bruin

name: gsheet.engineers
type: duckdb.sql

materialization:
    type: table
    strategy: create+replace

depends:
    - gsheet.customers

@bruin */

SELECT * FROM gsheet.customers
WHERE position LIKE '%Engineer'