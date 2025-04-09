<h2>𝐒𝐐𝐋 𝐐𝐮𝐞𝐫𝐲 𝐎𝐩𝐭𝐢𝐦𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐓𝐞𝐜𝐡𝐧𝐢𝐪𝐮𝐞𝐬</h2>
<p><em>(Query optimization involves rewriting the SQL queries to run faster, use fewer resources, and provide improved scalability)</em></p>

<p>🔗 <strong>URL</strong>: <a href="https://www.linkedin.com/feed/update/urn:li:activity:7303652480750432256/" target="_blank">LinkedIn Post</a></p>

<ol>
  <li>
    <strong>Analyze query performance</strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Execution plan shows how the database executes your query<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Identify slow parts of query<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Adjust indexing, joins and filter based on insights<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<code>EXPLAIN SELECT * FROM CUSTOMER WHERE CONDITION;</code>
  </li>

  <li>
    <strong>Avoid <code>SELECT *</code></strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Using * will waste the resources, so try to use required column names<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Using specific columns avoids unnecessary resource usage and improves memory
  </li>

  <li>
    <strong>Proper usage of indexes</strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Use indexes for frequently searched or filtered columns<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Avoid overuse of indexes, as it can slow down write operations<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<code>CREATE INDEX idx_customer_name ON Customers(customerName);</code><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<code>SELECT * FROM customer WHERE customerName = 'John';</code>
  </li>

  <li>
    <strong>Use <code>WHERE</code> instead of <code>HAVING</code></strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• WHERE filters rows <em>before</em> aggregation<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• HAVING filters <em>after</em> aggregation<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Filtering early improves performance and reduces dataset size
  </li>

  <li>
    <strong>Leverage joins effectively</strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Use INNER JOIN for specific matching rows<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Avoid CROSS JOIN (unless needed)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Always use <code>ON</code> condition to avoid Cartesian product<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Index join columns for faster lookup
  </li>

  <li>
    <strong>Avoid subqueries when possible</strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Use JOINs for better performance instead of nested subqueries
  </li>

  <li>
    <strong>Limit results with pagination</strong><br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Querying millions of records at once is resource intensive<br>
    &nbsp;&nbsp;&nbsp;&nbsp;• Use <code>LIMIT</code> and <code>OFFSET</code> for pagination<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<code>SELECT * FROM table_name LIMIT 10 OFFSET 20;</code>
  </li>
</ol>


<li>
  star and snowflake schem --------------
  list comprehension ----
  python namespaces-------
  pandas and numpy---------
  joins ---------
  query for removing duplicates and second highest salry in each deparment
  defaultt values fucntion ---------------
  olap and oltp---------------------
  steps of data modelling------------------
  scd --------------------------------------
  normalization----------------------------
  denormalization-------------------------------
  optmization rechniques-----------------
  partioning and bucketing----------------
  pushdown optimization ---------------------
  junk dimensionality -----------------
  differnec between distinct and groupby-----------
  differnce between where and having ----------
  use of apply()
  conactenate column values
  pyspark tunning
  pyspark optimization
  quartely sum of price using sql and python
  list of pandas fucntion for data manipulation
  api development
  jason functions
  what exactly is parquet format 
  how we convert all files in parquet format 
  how we can merge two columns data of two different tables
  
</li>
