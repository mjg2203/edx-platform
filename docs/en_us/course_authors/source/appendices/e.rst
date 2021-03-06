
.. _Appendix E:


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
APPENDIX E: Problem and Tool XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This appendix provides information about the XML for most problem and tool types in Studio:

* :ref:`Checkbox`
* :ref:`Chemical Equation Response`
* :ref:`Custom Response`
* :ref:`Formula Response`
* :ref:`Image Response`
* :ref:`Multiple Choice`
* :ref:`Numerical Response`
* :ref:`Option Response`
* :ref:`Schematic Response`
* :ref:`String Response`

.. _Checkbox:

Choice Response (Checkbox)
---------------------------

Sample Problem:

.. image:: ../Images/CheckboxExample.gif
 :alt: Image of a checkbox problem


**Sample Problem XML**

.. code-block:: xml

  <problem>
  <startouttext/>
    <p>Learning about the benefits of preventative healthcare can be particularly difficult. Check all of the reasons below why this may be the case.</p>

  <choiceresponse>
  <checkboxgroup>
  <choice correct="true"><text>A large amount of time passes between undertaking a preventative measure and seeing the result.</text></choice>
  <choice correct="false"><text>Non-immunized people will always fall sick.</text></choice>
  <choice correct="true"><text>If others are immunized, fewer people will fall sick regardless of a particular individual's choice to get immunized or not.</text></choice>
  <choice correct="true"><text>Trust in healthcare professionals and government officials is fragile.</text></choice>
  </checkboxgroup>

   <solution>
   <div class="detailed-solution">
   <p>Explanation</p>
   <p>People who are not immunized against a disease may still not fall sick from the disease. If someone is trying to learn whether or not preventative measures against the disease have any impact, he or she may see these people and conclude, since they have remained healthy despite not being immunized, that immunizations have no effect. Consequently, he or she would tend to believe that immunization  (or other preventative measures) have fewer benefits than they actually do.</p>
   </div>
   </solution>
  </choiceresponse>
  </problem>


**Template**

.. code-block:: xml

  <problem>
  <startouttext/>
    <p>Question text</p>

  <choiceresponse>

  <checkboxgroup>
  <choice correct="false"><text>Answer option 1 (incorrect)</text></choice>
  <choice correct="true"><text>Answer option 2 (correct)</text></choice>
  </checkboxgroup>

   <solution>
   <div class="detailed-solution">
   <p>Explanation</p>
   <p>Explanation text</p>
   </div>
   </solution>

  </choiceresponse>
  </problem>



.. _Chemical Equation Response:

Chemical Equation Response
--------------------------

The chemical equation problem type allows the student to enter chemical equations. The grader evaluates student responses by using a Python script that you create and embed in the problem.

**Sample Problem**

.. image:: ../Images/ChemicalEquationExample.png
 :alt: Image of a chemical equation response problem

**Sample Problem XML**:

.. code-block:: xml

  <problem>
    <startouttext/>
    <p>Some problems may ask for a particular chemical equation. Practice by writing out the following reaction in the box below.</p>
    
  \( \text{H}_2\text{SO}_4 \longrightarrow \text { H}^+ + \text{ HSO}_4^-\)

    <customresponse>
      <chemicalequationinput size="50"/>
      <answer type="loncapa/python">

  if chemcalc.chemical_equations_equal(submission[0], 'H2SO4 -> H^+ + HSO4^-'):
      correct = ['correct']
  else:
      correct = ['incorrect']

      </answer>
    </customresponse>
    <p>Some tips:</p>
    <ul>
    <li>Use real element symbols.</li>
    <li>Create subscripts by using plain text.</li>
    <li>Create superscripts by using a caret (^).</li>
    <li>Create the reaction arrow (\(\longrightarrow\)) by using "->".</li>
    </ul>

    <endouttext/>
  
   <solution>
   <div class="detailed-solution">
   <p>Solution</p>
   <p>To create this equation, enter the following:</p>
     <p>H2SO4 -> H^+ + HSO4^-</p>
   </div>
   </solution>
  </problem>


