<h1>CC5 - Game Master</h1>
<p><strong>Due: Thursday, October 29nd @ 8:00pm</strong></p>
<p><em>This is not a team assignment, do not copy someone else&rsquo;s work.</em></p>
<p>&nbsp;</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/7c29c2bc-088b-483c-af28-d898c08de7fb/binary-tree.png" alt="binary-tree.png" width="410" height="335" /></p>
<p style="text-align: center;"><sup>The perception of a computer science major</sup></p>
<h2>Introduction</h2>
<p>"In our finite lives, we have infinite options"</p>
<p>In the game of life, there is an individual called the game master who gives you a decision tree that represents a series of<span style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';"> possible paths ahead. Each decision has an overall aggregate reward or consequence that varies.</span></p>
<p><span style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';">However, the game master is tricky, and he gives you misleading paths that can steer you astray. </span>You don't want to go down any single path in fear that you will not choose a favorable outcome. You evaluate this seeminglingly "infinite" tree by developing a program to simulate each potential collective pathways in an attempt to outsmart the game master.</p>
<pre><sub>With your algorithm are you ensured to beat the game master every time?</sub> <sub>(Answer at the bottom of the page)</sub></pre>
<p>&nbsp;</p>
<h2>Challenge</h2>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/ad80cfe9-7a6f-474d-be73-fe306d12e65f/Untitled%20Diagram.png" alt="Untitled Diagram.png" /></p>
<h4>Overview</h4>
<p>Imagine that your life is at the root of the tree given to you where each decision is denoted by a left and right child. Your task is to find the best place to start at or in other words to d<span style="text-decoration: underline;"><span style="font-family: geomanist, sans-serif;">evelop an algorithm that returns the largest sum of a valid binary <em>search</em> subtree. </span></span><span style="font-family: geomanist, sans-serif;">The subtree <strong>must</strong> be a valid BST in order to consider the sum. </span></p>
<p><span style="font-family: geomanist, sans-serif;">To recall, a valid <span style="text-decoration: underline;">binary search tree</span> is defined as:</span></p>
<ul>
<li>Each node's left subtree contains only nodes with values lesser than the node&rsquo;s value</li>
<li>Each node's right subtree of a node contains only nodes with values greater than the node&rsquo;s value</li>
<li>There are no duplicate node values</li>
</ul>
<p><sub>The following TreeNode class is given to you</sub></p>
<table style="border-collapse: collapse; width: 69.3532%; height: 96px; background-color: #f5f5f5; border-color: #f5f5f5;" border="1">
<tbody>
<tr style="height: 96px;">
<td style="width: 100%; height: 96px;">
<pre><span style="font-family: 'courier new', courier, monospace;"><strong> class TreeNode:</strong></span><br /><span style="font-family: 'courier new', courier, monospace;">  &nbsp;  def __init__(self, val, left=None, right=None):</span><br /><span style="font-family: 'courier new', courier, monospace;">  &nbsp; &nbsp; &nbsp;  self.val = val</span><br /><span style="font-family: 'courier new', courier, monospace;">  &nbsp; &nbsp; &nbsp;  self.left = left</span><br /><span style="font-family: 'courier new', courier, monospace;">  &nbsp; &nbsp; &nbsp;  self.right = right</span></pre>
</td>
</tr>
</tbody>
</table>
<pre><sub><span style="font-family: geomanist, sans-serif;">Complete the function below</span></sub></pre>
<p><strong>game_master(root)</strong></p>
<ul>
<li><strong>root</strong>: TreeNode</li>
<li><span style="font-family: geomanist, sans-serif;">Determines the largest sum of a valid binary <em>search</em> subtree.&nbsp;</span></li>
<li><span style="font-family: geomanist, sans-serif;">Note: The tree given is a binary tree, and does not have to follow BST child protocol. The TreeNodes will <em>always</em> have values of integer type.</span></li>
<li><span style="text-decoration: underline;">Return</span>:<strong> int</strong></li>
</ul>
<h4>&nbsp;</h4>
<h4>Complexity</h4>
<p>Time Complexity: <strong>O(N)</strong>&nbsp;where N is the number of nodes in the tree</p>
<p>Space Complexity: <strong>O(1)</strong>&nbsp;not including the space allocated for the call stack</p>
<p>&nbsp;</p>
<h4>Examples</h4>
<p><strong>(empty tree)</strong></p>
<p>output:<strong> 0</strong></p>
<p>&nbsp;</p>
<p><strong>&nbsp; &nbsp; 1</strong></p>
<p>output:&nbsp;<strong>1</strong></p>
<pre><br />      5<br />  5<strong>       7</strong><br />    6<strong>   6   8</strong><br /><br />output: 7 + 6 + 8 = <strong>21</strong><br /><br />      5<br />  6       7<br /><strong>9   </strong>3   7   8   <br /><br />output: <strong>9 --&gt; the node 9 itself is a valid subtree</strong><strong><br /></strong></pre>
<p>&nbsp;</p>
<pre>   2<br /><br /><strong>2 &nbsp; &nbsp; </strong>2<br /><strong><br /></strong>output: <strong>2 --&gt; can have preference over the right # 2 as well (same result)</strong><br /><br /></pre>
<pre><strong>      5</strong><br /><strong>  3       7</strong><br /><strong>2   4   6   8</strong><br /><br />output: 5 + 3 + 2 + 4 + 7 + 6 + 8 = <strong>35<br /><br /></strong></pre>
<h2>Submission</h2>
<h4>Deliverables</h4>
<p>Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00p Eastern Time on Thursday, 10/29/20.</p>
<p>Your .zip folder can contain other files (for example, <code>description.md</code> and <code>tests.py</code>), but must include (at least) the following:</p>
<pre><code>CC5.zip
    |<span class="hljs-type">&mdash; CC5</span>/
        |<span class="hljs-type">&mdash; README</span>.md        (<span class="hljs-keyword">for</span> coding challenge feedback)
        |<span class="hljs-type">&mdash; __init__</span>.py      (<span class="hljs-keyword">for</span> proper Mimir testcase loading)
        |<span class="hljs-type">&mdash; solution</span>.py      (contains your solution source code)
