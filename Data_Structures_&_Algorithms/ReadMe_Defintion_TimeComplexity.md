<h2>Please help me out with several examples from easy to tough to calculate big O or complexity of the data structure. </h2>

Here are several examples, ranging from easy to tough, to help you calculate the Big O complexity of different data structures and algorithms.

<h2>Big O Complexity of Data Structures & Algorithms</h2>

<h3>1. Constant Time - O(1)</h3>
<p><strong>Example:</strong> Accessing an element in an array by index</p>
<pre>
<code>
arr = [10, 20, 30, 40]
print(arr[2])  # O(1)
</code>
</pre>
<p><strong>Explanation:</strong> No matter how big the array is, accessing an index takes <strong>constant time</strong>.</p>

<h3>2. Linear Time - O(n)</h3>
<p><strong>Example:</strong> Traversing an array</p>
<pre>
<code>
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num)  # O(n)
</code>
</pre>
<p><strong>Explanation:</strong> The loop runs <strong>n</strong> times, so the complexity is <strong>O(n)</strong>.</p>

<h3>3. Logarithmic Time - O(log n)</h3>
<p><strong>Example:</strong> Binary Search</p>
<pre>
<code>
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
</code>
</pre>
<p><strong>Explanation:</strong> The search space is <strong>halved</strong> in each iteration, leading to <strong>O(log n)</strong> complexity.</p>

<h3>4. Quadratic Time - O(n²)</h3>
<p><strong>Example:</strong> Nested Loop (Bubble Sort)</p>
<pre>
<code>
arr = [64, 25, 12, 22, 11]
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
</code>
</pre>
<p><strong>Explanation:</strong> The nested loops make the complexity <strong>O(n²)</strong>.</p>

<h3>5. Factorial Time - O(n!)</h3>
<p><strong>Example:</strong> Generating All Permutations</p>
<pre>
<code>
from itertools import permutations

arr = [1, 2, 3]
all_perms = list(permutations(arr))  # O(n!)
</code>
</pre>
<p><strong>Explanation:</strong> The number of permutations grows <strong>factorially</strong>, so the complexity is <strong>O(n!)</strong>.</p>

<h3>6. Exponential Time - O(2ⁿ)</h3>
<p><strong>Example:</strong> Recursive Fibonacci</p>
<pre>
<code>
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(2^n)
</code>
</pre>
<p><strong>Explanation:</strong> Each function call spawns <strong>two more calls</strong>, leading to <strong>O(2ⁿ)</strong> growth.</p>

<h3>7. Best & Worst Cases</h3>
<table>
    <tr>
        <th>Algorithm</th>
        <th>Best Case</th>
        <th>Worst Case</th>
    </tr>
    <tr>
        <td>Linear Search</td>
        <td>O(1)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Binary Search</td>
        <td>O(1)</td>
        <td>O(log n)</td>
    </tr>
    <tr>
        <td>QuickSort</td>
        <td>O(n log n)</td>
        <td>O(n²)</td>
    </tr>
    <tr>
        <td>MergeSort</td>
        <td>O(n log n)</td>
        <td>O(n log n)</td>
    </tr>
</table>

<p>Would you like me to add more examples or cover specific cases? 😊🚀</p>
