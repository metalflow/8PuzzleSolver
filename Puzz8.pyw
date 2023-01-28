#imports

class Puzzle8():
    SearchType = ""
    Puzzle = [[0] * 3]*3

    def __init__(self,search,puzzleIn):
        SearchType = search
        if self.SearchType != "best-first" and self.SearchType != "A*":
             sys.exit("Please enter a string in the format method:string where the only supported methods are best-first and A*.")

       
        if len(Puzzle) != 9 and len(Puzzle) != 16:
            sys.exit("Please enter a puzzle of size 9 or 16 (e.g. b,1,2,3,4,5,6,7,8)")
        elif len(Puzzle) == 9:
            checkCharList = ['b',1,2,3,4,5,6,7,8]
            Puzz8.Puzzle8(SearchType,Puzzle).Solve()
        elif len(Puzzle) == 16:
            checkCharList = ['b',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        else:
            sys.exit("Puzzle Size check failed?! How?!")

        fail = 0
        for checkChar in checkCharList:
            if checkChar not in checkCharList:
                print("Puzzle is missing charcater "+str(checkChar))
                fail = 1
        if fail:
            sys.exit()

         for charNum in range(len(puzzleIn)):




"""
The general approach we consider is called best-first search. Best-first search is an
instance of the general TREE-SEARCH or GRAPH-SEARCH algorithm in which a node is
selected for expansion based on an evaluation function, f(n). The evaluation function is EVALUATION
FUNCTION
construed as a cost estimate, so the node with the lowest evaluation is expanded first. The
implementation of best-first graph search is identical to that for uniform-cost search (Figure 3.14), except for the use of f instead of g to order the priority queue.
The choice of f determines the search strategy. (For example, as Exercise 3.21 shows,
best-first tree search includes depth-first search as a special case.) Most best-first algorithms
include as a component of f a heuristic function, denoted h(n): HEURISTIC
FUNCTION
h(n) = estimated cost of the cheapest path from the state at node n to a goal state.
(Notice that h(n) takes a node as input, but, unlike g(n), it depends only on the state at that
node.) For example, in Romania, one might estimate the cost of the cheapest path from Arad
to Bucharest via the straight-line distance from Arad to Bucharest.
Heuristic functions are the most common form in which additional knowledge of the
problem is imparted to the search algorithm. We study heuristics in more depth in Section 3.6.
For now, we consider them to be arbitrary, nonnegative, problem-specific functions, with one
constraint: if n is a goal node, then h(n)=0. The remainder of this section covers two ways
to use heuristic information to guide search.
3.5.1 Greedy best-first search
Greedy best-first search8 tries to expand the node that is closest to the goal, on the grounds GREEDY BEST-FIRST
SEARCH
that this is likely to lead to a solution quickly. Thus, it evaluates nodes by using just the
heuristic function; that is, f(n) = h(n).
Let us see how this works for route-finding problems in Romania; we use the straightline distance heuristic, which we will call hSLD . If the goal is Bucharest, we need to STRAIGHT-LINE
DISTANCE
know the straight-line distances to Bucharest, which are shown in Figure 3.22. For example, hSLD (In(Arad)) = 366. Notice that the values of hSLD cannot be computed from the
problem description itself. Moreover, it takes a certain amount of experience to know that
hSLD is correlated with actual road distances and is, therefore, a useful heuristic.
Figure 3.23 shows the progress of a greedy best-first search using hSLD to find a path
from Arad to Bucharest. The first node to be expanded from Arad will be Sibiu because it
is closer to Bucharest than either Zerind or Timisoara. The next node to be expanded will
be Fagaras because it is closest. Fagaras in turn generates Bucharest, which is the goal. For
this particular problem, greedy best-first search using hSLD finds a solution without ever
8 Our first edition called this greedy search; other authors have called it best-first search. Our more general
usage of the latter term follows Pearl (1984).

expanding a node that is not on the solution path; hence, its search cost is minimal. It is
not optimal, however: the path via Sibiu and Fagaras to Bucharest is 32 kilometers longer
than the path through Rimnicu Vilcea and Pitesti. This shows why the algorithm is called
“greedy”—at each step it tries to get as close to the goal as it can.
Greedy best-first tree search is also incomplete even in a finite state space, much like
depth-first search. Consider the problem of getting from Iasi to Fagaras. The heuristic suggests that Neamt be expanded first because it is closest to Fagaras, but it is a dead end. The
solution is to go first to Vaslui—a step that is actually farther from the goal according to
the heuristic—and then to continue to Urziceni, Bucharest, and Fagaras. The algorithm will
never find this solution, however, because expanding Neamt puts Iasi back into the frontier,
Iasi is closer to Fagaras than Vaslui is, and so Iasi will be expanded again, leading to an infinite loop. (The graph search version is complete in finite spaces, but not in infinite ones.) The
worst-case time and space complexity for the tree version is O(bm), where m is the maximum
depth of the search space. With a good heuristic function, however, the complexity can be
reduced substantially. The amount of the reduction depends on the particular problem and on
the quality of the heuristic.
"""


"""
A* search: Minimizing the total estimated solution cost
The most widely known form of best-first search is called A* A search (pronounced “A-star * SEARCH
search”). It evaluates nodes by combining g(n), the cost to reach the node, and h(n), the cost
to get from the node to the goal:
f(n) = g(n) + h(n) .
Since g(n) gives the path cost from the start node to node n, and h(n) is the estimated cost
of the cheapest path from n to the goal, we have
f(n) = estimated cost of the cheapest solution through n .
Thus, if we are trying to find the cheapest solution, a reasonable thing to try first is the
node with the lowest value of g(n) + h(n). It turns out that this strategy is more than just
reasonable: provided that the heuristic function h(n) satisfies certain conditions, A* search is
both complete and optimal. The algorithm is identical to UNIFORM-COST-SEARCH except
that A* uses g + h instead of g.

Conditions for optimality: Admissibility and consistency
The first condition we require for optimality is that h(n) be an admissible heuristic. An ADMISSIBLE
HEURISTIC
admissible heuristic is one that never overestimates the cost to reach the goal. Because g(n)
is the actual cost to reach n along the current path, and f(n) = g(n) + h(n), we have as an
immediate consequence that f(n) never overestimates the true cost of a solution along the
current path through n.
Admissible heuristics are by nature optimistic because they think the cost of solving
the problem is less than it actually is. An obvious example of an admissible heuristic is the
straight-line distance hSLD that we used in getting to Bucharest. Straight-line distance is
admissible because the shortest path between any two points is a straight line, so the straight
Section 3.5. Informed (Heuristic) Search Strategies 95
line cannot be an overestimate. In Figure 3.24, we show the progress of an A* tree search for
Bucharest. The values of g are computed from the step costs in Figure 3.2, and the values of
hSLD are given in Figure 3.22. Notice in particular that Bucharest first appears on the frontier
at step (e), but it is not selected for expansion because its f-cost (450) is higher than that of
Pitesti (417). Another way to say this is that there might be a solution through Pitesti whose
cost is as low as 417, so the algorithm will not settle for a solution that costs 450.
CONSISTENCY A second, slightly stronger condition called consistency (or sometimes monotonicity)
MONOTONICITY is required only for applications of A* to graph search.9 A heuristic h(n) is consistent if, for
every node n and every successor n of n generated by any action a, the estimated cost of
reaching the goal from n is no greater than the step cost of getting to n plus the estimated
cost of reaching the goal from n
:
h(n) = c(n, a, n
) + h(n
) .
This is a form of the general triangle inequality, which stipulates that each side of a triangle TRIANGLE
INEQUALITY
cannot be longer than the sum of the other two sides. Here, the triangle is formed by n, n
,
and the goal Gn closest to n. For an admissible heuristic, the inequality makes perfect sense:
if there were a route from n to Gn via n that was cheaper than h(n), that would violate the
property that h(n) is a lower bound on the cost to reach Gn.
It is fairly easy to show (Exercise 3.29) that every consistent heuristic is also admissible.
Consistency is therefore a stricter requirement than admissibility, but one has to work quite
hard to concoct heuristics that are admissible but not consistent. All the admissible heuristics
we discuss in this chapter are also consistent. Consider, for example, hSLD . We know that
the general triangle inequality is satisfied when each side is measured by the straight-line
distance and that the straight-line distance between n and n is no greater than c(n, a, n
).
Hence, hSLD is a consistent heuristic.
Optimality of A*
As we mentioned earlier, A* has the following properties: the tree-search version of A* is
optimal if h(n) is admissible, while the graph-search version is optimal if h(n) is consistent.
We show the second of these two claims since it is more useful. The argument essentially mirrors the argument for the optimality of uniform-cost search, with g replaced by
f—just as in the A* algorithm itself.
The first step is to establish the following: if h(n) is consistent, then the values of
f(n) along any path are nondecreasing. The proof follows directly from the definition of
consistency. Suppose n is a successor of n; then g(n
) = g(n) + c(n, a, n
) for some action
a, and we have
f(n
) = g(n
) + h(n
) = g(n) + c(n, a, n
) + h(n
) = g(n) + h(n) = f(n) .
The next step is to prove that whenever A* selects a node n for expansion, the optimal path
to that node has been found. Were this not the case, there would have to be another frontier
node n on the optimal path from the start node to n, by the graph separation property of
9 With an admissible but inconsistent heuristic, A* requires some extra bookkeeping to ensure optimality.

Arad as the start state. Nodes inside a given contour have f-costs less than or equal to the
contour value.

From the two preceding observations, it follows that the sequence of nodes expanded
by A* using GRAPH-SEARCH is in nondecreasing order of f(n). Hence, the first goal node
selected for expansion must be an optimal solution because f is the true cost for goal nodes
(which have h = 0) and all later goal nodes will be at least as expensive.
The fact that f-costs are nondecreasing along any path also means that we can draw
CONTOUR contours in the state space, just like the contours in a topographic map. Figure 3.25 shows
an example. Inside the contour labeled 400, all nodes have f(n) less than or equal to 400,
and so on. Then, because A* expands the frontier node of lowest f-cost, we can see that an
A* search fans out from the start node, adding nodes in concentric bands of increasing f-cost.
With uniform-cost search (A* search using h(n)=0), the bands will be “circular”
around the start state. With more accurate heuristics, the bands will stretch toward the goal
state and become more narrowly focused around the optimal path. If C* is the cost of the
optimal solution path, then we can say the following:
• A* expands all nodes with f(n) < C*.
• A* might then expand some of the nodes right on the “goal contour” (where f(n) = C*)
before selecting a goal node.
Completeness requires that there be only finitely many nodes with cost less than or equal to
C*, a condition that is true if all step costs exceed some finite  and if b is finite.
Notice that A* expands no nodes with f(n) > C*—for example, Timisoara is not
expanded in Figure 3.24 even though it is a child of the root. We say that the subtree below
PRUNING Timisoara is pruned; because hSLD is admissible, the algorithm can safely ignore this subtree
while still guaranteeing optimality. The concept of pruning—eliminating possibilities from
consideration without having to examine them—is important for many areas of AI.
One final observation is that among optimal algorithms of this type—algorithms that
extend search paths from the root and use the same heuristic information—A* is optimally
efficient for any given consistent heuristic. That is, no other optimal algorithm is guaran- OPTIMALLY
EFFICIENT
teed to expand fewer nodes than A* (except possibly through tie-breaking among nodes with
f(n) = C*). This is because any algorithm that does not expand all nodes with f(n) < C*
runs the risk of missing the optimal solution.
That A* search is complete, optimal, and optimally efficient among all such algorithms
is rather satisfying. Unfortunately, it does not mean that A* is the answer to all our searching
needs. The catch is that, for most problems, the number of states within the goal contour
search space is still exponential in the length of the solution. The details of the analysis are
beyond the scope of this book, but the basic results are as follows. For problems with constant
step costs, the growth in run time as a function of the optimal solution depth d is analyzed in
ABSOLUTE ERROR terms of the the absolute error or the relative error of the heuristic. The absolute error is
RELATIVE ERROR defined as ? = h* - h, where h* is the actual cost of getting from the root to the goal, and
the relative error is defined as  = (h* - h)/h*.
The complexity results depend very strongly on the assumptions made about the state
space. The simplest model studied is a state space that has a single goal and is essentially a
tree with reversible actions. (The 8-puzzle satisfies the first and third of these assumptions.)
In this case, the time complexity of A* is exponential in the maximum absolute error, that is,
O(b?). For constant step costs, we can write this as O(bd), where d is the solution depth.
For almost all heuristics in practical use, the absolute error is at least proportional to the path
cost h*, so  is constant or growing and the time complexity is exponential in d. We can
also see the effect of a more accurate heuristic: O(bd) = O((b)d), so the effective branching
factor (defined more formally in the next section) is b.
When the state space has many goal states—particularly near-optimal goal states—the
search process can be led astray from the optimal path and there is an extra cost proportional
to the number of goals whose cost is within a factor  of the optimal cost. Finally, in the
general case of a graph, the situation is even worse. There can be exponentially many states
with f(n) < C* even if the absolute error is bounded by a constant. For example, consider
a version of the vacuum world where the agent can clean up any square for unit cost without
even having to visit it: in that case, squares can be cleaned in any order. With N initially dirty
squares, there are 2N states where some subset has been cleaned and all of them are on an
optimal solution path—and hence satisfy f(n) < C*—even if the heuristic has an error of 1.
The complexity of A* often makes it impractical to insist on finding an optimal solution.
One can use variants of A* that find suboptimal solutions quickly, or one can sometimes
design heuristics that are more accurate but not strictly admissible. In any case, the use of a
good heuristic still provides enormous savings compared to the use of an uninformed search.
In Section 3.6, we look at the question of designing good heuristics.
Computation time is not, however, A*’s main drawback. Because it keeps all generated
nodes in memory (as do all GRAPH-SEARCH algorithms), A* usually runs out of space long
Section 3.5. Informed (Heuristic) Search Strategies 99
function RECURSIVE-BEST-FIRST-SEARCH(problem) returns a solution, or failure
return RBFS(problem, MAKE-NODE(problem.INITIAL-STATE),8)
function RBFS(problem, node,f limit) returns a solution, or failure and a new f-cost limit
if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
successors ?[ ]
for each action in problem.ACTIONS(node.STATE) do
add CHILD-NODE(problem, node, action) into successors
if successors is empty then return failure, 8
for each s in successors do /* update f with value from previous search, if any */
s.f ? max(s.g + s.h, node.f ))
loop do
best ? the lowest f-value node in successors
if best.f > f limit then return failure, best.f
alternative ?the second-lowest f-value among successors
result, best.f ? RBFS(problem, best, min(f limit, alternative))
if result  = failure then return result
Figure 3.26 The algorithm for recursive best-first search.
before it runs out of time. For this reason, A* is not practical for many large-scale problems. There are, however, algorithms that overcome the space problem without sacrificing
optimality or completeness, at a small cost in execution time. We discuss these nex
"""