</code></pre>
<h4>&nbsp;</h4>
<h4>Grading</h4>
<p>The following 100-point rubric will be used to determine your grade on CC5:</p>
<ul>
<li>Tests (75)
<ul>
<li>00 - Coding Standard: __/5</li>
<li>01 - Basic: __/5</li>
<li>02 - Left and Right Biased Trees: __/10</li>
<li>03 - Tree Leaves: __/10</li>
<li>04 - Larger Trees: __/15</li>
<li>05 - Even Larger Trees - Balanced: __/15</li>
<li>06 - Even Larger Trees - Unbalanced: __/15</li>
</ul>
</li>
<li>Manual (25)
<ul>
<li>Time Complexity is <em>O(N)</em>: __/10</li>
<li>Space Complexity is <em>O(1)</em>: __/10</li>
<li>README.md is <em>completely</em> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5</li>
</ul>
</li>
</ul>
<p>&nbsp;</p>
<h2>Tips, Tricks &amp; Notes</h2>
<ul>
<li>This coding challenge is essentially two separate problems put together. Try to solve each individually, then combine them together. This will help greatly with compartmentalizing the conceptualization.
<ol>
<li>Finding the largest sum of a binary subtree&nbsp;&nbsp;</li>
<li>Validating if the tree is a binary search tree</li>
</ol>
</li>
<li>Our solution contains a recursive bottom up/depth first search/post order traversal algorithm.</li>
<li>Can you create another function to help you... inner? Can this function return multiple results at once? What are <em>all </em>the elements you should be keeping track of?</li>
<li>Remember: The space of the tree given is not included in the space complexity rather the additional or exra space that is ued is what comprises this.</li>
</ul>
<p>&nbsp;</p>
<h3>Have a great Halloween! 🎃🍭🕸️🕷️👻👽🧟🔮</h3>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/4378c7c4-d374-4b88-bbac-3b1eeeee8c39/ezgif.com-gif-maker%20%281%29.gif" alt="ezgif.com-gif-maker (1).gif" width="364" height="368" /></p>
<p><sup>Boo Spooky Tree (BST)</sup></p>
<p>&nbsp;</p>
<p><strong>Answer</strong>: No, you are not <em>always</em> guaranteed to be able to beat the game master. And that's okay because just like in life, we have the opportunity to make a <em>decision</em> to get up and try again!</p>
<p>Finding the largest valid subtree sum does not guarantee the <em>opportunity</em> for the highest valid path sum or in other words, it does not <em>have</em> to contain this path. The tree can have a disconnected sub path sum that is greater. Try to think of some examples.&nbsp;</p>
<p>&nbsp;</p>
<p><em style="background-color: transparent;">Coding challenge authored by Max Huang &amp; Anna De Biasi</em></p>