.. _Custom Response:

Custom Response ("Write-Your-Own-Grader")
------------------------------------------

In write-your-own-grader problems (also called “custom Python-evaluated input” problems), the grader evaluates a student’s response using a Python script that you create and embed in the problem. Students can enter more than one line of text.

**Sample Problem**

.. image:: ../Images/CustomPythonExample.png
 :alt: Image of a custom response problem


**Sample Problem XML**:

.. code-block:: xml

  <problem>
  <p>This question has two parts.</p>

  <script type="loncapa/python">

  def test_add(expect, ans):
      try:
          a1=int(ans[0])
          a2=int(ans[1])
          return (a1+a2) == int(expect)
      except ValueError:
          return False

  def test_add_to_ten(expect, ans):
      return test_add(10, ans)

  </script>

  <p>Part 1: Enter two integers that sum to 10. </p>
  <customresponse cfn="test_add_to_ten">
          <textline size="10" correct_answer="3"/><br/>
          <textline size="10" correct_answer="7"/>
  </customresponse>

  <p>Part 2: Enter two integers that sum to 20. </p>
  <customresponse cfn="test_add" expect="20">
          <textline size="10"/><br/>
          <textline size="10"/>
  </customresponse>

      <solution>
          <div class="detailed-solution">
              <p>Explanation</p>
                 <p>For part 1, any two numbers of the form <i>n</i> and <i>10-n</i>, where <i>n</i> is any integer, will work. One possible answer would be the pair 0 and 10.</p>
                <p>For part 2, any pair <i>x</i> and <i>20-x</i> will work, where <i>x</i> is any real number with a finite decimal representation. Both inputs have to be entered either in standard decimal notation or in scientific exponential notation. One possible answer would be the pair 0.5 and 19.5. Another way to write this would be 5e-1 and 1.95e1.</p>
          </div>
      </solution>
  </problem>

**Templates**

The following template includes suggested correct answers (to include these, add a ``correct_answer`` attribute to the ``<textline>`` tag).

.. code-block:: xml

  <problem>

  <script type="loncapa/python">
  def test_add(expect,ans):
    a1=float(ans[0])
    a2=float(ans[1])
    return (a1+a2)== float(expect)
  </script>


  <p>Enter two real numbers that sum to 20: </p>
  <customresponse cfn="test_add" expect="20">
          <textline size="10" correct_answer="11"/><br/>
          <textline size="10" correct_answer="9"/>
  </customresponse>

      <solution>
          <div class="detailed-solution">
          </div>
      </solution>
  </problem>

The following template does not include suggested correct answers.

.. code-block:: xml

  <problem>

  <script type="loncapa/python">
  def test_add(expect,ans):
    a1=float(ans[0])
    a2=float(ans[1])
    return (a1+a2)== float(expect)
  </script>


  <p>Enter two real numbers that sum to 20: </p>
  <customresponse cfn="test_add" expect="20">
          <textline size="10" /><br/>
          <textline size="10" />
  </customresponse>

      <solution>
          <div class="detailed-solution">
          </div>
      </solution>
  </problem>

.. _Formula Response:

Formula Response (Math Expression Input Problems)
-------------------------------------------------

**Sample Problem**

.. image:: ../Images/MathExpressionInputExample.gif
 :width: 600
 :alt: Image of a math expression input problem

**Sample Problem XML**

