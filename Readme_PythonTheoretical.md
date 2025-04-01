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


<ul>
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
