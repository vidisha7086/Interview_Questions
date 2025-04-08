<h2>𝐒𝐐𝐋 𝐐𝐮𝐞𝐫𝐲 𝐎𝐩𝐭𝐢𝐦𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐓𝐞𝐜𝐡𝐧𝐢𝐪𝐮𝐞𝐬</h2>
<p><em>Query optimization involves rewriting SQL queries to run faster, use fewer resources, and provide improved scalability:</em></p>

<ol>
  <li><strong>Query execution plan</strong></li>

  <li><strong>Avoid <code>SELECT *</code></strong>
    <ul>
      <li>Using <code>*</code> will waste resources, so try to use only required column names.</li>
      <li>Specifying column names improves memory usage and performance.</li>
    </ul>
  </li>

  <li><strong>Proper usage of indexes</strong>
    <ul>
      <li>Use indexes for frequently searched or filtered columns.</li>
      <li>Avoid overusing indexes, as they can slow down write operations.</li>
      <li>Example:
        <pre><code>CREATE INDEX idx_customer_name ON Customers(customerName);
SELECT * FROM Customers WHERE customerName = 'John';</code></pre>
      </li>
    </ul>
  </li>

  <li><strong>Use <code>WHERE</code> instead of <code>HAVING</code></strong></li>
</ol>