.. code-block:: xml

  <problem>
    <p>Some problems may ask for a mathematical expression. Practice creating mathematical expressions by answering the questions below.</p>
    <p>Notes:</p>
    <ul>
      <li>Use standard arithmetic operation symbols.</li>
      <li>Indicate multiplication explicitly by using an asterisk (*).</li>
      <li>Use a caret (^) to raise to a power.</li>
      <li>Use an underscore (_) to indicate a subscript.</li>        
      <li>Use parentheses to specify the order of operations.</li>
    </ul>

    <p>Write an expression for the product of R_1, R_2, and the inverse of R_3.</p>
    <formularesponse type="ci" samples="R_1,R_2,R_3@1,2,3:3,4,5#10" answer="$VoVi">
      <responseparam type="tolerance" default="0.00001"/>
      <formulaequationinput size="20" />
    </formularesponse>

  <script type="loncapa/python">
  VoVi = "(R_1*R_2)/R_3"
  </script>

    <p>Let <i>x</i> be a variable, and let <i>n</i> be an arbitrary constant. What is the derivative of <i>x<sup>n</sup></i>?</p>
  <script type="loncapa/python">
  derivative = "n*x^(n-1)"
  </script>
    <formularesponse type="ci" samples="x,n@1,2:3,4#10" answer="$derivative">
      <responseparam type="tolerance" default="0.00001"/>
      <formulaequationinput size="20" />
    </formularesponse>

    <solution>
      <div class="detailed-solution">
        <p>Explanation</p>

      </div>
    </solution>
  </problem>

**XML Attribute Information**

<script>


  .. image:: ../Images/formularesponse.png


<formularesponse>


  .. image:: ../Images/formularesponse3.png

Children may include ``<formulaequationinput/>``.

If you do not need to specify any samples, you should look into the use of the
Numerical Response input type, as it provides all the capabilities of Formula
Response without the need to specify any unknown variables.

<responseparam>


  .. image:: ../Images/formularesponse6.png

<formulaequationinput/>

========= ============================================= =====
Attribute                  Description                  Notes
========= ============================================= =====
size      (optional) defines the size (i.e. the width)
          of the input box displayed to students for
          typing their math expression.
========= ============================================= =====

.. _Image Response:

Image Response
--------------

The Image Response input type presents an image and accepts clicks on the image as an answer.
Images have to be uploaded to the courseware Assets directory. Response clicks are marked as correct if they are within a certain specified sub rectangle of the image canvas.

*Note The Mozilla Firefox browser is currently not supported for this problem type.*

Sample Problem:

.. image:: ../Images/image294.png
 :width: 600


**Problem Code**:

.. code-block:: xml

  <problem>
    <p><b>Example Problem</b></p>
  <startouttext/>
      <p>You are given three shapes. Click on the triangle.</p>
      <endouttext/>
      <imageresponse>
      <imageinput src="/static/threeshapes.png" width="220" height="150" rectangle="(80,40)-(130,90)" />
      </imageresponse>
  </problem>

Template

.. code-block:: xml

  <problem>
      <imageresponse>
      <imageinput src="Path_to_Image_File.png" width="220" height="150" rectangle="(80,40)-(130,90)" />
      </imageresponse>
  </problem>

XML Attribute Information


<imageresponse>

  .. image:: ../Images/imageresponse1.png

<imageinput>

  .. image:: ../Images/imageresponse2.png

.. _Multiple Choice:

Multiple Choice
---------------


The Multiple Choice input type allows the student to select at most one choice
from a collection of answer choices, presented as a list of radio buttons.

A Multiple Choice problem can have more than one correct answer, depending on
how many choices are marked as correct in the underlying XML. If all choices are
marked as incorrect, there is no correct response.

Multiple Choice is structurally similar to Option Response. Some conceptual
differences between the two include the following.

• The Multiple Choice radio button format makes it easier for students to read very long response options.

• The Option Response drop-down input format makes it more likely for students to think of an answer and then search for it, rather than relying purely on recognition to answer the question.

• The Multiple Choice format is more explicit and visual. This makes it a more appropriate choice for presenting tricky or complicated answer options which are intended to get the student to pause and think.

Sample Problem:

.. image:: ../Images/image289.png
 :width: 600
 :alt: Image of a multiple choice problem

**Problem Code:**

