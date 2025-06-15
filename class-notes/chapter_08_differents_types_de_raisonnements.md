# Chapitre 8: Les differents types de raisonnements

## Double Implication

Soient $P$ et $Q$ deux assertions.  

On souhaite montrer que $P \iff Q$

Le raisonnement par double implication consiste a montrer que
$$
P \implies Q \land Q \implies P \\
P \iff Q
$$
  Pourquoi est-ce valide?

(Exercice: faire la table de verite)

#### Exemple 

Soient $A$ et $B$ deux ensembles parties de $E$.
$$
\text{Montrer que: } A = B \iff A \cap B = A \cup B \\
$$


" $\implies$ " On suppose que $A = B$
$$
A \cap B = A \land A \cup B = A \implies A \cup B = A \cap B
$$
 " $\impliedby$ "  On suppose que $A \cup B = A \cap B$ "
$$
A ⊂ A \cup B = A \cap B ⊂ B \\
\text{Donc } A ⊂ B
$$
$A$ et $B$ jouant des roles symmetriques, on a $B ⊂ A$ Donc $A = B$ par double inclusion.

## Contraposee

Soient $P$ et $Q$ 2 assertions.

On souhaite prouver que $P \implies Q$

Le raisonnement par contraposee consiste a prouver que:
$$
\neg Q \implies \neg P
$$
   Pourquoi ce raisonnement est valide?

Par ce que $P \implies Q \iff \neg Q \implies \neg P$ 

(Faire table de verite)

#### Exemple

Soient $x,y ∈ \mathbb{R}$

Montrer que:
$$
x \neq y \implies \frac{1}{1-x} \neq \frac{1}{1-y}
$$
Par contraposee:
$$
\frac{1}{1-x} = \frac{1}{1-y} \implies x = y
$$

#### Exemple

Soint $n ∈ \mathbb{N}$, montrer que:
$$
n = 2p, p ∈\mathbb{N} \iff n^2 = 2p', p' ∈\mathbb{N}
$$
 " $\implies$ "

Supposons que $n$ soit paire.
$$
n = 2p \\
n^2 = 4p^2 \\
n^2 = 2(2p^2) \\
p' = 2p^2
$$
 " $\impliedby$ "

On supopose $n$ impaire.
$$
n = 2p+1 \\
n^2 = 4p^2 +4p + 1 \\
n^2 = 2(2p^2 + 2p) + 1 \\
p' = 2p^2+2p \\
n^2 = 2p'+1
$$
 Donc La contraposee est prouvee.

## L'Absurde

On souhaite prouver l'assertion $P$, la preuve par l'absurde consiste a prouver l'absurdite de l'assertion contraire/complementaire.

Pourquoi ce raisonnement est valide?
$$
P \iff \neg \neg P
$$

or l'absurde consiste a dire que $\neg P$ est faux donc de prouver $\neg \neg P$, et ainsi de prouver $P$.

#### Exemple

Montrer que $\sqrt{2} ∉ \mathbb{Q}$

