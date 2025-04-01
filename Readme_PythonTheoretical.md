<h3> Question 1: What are Python decorators and how would you use them? </h3>


## Understanding "Extend Past Python"

<p>
The phrase <i>"extend past Python"</i> suggests that the concept of decorators is not exclusive to Python but exists in other programming languages as well. It implies that similar functionality—where functions take other functions as arguments and return modified functions—can be found in other paradigms, such as:
</p>

<ul>
  <li><b>Higher-order functions</b> in functional programming languages (e.g., Haskell, JavaScript with <code>map</code>, <code>filter</code>, and <code>reduce</code>).</li>
  <li><b>Aspect-Oriented Programming (AOP)</b>, which allows modifying function behavior dynamically (e.g., Java’s annotations with Spring AOP).</li>
  <li><b>Function wrappers</b> in JavaScript, such as middleware functions in Express.js.</li>
</ul>

<p>
However, the specific syntax of decorators using <code>@decorator_name</code> is Python-specific, whereas the general idea of functions modifying other functions (or classes) exists in multiple languages.
</p>


<h3> Question 2: What is PEP8 and do you follow its guidelines when you're coding? </h3>
<p> A coding standard, and I try to. pylint is a great help.</p> Pylint is an open-source tool designed to help developers check code and its quality, detect programming errors in the Python language and offer simple refactoring suggestions.

<h3> Question 3: How are arguments passed – by reference of by value? </h3> (easy, but not that easy, I'm not sure if I can answer this clearly)
<p> </p>

<h3> Question 4:Do you know what list and dict comprehensions are? Can you give an example? </h3>
<p> Ways to construct a list or dict through an expression and an iterable  </p>

<h3> Question 5: How to read a 8GB file ? </h3>
Operate on chunks, and not one byte at a time. Be wary about the RAM of the host machine. What is the nature of the data such that it is so large? How are you operating on it? What are you returning? Are you accessing it sequentially or randomly? There's a lot more to ask than to answer here. 

<h3> Question 6: What don't you like about Python? </h3>
It's **slow**, and it can be **too dynamic** for certain tasks in my opinion. **It is not compiled**. It can be very unpredictable. People** abuse the flexibility** of it sometimes.

<h3> Question 7: Do you use tabs or spaces, which ones are better? </h3>
Spaces. Stick to PEP8 when possible.

<h3> Question 8: How are arguments passed – by reference of by value? </h3>
The terms PBR and PBV were developed to talk about languages like Fortran and C and using them to talk about Python is only a source of confusion. Python's passing semantics are different from either of these languages.
The literal answer is that Python is pass-by-value in all cases, and also in all cases the value is an object reference. In a PBR language you can rebind the name in the passing scope, but in Python you can only mutate an object you receive. This is analogous to passing pointers in C, while C remains a PBV-only language.
<h4> Another Answer </h4>
PBV and PBR were designed to talk about all programming languages.
Pass by value: the argument expression is evaluated, and the value it results in is assigned to the formal parameter.
Pass by reference: the argument expression is evaluated, and a reference to the result is assigned to the formal parameter.
People get confused and think that PBV == copying, because in C, assignment of a value copies the value.


<h3> Question 9: Differences Between Python 2.x and Python 3.x</h3>  
<ul>
        <li>
            <strong>Print Statement vs Print Function:</strong>
            <p><strong>Python 2.x:</strong> <code>print "Hello, world!"</code> (No parentheses required.)</p>
            <p><strong>Python 3.x:</strong> <code>print("Hello, world!")</code> (Parentheses required.)</p>
        </li>        
        <li>
            <strong>Integer Division:</strong>
            <p><strong>Python 2.x:</strong> Division of integers results in integer output. 
                For example, <code>3 / 2</code> returns <strong>1</strong>.</p>
            <p><strong>Python 3.x:</strong> Division of integers returns a float. 
                For example, <code>3 / 2</code> returns <strong>1.5</strong>.</p>
        </li>
        <li>
            <strong>Unicode Support:</strong>
            <p><strong>Python 2.x:</strong> Strings are ASCII by default. You need to specify Unicode with a <code>u</code> prefix. 
                Example: <code>u"Hello"</code> for Unicode string.</p>
            <p><strong>Python 3.x:</strong> All strings are Unicode by default. No need to prefix with <code>u</code>.</p>
        </li>
        <li>
            <strong>Iterators:</strong>
            <p><strong>Python 2.x:</strong> Functions like <code>range()</code> and <code>zip()</code> return lists.</p>
            <p><strong>Python 3.x:</strong> Functions like <code>range()</code> and <code>zip()</code> return iterators instead of lists.</p>
        </li>
        <li>
            <strong>Input Function:</strong>
            <p><strong>Python 2.x:</strong> <code>input()</code> evaluates the input as a Python expression, and <code>raw_input()</code> reads input as a string.</p>
            <p><strong>Python 3.x:</strong> <code>input()</code> always returns the input as a string. There is no <code>raw_input()</code>.</p>
        </li>
    </ul>
<ul>
Key Differences:
- Print Statement vs Function: In Python 2.x, print is a statement, but in Python 3.x, it's a function that requires parentheses.
- Integer Division: Python 2.x performs integer division by default when dividing two integers, while Python 3.x performs float division.
- Unicode Support: Python 3.x has better support for Unicode by default, unlike Python 2.x, where you need to explicitly define strings as Unicode.
- Iterators: Functions like range() and zip() return iterators in Python 3.x, whereas they return lists in Python 2.x.
- Input Function: In Python 2.x, input() evaluates the input as code, while raw_input() returns input as a string. Python 3.x only has input(), which always returns a string.
  
<h4> More Questions </h4>
    <li><strong>Generators / yield keyword:</strong> In Python, generators are special functions that use the <code>yield</code> keyword to return values lazily, meaning they produce items one at a time rather than storing everything in memory.</li>
    <li><strong>Multiple inheritance:</strong> Python supports multiple inheritance, allowing a class to inherit attributes and methods from more than one parent class. However, it can lead to complexity, especially with the "diamond problem," which Python resolves using the C3 linearization (method resolution order, MRO).</li>
    <li><strong>Is Python compiled, interpreted, and/or emulated?</strong> Python is primarily an interpreted language, meaning its code is executed line by line. However, it is first compiled to bytecode (.pyc files) before being interpreted by the Python Virtual Machine (PVM).</li>
    <li><strong>What differentiates Python from Ruby?</strong> While both are high-level, dynamically typed languages, Python emphasizes readability and explicitness (using indentation for structure), whereas Ruby is more flexible and designed for developer happiness, often allowing multiple ways to achieve the same task.</li> Knit hats and smugness?
    <li><strong>Debugging Python: What is <code>pdb</code> and how do you use it?</strong> Python's built-in debugger (<code>pdb</code>) allows step-by-step execution, inspecting variables, and setting breakpoints. You can start debugging by adding <code>import pdb; pdb.set_trace()</code> in your script or using the command-line tool <code>python -m pdb script.py</code>.</li>
    <li><strong>Modifying global variables in a function & why to avoid it:</strong> You can modify a global variable inside a function using the <code>global</code> keyword. However, this is generally discouraged as it makes code harder to understand and debug by introducing side effects.</li>
    <li><strong>Use of the <code>re</code> module:</strong> The <code>re</code> module in Python provides support for regular expressions. Example:
        <pre>
import re
pattern = r'\d+'
result = re.findall(pattern, 'Order 123 was shipped on 2024-04-01')
print(result)  # Output: ['123', '2024', '04', '01']
        </pre>
    </li>
</ul>