.. code-block:: xml

  <problem>
  <p><b>Example Problem</b></p>
  <p>How many correct responses can a Multiple Choice question have?</p>
      <multiplechoiceresponse>
     <choicegroup type="MultipleChoice">
        <choice correct="false" name="one">Only one</choice>
        <choice correct="false" name="zeroone">Only zero or one</choice>
        <choice correct="true" name="zeromore">Zero or more</choice>
        <choice correct="false" name="onemore">Only one or more</choice>
        <choice correct="false" name="noone">Nobody knows</choice>
        <choice correct="true" name="someone">Somebody might know :)</choice>
    </choicegroup>
    </multiplechoiceresponse>
  <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
            <p>It depends on how many choices are marked as correct in the underlying XML.</p>
  <p>Note that if all choices are marked as incorrect, there is no
          correct response.</p>
        </div>
    </solution>
  </problem>


**Template**

.. code-block:: xml

  <problem>

  <multiplechoiceresponse>
    <choicegroup type="MultipleChoice">
      <choice correct="false" name="a">A</choice>
      <choice correct="true" name="b">B</choice>
    </choicegroup>
  </multiplechoiceresponse>

  <solution>
    <div class="detailed-solution">

    </div>
  </solution>
  </problem>


**XML Attribute Information**


<multiplechoiceresponse>

.. image:: ../Images/multipleresponse.png


<choicegroup>

  .. image:: ../Images/multipleresponse2.png


<choice>

  .. image:: ../Images/multipleresponse3.png

.. _Numerical Response:

Numerical Response
------------------

The Numerical Response input type accepts a line of text input from the student
and evaluates the input for correctness based on its numerical value. The input
is allowed to be a number or a mathematical expression in a fixed syntax.

The answer is correct if it is within a specified numerical tolerance of the
expected answer.

The expected answer can be specified explicitly or precomputed by a Python
script.

Accepted input types include ``<formulaequationinput />`` and ``<textline />``.
However, the math display on ``<textline math="1" />`` uses a different parser
and has different capabilities than the response type--this may lead to student
confusion. For this reason, we strongly urge using ``<formulaequationinput />``
only, and the examples below show its use.

Sample Problem:

.. image:: ../Images/image292.png
 :width: 600
 :alt: Image of a numerical response problem


**Problem Code**:

.. code-block:: xml

  <problem>
    <p><b>Example Problem</b></p>

  <p>What base is the decimal numeral system in?
      <numericalresponse answer="10">
          <formulaequationinput />
      </numericalresponse>
  </p>

    <p>What is the value of the standard gravity constant <i>g</i>, measured in m/s<sup>2</sup>? Give your answer to at least two decimal places.
    <numericalresponse answer="9.80665">
      <responseparam type="tolerance" default="0.01" />
      <formulaequationinput />
    </numericalresponse>
  </p>

  <!-- Use python script spacing. The following should not be indented! -->
  <script type="loncapa/python">
  computed_response = math.sqrt(math.fsum([math.pow(math.pi,2), math.pow(math.e,2)]))
  </script>

  <p>What is the distance in the plane between the points (pi, 0) and (0, e)? You can type math.
      <numericalresponse answer="$computed_response">
          <responseparam type="tolerance" default="0.0001" />
          <formulaequationinput />
      </numericalresponse>
  </p>
  <solution>
    <div class="detailed-solution">
      <p>Explanation</p>
      <p>The decimal numerical system is base ten.</p>
      <p>The standard gravity constant is defined to be precisely 9.80665 m/s<sup>2</sup>.
      This is 9.80 to two decimal places. Entering 9.8 also works.</p>
      <p>By the distance formula, the distance between two points in the plane is
         the square root of the sum of the squares of the differences of each coordinate.
        Even though an exact numerical value is checked in this case, the
        easiest way to enter this answer is to type
        <code>sqrt(pi^2+e^2)</code> into the editor.
        Other answers like <code>sqrt((pi-0)^2+(0-e)^2)</code> also work.
      </p>
    </div>
  </solution>
  </problem>

**Templates**

Exact values

.. code-block:: xml

  <problem>

    <numericalresponse answer="10">
      <formulaequationinput />
    </numericalresponse>

    <solution>
    <div class="detailed-solution">

    </div>
  </solution>
  </problem>

Answers with decimal precision