Raisonnement par l'absurde: on montre qu'il est rationel.
$$
∃ p, q ∈ \mathbb{N}^{*} / \sqrt{2} = \frac{p}{q} \\
\text{PGCD}(p,q) = 1 \iff \text{La fraction est sous forme irreductible} \\
q\sqrt{2} = p \\
q^2 \times 2 = p^2 \iff p^2 \text{est paire} \iff p \text{est paire} \\
∃ k ∈ \mathbb{N} / p = 2k \\
q^2 \times 2 = 4k^2 \\
q^2 = 2k^2 \\
q = 2k' / k' ∈ \mathbb{N} \\
\text{L'absurdite appartient au fait que } p \text{ et } q \text{ sont irreductibles, et pourtant on un PGCD de } 2.
$$

## Disjonction de cas

Soient $P,Q_1, Q_2$ , trois assertio.

On souhaite prouver que $P$ est vraie sachant que $Q_1$ ou $Q_2$ est vraie.
$$
Q_1 \lor Q_2 \implies P
$$
   Le raisonnement consiste donc a montrer que $Q_1 \implies P$, et $Q_2 \implies P$.

Pourquoi ce raisonnement fonctionne?
$$
(Q_1 \implies P) \land (Q_2 \implies P) \iff (Q_1 \lor Q_2) \implies P
$$
  On sait que $Q_1 \implies P$ et $Q_2 \implies P$, donc $Q_1 \lor Q_2 \implies P$   

#### Exemple

Montrer que:
$$
∀ x ∈ \mathbb{R}, 0 \le \frac{x+|x|}{2} \le |x|
$$
$x \ge 0$:
$$
x = |x| \implies \frac{x+|x|}{2} = |x|
$$
 $x < 0$
$$
x = -|x| \implies \frac{x+|x|}{2} = 0
$$
  Ainsi $∀ x ∈ \mathbb{R}, \frac{x+|x|}{2} ∈ [0,|x|]$ 

## Recurrence Simple

#### Théorème

Soient $n_0 ∈ \mathbb{N}$ et $n\ge n_0, P(n)$ une asserti.

On suppose que:

-  $P(n_0)$ (Initialisation)
- $∀ n \ge n_0 , P(n) \iff P(n+1)$ (Heredite)

#### Preuve

On raisonne par l'absurde:

On supoose que $∃ n_1 \ge n_0 / \neg P(n)$ .

On introduit $E$:
$$
E = \{n \ge n_0 / \neg P(n)\}
$$
$E ⊂ \mathbb{N}, \text{card}(E) \neq 0$ car $n_1 ∈ E$.

Par un axiome de Peano, $E$ admet un minimum , note $n_2$

##### Cas 1: $n_2 = n_0$

$$
n_2 ∈ E \iff \neg P(n_2) \\
\text{ or } P(n_2) \iff P(n_0) \\
\text{et  on a } P(n_0) \text{ donc on a pas } n_2 ∈ E 
$$

##### Cas 2: $n_2 \ge n_0 + 1$

$$
\neg P(n_2) \implies \neg P(n_2-1) \\
\iff n_2 - 1 ∈ E \text{ or } \text{min}(E) = n_2 \\
\text{Donc contradiction} 
$$

#### Remarque

Pour effectuer une preuve par recurrence il est obligatoire de disposer d'une relation de recurrence

## Recurrence Double

#### Théorème

Soient $n_0 ∈ \mathbb{N}$ et $n\ge n_0, P(n)$ une assertion.

On suppose que:

-  $P(n_0) \land P(n_0+1)$ (Initialisation)

- $∀ n \ge n_0 , P(n) \land P(n+1) \implies P(n+2) $ (Heredite)

#### Preuve

  On prouve que $Q(n): P(n) \land P(n+1)$ 

  est vraie par recurrence simple.

  Puis que $Q(n)\implies P(n+2)$ 

#### Exemple

Soint $(u_n)$ la suite definie par:
$$
\begin{cases}
∀ n ∈ \mathbb{N}, u_{n+1} = u_{n+1} + u_n \\
u_0 = 0 \\
u_1 = 0
\end{cases}
$$

$$
∀ n ∈ \mathbb{N}, u_n ∈ \mathbb{N}^{*}
$$

$$
u_0, u_1 ∈ \mathbb{N}^{*}
$$

Soit $n ∈ \mathbb{N} / u_n ∈ \mathbb{N}^{*} \land u_{n+1} ∈ \mathbb{N}^{*}$ Montrons que $u_{n+2} ∈ \mathbb{N}^{*}$ 

La somme de 2 entiers est un entier donc $u_{n+2} ∈ \mathbb{N}^{*}$ 

Recurrence double achevee.

## Recurrence Forte

#### Théorème

Soient $n_0 ∈ \mathbb{N}$ et $n\ge n_0, P(n)$ une assertion.

On suppose que:

-  $P(n_0)$ (Initialisation)
- $∀ n \ge n_0 , (P(n_0), P(n_0 + 1), P(n_0 +2), \cdots, P(n)) \implies P(n+1)$ (Heredite)

#### Preuve

On prouve que $Q(n): P(n_0), P(n_0+1), \cdots P(n)$  est vraie par reccurence simple.

#### Exemple

$$
\begin{cases}
∀ n ∈ \mathbb{N}, u_{n+1} = \sum_{k=0}^{n} u_k \\
u_0 = 1
\end{cases}
$$

Montrer que:  $∀ n ∈ \mathbb{N}, 0 < u_n \le 2^{n}$ 
$$
0 < u_0 < 2^{0} 
$$
Donc $P(n_0)$ est vraie.

Soit $n ∈ \mathbb{N} / ∀ 0 \le k \le n, 0 \le u_k \le 2^{k}$ 
$$
u_{n+1} = \sum_{i=0}^{n} u_i > 0
$$

$$
u_{n+1} = \sum_{i=0}^{n} 2^{i} \ge 2^{n+1} - 1
$$

Donc $u_{n+1} ∈ [0, 2^{n+1}]$

## Recurrence finie

#### Théorème

Soit $n_0, n_1 ∈ \mathbb{N} / n_1 > n_0 \land ∀ n ∈ [n_0, n_1], P(n)$

On suppose:

-  $P(n_0)$
- pui que $∀ n_0 \le n \le n_1 - 1, P(n) \implies P(n+1)$  

## Analyse-Synthese

Un raisonnement permettant de determiner toutes les solutions d'un probleme.

Il se deroule en 2 temps:

1. Analyse
1. Synthese

### Analyse

On raisonne sur une hypothetique solution du probleme pour en deduire un maξmum de proprietes qu'elle verifie, afin d'obtenir des *solutions potentielles*.

### Synthese

On verifie qui parmi les solutions potentielles trouvees dans l'analyse sont reelement solutions du probleme considere.

#### Exemple

Soit $f: \mathbb{R} \to \mathbb{R}$

Montrer que $f$ se decompose de maniere unique en la somme d'une fonction paire et d'une fonction impaire.  

##### Analyse

$$
f = g+h \\
g(-x) = g(x)\land h(-x) = -h(x)
$$


$$
∀ x ∈ \mathbb{R}, f(x) = g(x) + h(x) \\
f(-x) = g(-x) + h(-x) = g(x) - h(x) \\
\implies ∀ x ∈ \mathbb{R},
\begin{cases}
g(x) = \frac{f(x) + f(-x)}{2} \\
h(x) = \frac{f(x) - f(-x)}{2}
\end{cases}
$$

##### Synthese

On pose $g: x \mapsto \frac{f(x) + f(-x)}{2}$, et $h:x \mapsto \frac{f(x)-f(-x)}{2}$ 

On observe que:
$$
g + h = f \\
g(-x) = \frac{f(-x) + f(x)}{2} = g(x) \\
h(-x) = \frac{f(-x) - f(x)}{2} = -h(x)
$$

#### Exemple

Soient $I$ un intervalle de $\mathbb{R}$, $a,b,y_0, y_1 ∈ \mathbb{K}, x_0 ∈ I$ et $f:I\to\mathbb{K}$

avec $f$ continue. Le probleme de Cauchy.
$$
\begin{cases}
y''+ay'+by = f \\
y(x_0) = y_0 \\
y'(x_0) = y_1
\end{cases}
$$
​    admet une unique solution.

##### Analyse

$$
r^2+ar+b = 0 \iff (r-r_1)(r-r_2) = 0, r_1, r_2 ∈ \mathbb{C} \\
r_1 + r_2 = -a \\
r_1 \times r_2 = b
$$

D'ou:
$$
y'' - (r_1 + r_2)y' + r_1r_2y\\
(y'-r_1y)' - r_2(y'-r_1y)
$$

###### Cas ou $\mathbb{C} = \mathbb{K}$

Soit $y$ une solution du probleme,

   On pose $z: x \mapsto y'(x) - r_1y(x)$, $z$ est uniquement determine car solution du probleme de Cauchy:
$$
\begin{cases}
z'-r_2z = f \\
z(x_0) = y_1 - r_1 y_0
\end{cases}
$$
 $y$ est uniquement determine car solution du probleme de Cauchy:
$$
\begin{cases}
y' - r_1y = z \\
y(x_0) = y_0
\end{cases}
$$

##### Synthese

Soit $z$ la solution du probleme de Cauchy:
$$
\begin{cases}
z'-r_2z = f \\
z(x_0) = y_1 - r_1 y_0
\end{cases}
$$
 Soit $y$ la solution du probleme de Cauchy:
$$
\begin{cases}
y' - r_1y = z \\
y(x_0) = y_0
\end{cases}
$$
On a : $y(x_0) = y_0$ ,
$$
y'(x_0) = z(x_0) + r_1y(x_0) \\
= y_1 - r_1y_0 + r_1y_0 \\
= y_1
$$
On a:
$$
y' = r_1y + z
$$
Or $y$ et $z$ sont derivables donc $y''$ existe:
$$
y'' = r_1y'+z' \\
= r_1y' + (f+r_2z) \\
= r_1y' + f + r_2(y'-r_1y) \\
= (r_1+r_2)y' -r_1r_2y + f \\
y'' + ay' + by = f
$$

###### Cas ou $\mathbb{R} = \mathbb{K}$ 

On a unicite et on a existence d'une solution $y$ mais *a priori* a valeur complexes

On montre que $\overline{y}: x \mapsto \overline{y(x)}$ 

est solution du meme probleme de Cauchy (Exercice)

Par unicite, $∀ x ∈ I, \overline{y}(x) = y(x)$

donc $y$ est bien a valeurs reelles. 