.. code-block:: xml

  <problem>

    <numericalresponse answer="9.80665">
      <responseparam type="tolerance" default="0.01" />
      <formulaequationinput />
    </numericalresponse>

    <solution>
    <div class="detailed-solution">

    </div>
  </solution>
  </problem>

Answers with percentage precision

.. code-block:: xml

  <problem>

    <numericalresponse answer="100">
      <responseparam type="tolerance" default="10%" />
      <formulaequationinput />
    </numericalresponse>

    <solution>
    <div class="detailed-solution">

    </div>
  </solution>
  </problem>

Answers with scripts

.. code-block:: xml

  <problem>

  <!-- Use python script spacing. The following should not be indented! -->
  <script type="loncapa/python">
  computed_response = math.sqrt(math.fsum([math.pow(math.pi,2), math.pow(math.e,2)]))
  </script>

    <numericalresponse answer="$computed_response">
      <responseparam type="tolerance" default="0.0001" />
      <formulaequationinput />
    </numericalresponse>

    <solution>
    <div class="detailed-solution">

    </div>
  </solution>
  </problem>


**XML Attribute Information**

<script>

  .. image:: ../Images/numericalresponse.png


``<numericalresponse>``

+------------+----------------------------------------------+-------------------------------+
| Attribute  |                 Description                  |              Notes            |
+============+==============================================+===============================+
| ``answer`` | A value to which student input must be       | Note that any numeric         |
|            | equivalent. Note that this expression can be | expression provided by the    |
|            | expressed in terms of a variable that is     | student will be automatically |
|            | computed in a script provided in the problem | simplified on the grader's    |
|            | by preceding the appropriate variable name   | backend.                      |
|            | with a dollar sign.                          |                               |
|            |                                              |                               |
|            | This answer will be evaluated similar to a   |                               |
|            | student's input. Thus '1/3' and 'sin(pi/5)'  |                               |
|            | are valid, as well as simpler expressions,   |                               |
|            | such as '0.3' and '42'                       |                               |
+------------+----------------------------------------------+-------------------------------+


+------------------------+--------------------------------------------+--------------------------------------+
|       Children         |                 Description                |                 Notes                |
+========================+============================================+======================================+
| ``responseparam``      | used to specify a tolerance on the accepted|                                      |
|                        | values of a number. See description below. |                                      |
+------------------------+--------------------------------------------+--------------------------------------+
|``formulaequationinput``| An input specifically for taking math      |                                      |
|                        | input from students. See below.            |                                      |
+------------------------+--------------------------------------------+--------------------------------------+
| ``textline``           | A format to take input from students, see  | Deprecated for NumericalResponse.    |
|                        | description below.                         | Use ``formulaequationinput`` instead.|
+------------------------+--------------------------------------------+--------------------------------------+


<responseparam>

  .. image:: ../Images/numericalresponse4.png

<formulaequationinput/>

========= ============================================= =====
Attribute                  Description                  Notes
========= ============================================= =====
size      (optional) defines the size (i.e. the width)
          of the input box displayed to students for
          typing their math expression.
========= ============================================= =====

<textline> (While <textline /> is supported, its use is extremely discouraged.
We urge usage of <formulaequationinput />. See the opening paragraphs of the
`Numerical Response`_ section for more information.)

  .. image:: ../Images/numericalresponse5.png

.. _Math Expression Syntax:

Math Expression Syntax
----------------------

In NumericalResponses, the student's input may be more complicated than a
simple number. Expressions like ``sqrt(3)`` and even ``1+e^(sin(pi/2)+2*i)``
are valid, and evaluate to 1.73 and -0.13 + 2.47i, respectively.

A summary of the syntax follows:

Numbers
~~~~~~~

Accepted number types:

- Integers: '2520'
- Normal floats: '3.14'
- With no integer part: '.98'
- Scientific notation: '1.2e-2' (=0.012)
- More s.n.: '-4.4e+5' = '-4.4e5' (=-440,000)
- Appending SI suffixes: '2.25k' (=2,250). The full list:

  ====== ========== ===============
  Suffix Stands for One of these is
  ====== ========== ===============
  %      percent    0.01 = 1e-2
  k      kilo       1000 = 1e3
  M      mega       1e6
  G      giga       1e9
  T      tera       1e12
  c      centi      0.01 = 1e-2
  m      milli      0.001 = 1e-3
  u      micro      1e-6
  n      nano       1e-9
  p      pico       1e-12
  ====== ========== ===============

The largest possible number handled currently is exactly the largest float
possible (in the Python language). This number is 1.7977e+308. Any expression
containing larger values will not evaluate correctly, so it's best to avoid
this situation.

Default Constants
~~~~~~~~~~~~~~~~~

Simple and commonly used mathematical/scientific constants are included by
default. These include:

- ``i`` and ``j`` as ``sqrt(-1)``
- ``e`` as Euler's number (2.718...)
- ``pi``
- ``k``: the Boltzmann constant (~1.38e-23 in Joules/Kelvin)
- ``c``: the speed of light in m/s (2.998e8)
- ``T``: the positive difference between 0K and 0°C (285.15)
- ``q``: the fundamental charge (~1.602e-19 Coloumbs)

Operators and Functions
~~~~~~~~~~~~~~~~~~~~~~~

As expected, the normal operators apply (with normal order of operations):
``+ - * / ^``. Also provided is a special "parallel resistors" operator given
by ``||``. For example, an input of ``1 || 2`` would represent the resistance
of a pair of parallel resistors (of resistance 1 and 2 ohms), evaluating to 2/3
(ohms).

At the time of writing, factorials written in the form '3!' are invalid, but
there is a workaround. Students can specify ``fact(3)`` or ``factorial(3)`` to
access the factorial function.

The default included functions are the following:

- Trig functions: sin, cos, tan, sec, csc, cot
- Their inverses: arcsin, arccos, arctan, arcsec, arccsc, arccot
- Other common functions: sqrt, log10, log2, ln, exp, abs
- Factorial: ``fact(3)`` or ``factorial(3)`` are valid. However, you must take
  care to only input integers. For example, ``fact(1.5)`` would fail.
- Hyperbolic trig functions and their inverses: sinh, cosh, tanh, sech, csch,
  coth, arcsinh, arccosh, arctanh, arcsech, arccsch, arccoth


.. _Option Response:

Option Response (Dropdown)
--------------------------

The Option Response input type allows the student to choose from a collection of
answer options, presented as a drop-down list.

Option Response is structurally similar to Multiple Choice. Some conceptual
differences between the two include the following.

* The Multiple Choice radio button format makes it easier for students to read very long response options.

* The Option Response drop-down input format makes it more likely for students to think of an answer and then search for it, rather than relying purely on recognition to answer the question. The Multiple Choice format is more explicit and visual. This makes it a more appropriate choice for presenting tricky or complicated answer options which are intended to get the student to pause and think.

Sample Problem:

.. image:: ../Images/image287.png
    :width: 600
    :alt: Image of an option response problem

**Problem Code:**

.. code-block:: xml

  <problem>

   <p>Option Response is most similar to __________.</p>

    <optionresponse>
     <optioninput
       options="('Multiple Choice','String Response',
                'Numerical Response','External Response',
                'Image Response')"
      correct="Multiple Choice"/>1
    </optionresponse>

   <solution>
     <div class="detailed-solution">
       <p>Explanation</p>
        <p>Like Option Response, Multiple Choice also allows students to select
       from a variety of pre-written responses.</p>
     </div>
    </solution>
  </problem>




**Template**

.. code-block:: xml

  <problem>

    <optionresponse>
     options="('A','B')"
      correct="A"/>
    </optionresponse>

    <solution>
      <div class="detailed-solution">
      </div>
    </solution>
  </problem>



**XML Attribute Information**

<optionresponse>


  .. image:: ../Images/option_response1.png


<optioninput>

  .. image:: ../Images/optionresponse2.png


.. _Schematic Response:

Schematic Response
------------------

The Schematic Response input type provides an interactive grid on which the
student can construct a schematic answer, such as a circuit.

Sample Problem:

.. image:: ../Images/image297.png
 :width: 600
 :alt: Image of a schematic response problem

.. image:: ../Images/image298.png
 :width: 600
 :alt: Image of a schematic response problem

.. image:: ../Images/image299.png
 :width: 600
 :alt: Image of a schematic response explanation

**Problem Code**:

.. code-block:: xml


    <problem>
      Make a voltage divider that splits the provided voltage evenly.

    <schematicresponse>
    <center>
    <schematic height="500" width="600" parts="g,r" analyses="dc"
    initial_value="[["v",[168,144,0],{"value":"dc(1)","_json_":0},["1","0"]],["r",[296,120,0],{"r":"1","_json_":1},["1","output"]],["L",[296,168,3],{"label":"output","_json_":2},["output"]],["w",[296,216,168,216]],["w",[168,216,168,192]],["w",[168,144,168,120]],["w",[168,120,296,120]],["g",[168,216,0],{"_json_":7},["0"]],["view",-67.49999999999994,-78.49999999999994,1.6000000000000003,"50","10","1G",null,"100","1","1000"]]"
    />
    </center>
    <answer type="loncapa/python">
    dc_value = "dc analysis not found"
    for response in submission[0]:
      if response[0] == 'dc':
          for node in response[1:]:
              dc_value = node['output']

    if dc_value == .5:
      correct = ['correct']
    else:
      correct = ['incorrect']

    </answer>
    </schematicresponse>
    <schematicresponse>
    <p>Make a high pass filter.</p>
    <center>
    <schematic height="500" width="600" parts="g,r,s,c" analyses="ac"
    submit_analyses="{"ac":[["NodeA",1,9]]}"
    initial_value="[["v",[160,152,0],{"name":"v1","value":"sin(0,1,1,0,0)","_json_":0},["1","0"]],["w",[160,200,240,200]],["g",[160,200,0],{"_json_":2},["0"]],["L",[240,152,3],{"label":"NodeA","_json_":3},["NodeA"]],["s",[240,152,0],{"color":"cyan","offset":"0","_json_":4},["NodeA"]],["view",64.55878906250004,54.114697265625054,2.5000000000000004,"50","10","1G",null,"100","1","1000"]]"/>
    </center>
    <answer type="loncapa/python">
    ac_values = None
    for response in submission[0]:
      if response[0] == 'ac':
          for node in response[1:]:
              ac_values = node['NodeA']
    print "the ac analysis value:", ac_values
    if ac_values == None:
      correct = ['incorrect']
    elif ac_values[0][1] < ac_values[1][1]:
      correct = ['correct']
    else:
      correct = ['incorrect']
    </answer>
    </schematicresponse>

        <solution>
            <div class="detailed-solution">
                <p>Explanation</p>
                <p>A voltage divider that evenly divides the input voltage can be formed with two identically valued resistors, with the sampled voltage taken in between the two.</p>
                <p><img src="/c4x/edX/edX101/asset/images_voltage_divider.png"/></p>
                <p>A simple high-pass filter without any further constaints can be formed by simply putting a resister in series with a capacitor. The actual values of the components do not really matter in order to meet the constraints of the problem.</p>
                <p><img src="/c4x/edX/edX101/asset/images_high_pass_filter.png"/></p>
            </div>
        </solution>
    </problem>

.. _String Response:



String Response
---------------

The String Response input type provides an input box in which the student can
enter a line of text, which is then checked against a specified expected answer.

A String Response input does not provide any answer suggestions, so it can be a
good way to get the students to engage with the material more deeply in a
sequence and look up, figure out, or remember the correct answer themselves.

Note that a student's answer in a String Response is marked as correct if it
matches every character of the expected answer. This can be a problem with
international spelling, dates, or anything where the format of the answer is not
clear.

Sample Problem:

.. image:: ../Images/image291.png
 :width: 600
 :alt: Image of a string response problem

**Problem Code:**

.. code-block:: xml

  <problem>
    <p><b>Example Problem</b></p>
    <p>What is the name of this unit? (What response type is this?)</p>
    <stringresponse answer="String Response" type="ci">
      <textline size="20"/>
    </stringresponse>
    <solution>
      <div class="detailed-solution">
        <p>Explanation</p>
        <p>The name of this unit is "String Response," written without the punctuation.</p>
        <p>Arbitrary capitalization is accepted.</p>
      </div>
    </solution>
  </problem>

**Template**

.. code-block:: xml

  <problem>
    <stringresponse answer="REPLACE_THIS" type="ci">
      <textline size="20"/>
    </stringresponse>
    <solution>
      <div class="detailed-solution">
      </div>
    </solution>
  </problem>


This response type allows to add more than one answer. Use `additional_answer`  tag to add more answers.

You can add `regexp` to value of `type` attribute, for example: `type="ci regexp"` or `type="regexp"` or `type="regexp cs"`.
In this case, any answer and hint will be treated as regular expressions.
Regular expression has to match whole answer, for answer to be correct.
Student answers "foobar", "o foo" or " ==foo==", will be correct if teacher has set answer=".*foo.*" with type="regexp".

**Template**

.. code-block:: xml

    <problem>
        <stringresponse answer="a1" type="ci regexp">
            <additional_answer>\d5</additional_answer>
            <additional_answer>a3</additional_answer>
            <textline size="20"/>
            <hintgroup>
                <stringhint answer="a0" type="ci" name="ha0" />
                <stringhint answer="a4" type="ci" name="ha4" />
                <stringhint answer="^\d" type="ci" name="re1" />
                <hintpart on="ha0">
                    <startouttext />+1<endouttext />
                </hintpart >
                <hintpart on="ha4">
                    <startouttext />-1<endouttext />
                </hintpart >
                <hintpart on="re1">
                    <startouttext />Any number+5<endouttext />
                </hintpart >
            </hintgroup>
        </stringresponse>
    </problem>


**XML Attribute Information**

<stringresponse>

 .. raw:: html

      <table border="1" class="docutils" width="60%">
        <colgroup>
        <col width="15%">
        <col width="75%">
        <col width="10%">
        </colgroup>
        <thead valign="bottom">
        <tr class="row-odd"><th class="head">Attribute</th>
        <th class="head">Description</th>
        <th class="head">Notes</th>
        </tr>
        </thead>
        <tbody valign="top">
        <tr class="row-even"><td>type</td>
        <td>(optional) “[ci] [regex]”. Add “ci” if the student response should be graded case-insensitively. The default is to take case into consideration when grading. Add “regexp” for correct answer to be treated as regular expression.</td>
        <td>&nbsp;</td>
        </tr>
        <tr class="row-odd"><td>answer</td>
        <td>The string that is used to compare with student answer. If "regexp" is not presented in value of <em>type</em> attribute, student should enter value equal to exact value of this attribute in order to get credit. If  "regexp" is presented in value of <em>type</em> attribute, value of <em>answer</em> is treated as regular expression and exact match of this expression and student answer will be done. If search is successful, student will get credit.</td>
        <td>&nbsp;</td>
        </tr>
        </tbody>
      </table>

      <table border="1" class="docutils" width="60%">
        <colgroup>
        <col width="15%">
        <col width="75%">
        <col width="10%">
        </colgroup>
        <thead valign="bottom">
        <tr class="row-odd"><th class="head">Children</th>
        <th class="head">Description</th>
        <th class="head">Notes</th>
        </tr>
        </thead>
        <tbody valign="top">
        <tr class="row-even"><td>textline</td>
        <td>used to accept student input. See description below.</td>
        <td>&nbsp;</td>
        </tr>
        <tr class="row-odd"><td>additional_answer</td>
        <td>todo</td>
        <td>&nbsp;</td>
        </tr>
        </tbody>
      </table>


<textline>

  .. image:: ../Images/stringresponse2.png

<additional_answer> - Can be unlimited number of this tags. Any tag adds one more additional answer for matching.












