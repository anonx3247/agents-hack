# Chapitre 22: Dénombrement

## Définition et cardinal d'un ensemble fini

#### Définition

Soit $n ∈ \mathbb{N}^{*}$,
l'ensemble
$$
[[1,n]]
$$ 
est l'ensemble des entiers allant de $1$ a $n$

Par convention si $n=0$ alors l'ensemble est $\varnothing$

#### Lemme

Soit $n,m ∈ \mathbb{N}$

si $[[1,n]]$ et $[[1,m]]$ sont en bijection alors $n=m$

#### Preuve
On prouve par récurrence que
$$
∀ n ∈ \mathbb{N}, P(n): "∀ m ∈ \mathbb{N}, \text{ si } [[1,m]] \text{ est en bijetion avec } [[1,n]] \text{ alors } n=m
$$

**Initialisation:**

$P(0)$ est vrai car $\varnothing$ est en bijection avec lui-même

**Hérédité:**

Soit $n ∈ \mathbb{N}$ tel que $P(n)$, montrons $P(n+1)$

Soit $m ∈ \mathbb{N} / [[1,n+1]]$ soit en bijection avec $[[1,m]]$ via l'application $φ$

*Cas 1:* $φ (n+1) = m$ 

On en déduit que $[[1,n]]$ est en bijection avec $[[1,m-1]]$ via $φ _{|[1,n]}^{|[1,m-1]}$

Par hypothèse de récurrence, $n = m-1$ Donc $n+1=m$

*Cas 2:* $φ (n+1) \neq m$

On note $a = φ (n+1)$ et $τ$ l'application de $[[1,n]]$ dans $[[1,m]]$ qui intervertit $a$ et $m$ et reste invariant les autres élements,

$τ$ est involutive, donc elle est bijective.

$τ \circ φ$ l'est donc aussi.

et $τ \circ φ [[1,n+1]] \to [[1,m]]$ et $τ \circ φ (n+1) = m$
On est donc rammené au cas précédent.

Récurrence achevée

#### Définition-Théorème

Soit $E$ un ensemble

On dit que $E$ est fini si il existe un $n ∈ \mathbb{N}$ tel que $[[1,n]]$ soit en bijection avec $E$.

On note alors $n = |E| = \text{card}(E) = E^{\#}$

Sinon $E$ est infini

#### Preuve

**unicité**:
Soient $n,m$ deux cardinaux de $E$.

Soit $φ : E \to [[1,n]]$ une application bijective
Soit $ψ : E \to [[1,m]]$ une application bijective

$ψ \circ φ ^{-1}$ est une bijection de $[[1,n]]$ dans $[[1,m]]$ donc par le lemme précédent, $n=m$

#### Exemples

- $\text{card}([[1,n]]) = n$ car $[ [1,n]]$ est en bjection avec lui meme par l'identité
- en particulier $\text{card}(\varnothing) = 0$
- Soient $a,b ∈ \mathbb{Z} / a \le b$ alors $\text{card}([ [a,b]]) = b-a+1$ car il est en bijection avec $[ [1,b-a+1]]$ par l'application $k \mapsto k-a+1$

#### Remarques

- Conaissant $n=\text{card}(E)$ et de l'application bijective $φ :[[1,n]] \to E$ on peut écrire $E$ en extension:
$$
E = \{ φ (1), φ (2), φ (3), \cdots φ (n)\}
$$

La réciproque est fausse car il faut vérifier que les élements de l'ecriture en extension sont deux-a-deux distincts.

On suppose que $E$ est fini:
$$
\sum_{i ∈ E} 1 = \text{card}(E)
$$ 

Car le changement d'indice $j = φ (i)$ avec $φ E \to [[1,n]]$ une bijection alors on obtinet:
$$
\sum_{i ∈ E} 1 = \sum_{j=1}^{n} 1 = n=\text{card}(E)
$$

## Sous-ensembles d'un ensemble fini

#### Lemme

Soit $E$ un ensemble fini, non vide

Soit $a ∈ E$ on pose $E'=E\backslash \{a\}$

Alors $|E'| = |E| - 1$

#### Preuve

On note $n = |E|$ et procédont par récurrence sur $n$

La propriété est vraie pour $n=1$ car $E' = \varnothing$ donc $|E'| = 0 = 1-1$

Supposons la propriété vraie pour $n$, montrons que'elle est vraie pour $n+1$

On prends $|E| = n+1$ donc il existe une bijection $φ : E \to [[1,n+1]]$ 

*Cas 1:*
Si $φ (a) = n+1$

alors $E'$ est en bijection avec $[[1,n]]$ via $φ _{|E'}^{|[1,n]}$

Ainsi $|E'| = n = |E| - 1$

*Cas 2:*
Si $φ (a) \neq n+1$

On considère $τ $ la transposition de $[[1,n+1]]$ dans lui même qui échange $φ (a)$ et $n+1$ et laisse invariant les autres.

$τ $ est bijective car involutive et $τ \circ φ : E \to [[1,n+1]]$ vérifie que $τ \circ φ (a) = n+1$ et on est ramené au cas précédent.

#### Remarque

La récurrence n'est pas utile (il faut noter cela en DS)

#### Théorème

Soit $E$ un ensemble fini et $F ⊂ E$ alors $F$ est fini et $|F| \le |E|$ avec $|F| = |E|$ si et seulement si $F = E$

#### Preuve

On note $n = \text{card}(E)$ et on procède par récurrence sur $n$

La propriété est vraie au rang $0$ car si $n=0$ alors $E= \varnothing$ et $F = \varnothing$

On suppose donné $n ∈ \mathbb{N}$ tel que la propriété soit établie au rang $n$ montrons la au rang $n+1$

$|E| = n+1$

et $F ⊂ E$.

*Cas 1*

Si $F = E$ alors $|F| = |E|$

*Cas 2*

Si $F \neq E$ alors $∃ a ∈ E / F ⊂ E \backslash \{a\}$ par le lemme précédent, $|E \backslash \{a\}| = |E| -1$ donc par hypothèse de récurrence, alors $F$ est fini et plus petit que $|E \backslash \{a\}|$ donc $|F| < |E|$

## Réunion finie d'ensembles finis

#### Théorème

Soient $E, A,B ⊂ E$ avec $A$ et $B$ finis et disjoints

$A \cup B$ est fini et $|A \cup B| = |A| + |B|$

#### Preuve

Soit $n = \text{card}(A), p = \text{card}(B)$

soient les bijections $f : A \to [[1,n]], g: B \to [[1,p]]$

On pose $φ : A \cup B \to [[1,n+p]$
$$
φ : x \mapsto \begin{cases}
f(x) \text{ si } x ∈ A \\
g(x) + n \text{ si } x ∈ B
\end{cases}
$$

Comme $A,B$ sont disjoints, alors $φ $ est bien une application, et elle est bijective:

Injectivite:

$φ (x) = φ (y)$

si $x,y ∈ A$ alors 
$$
f^{-1}(φ (x)) = f^{-1} (φ (y)) \\
x = y
$$
si $x,y ∈ B$ alors
$$
g^{-1}(φ (x)-n) = g^{-1} (φ (y)-n) \\
x = y
$$
Sinon si $x ∈ A$ et $y ∈ B$ (ici ils jouent des roles symmétriques)

Alors $φ (x) \neq φ (y)$ car $∀ x ∈ A, φ (x) \le n$ et $∀ y ∈ B, φ (y) > n$

Surjectivité:
$y = φ (x)$

si $n+1 \le y \le n+p$

#### Corollaire

Soient $E$ un ensemble et $(A_i)_{1 \le i \le p}$ une famille de $p$ parties de $E$ deux a deux disjoints, on a alors que:
$$
\bigcup_{i=1}^{p} A_i 
$$
Est un ensemble fini et
$$
|\bigcup_{i=1}^{p} A_i | = \sum_{i=1}^{p} |A_i|
$$

#### Exemple

Combien y a t'il dans un quadrillage de $3\times3$

Il y a les carés de taille $1  (9)$, les carés de taille $4 (4)$ et ceux de taille $9 (1)$ donc au total:
$$
14
$$

#### Corollaire

Soit $E$ fini et $A ⊂ E$, alors $A^{c} ⊂ E$ et $|A^{c}| = |E| - |A|$

#### Preuve

$E = A \cup A^{c}$ et ils sont disjoints donc $|E| = |A| + |A^{c}|$

#### Exemple

Combien y a t'il de mots de 3 lettres qui contiennent au moins un "w"?

- $E = \{\text{les mots de 3 lettres }\}$ avec $|E| = 26^3$
- $A = \{\text{les mots de 3 lettres ayant au moins un "w"}\}$
- $A^{c} = \{\text{les mots de 3 lettres ayant aucun "w"}, |A^{c}| = 25^3$

donc $|A| = 26^3 - 25^3$

#### Corollaire "Principe d'inclusion-exclusion" / "Formule de Pointcarré" / "Formule du Crible"

Soient $E$ un ensemble fini, $A,B ⊂ E$

$A \cup B$ est fini et $|A \cup B| = |A| + |B| - |A \cap B|$

#### Preuve
$$
A = (A\backslash B) \cup_{-} (A \cap B)
$$
donc $|A| = |A\backslash B| + |A \cap B|$

$A \cup B = B \cup_{-} A\backslash B$
$$
|A \cup B|  = |B| + |A \backslash B|
$$
$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

#### Exemple

Dans une classe de 46 élèves il y a 25 qui étudient la physique et 17 qui étudient les mathématiques, et 3 qui étudient les deux matières.

Combien d'élèves n'étudient aucune matière?

- $E = \{\text{les élèves}\}, |E| = 46$
- $P = \{\text{étudiants de physique}\}, |P| = 25$
- $M = \{\text{étudiants de mathématiques}\}, |M| = 17$
- $|P \cap M| = 3$

$$
|P^{c} \cap M^{c}| = |(P \cup M)^{c}|
$$ 
d'après les lois de morgan
$$
= |E| - |P \cup M|
$$
$$
= |E| - |P| - |M| + |P \cap M| \\
= 7
$$
d'après pointcarré

#### Remarque
- $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$
$$
| \bigcup_{k=1}^{n} A_k | = \sum_{I ⊂ \{1, \cdots, n\} / T \neq \varnothing} (-1)^{k+1} \times | \bigcap_{i ∈ I} A_i|
$$

#### Exercice

Montrer que:
$$
|\bigcap_{i=1}^{n} A_i| = \sum_{I ⊂ \{1, \cdots, n\} / I \neq \varnothing} (-1)^{k+1} \times |\bigcup_{i ∈ I} A_i|
$$

## Applications et ensembles finis

### Utilisation des applications pour calculer le cardinal d'un ensemble

#### Théorème

Soient $E,F$ deux ensembles, et $f:E \to F$  une bijection.
Alors $E$ est fini si et seulement si $F$ est fini  
Et alors $|E| = |F|$ 

#### Preuve

Comme $f$ est bijective, quitte a remplacer $f$ par $f^{-1}$ on prouve les deux sens de l'équivalence par implication simple.

On suppose $E$ fini, et on note $n = |E|$, 
il existe $φ : E \to [[1,n]]$

On considère alors $φ \circ f^{-1}$ une application bijective mettant
$F$ en bojection avec $[[1,n]]$, $F$ est donc fini de cardinal $n$.

#### Exemple

Soit $E / |E| = n ∈ \mathbb{N}$

soit $0 \le k \le n$

On note $\mathcal{A}_k$ l'ensemble des parties de $E$ ayant $k$ éléments.

par définition, $|\mathcal{A}_k| = \binom{n}{k}$.

Soit $φ : \mathcal{A}_k \to \mathcal{A}_{n-k}$
$$
φ : A \mapsto A^{c}
$$

$φ $ est bijective car $ψ : \mathcal{A}_{n-k} \to \mathcal{A}_k$ 
$$
ψ : A \mapsto A^{c}
$$

vérifie: $φ \circ ψ = \text{Id}$

Donc $|\mathcal{A}_{k}| = |\mathcal{A}_{n-k}| \iff \binom{n}{k} = \binom{n}{n-k}$ 

#### Théorème "Le principe des tiroirs"

Soient $E,F$ et
$$
f : E \to F
$$

avec $f$ injective

si F est fini alors $E$ est un ensemble fini et:
$$
|E| \le |F|
$$

#### Remarque

Ce théorème s'appelle "Le principe des tiroirs" et s'utilise aussi sous forme contraposée pour montrer que si $|E| > |F|$ alors $f$ n'est pas injective.

Par exemple, si $F$ est fini et $E$ ne l'est pas alors $f$ n'est pas injective.

- Il s'appelle le principe des tiroirs car si on range $n+1$ chausettes dans $n$ tiroirs, au moins un des tiroirs contient au moins deux chausettes.
- E effet le théorème dit que:
$$
f: \{\text{chausettes}\} \to \{\text{tiroirs}\} \\
\text{chausette} \mapsto \text{tiroir ou elle est rangée}
$$
est injective.

#### Preuve

$f^{|\text{Im}(f)}$ est surjective et comme on la suppose injective, elle est bijective. 

Or $\text{Im}(f) ⊂ F$ et $F$ est fini donc $\text{Im}(f)$ est finie.

et $|\text{Im}(f)| \le |F|$

comme $E$ et $\text{Im}(f)$  sont en bijection, ils possèdent le même cardinal, ainsi:
$$
|E| \le |F|
$$

#### Exemple

Soit un village de 700 habitants, on veut montrer qu'au moins deux personnes ont les mêmes initiales.

On introduit l'application $f$:
$$
f : \{\text{habitants}\} \to \{\text{initiales}\} \\
\text{habitant} \mapsto \text{initiales de cet habitant}
$$ 

On souhaite montrer que $f$ n'est pas injective. 

$|\{\text{habitants}\}| = 700 > 26^2 = |\{\text{initiales}\}|$

donc par le principe des tiroirs, $f$ n'est pas injective.

Donc il existe (au moin\pm deux habitants ayant les mêmes initiales.

#### Rappel

On suppose que $E$ est muni d'une relation d'équivalence $\mathcal{R}$

on note $\overline{x} = \{y ∈ E / x \mathcal{R} y\}$

on note $E/\mathcal{R}$ l'ensemble des classes d'équivalences.

Or $E/\mathcal{R}$ est une partition de $E$, 


plus précisément: 
soient $x,y ∈ E$, si $\overline{x} \cap \overline{y} \neq \varnothing$ alors $\overline{x} = \overline{y}$ et sinon $\overline{x} \cap \overline{y} = \varnothing$


#### Théorème

Soient $E,F$ deux ensembles et $f$
$$
f: E \to F
$$
avec $f$ surjective,

si $E$ est fini alors $F$ l'est aussi et $|F| \le |E|$

#### Lemme

Supposons $E$ fini et muni d'une relation d'équivalence, alors
$$
E/\mathcal{R}
$$ 

est fini et $|E/\mathcal{R}| \le |E|$

#### Preuve

Soit $\overline{x} ∈ E/\mathcal{R}$, comme $\overline{x} \neq \varnothing$
on sait que $∃ c_x ∈ \overline{x}$

On peut donc construire l'application: (par l'axiome du choix)
$$
φ E/\mathcal{R} \to E \\
\overline{x} \to c_x
$$

Soient $\overline{x}, \overline{y} ∈ E/\mathcal{R}$ tel que $φ (\overline{x}) = φ (\overline{y})$

Donc $c_x = c_y$ $c_x ∈ \overline{x}$ et $c_y ∈ \overline{y}$ donc $\overline{x} \cap \overline{y} \neq \varnothing$ donc $\overline{x} = \overline{y}$ et $φ $ est injective

Par le principe des tiroirs, $E/\mathcal{R}$ est fini et $|E/\mathcal{R}| \le |E|$

#### Preuve (du théorème)

Soit $\mathcal{R}$ une relation binaire sur $E$
$$
∀ x,y ∈ E, (x \mathcal{R} y \iff f(x) = f(y))
$$

- $\mathcal{R}$ est reflexive car $∀ x ∈ E,f(x) = f(x) \implies x \mathcal{R} x$

- Soient $x,y,z ∈ E$ avec $x \mathcal{R} y$ et $y \mathcal{R} z$
$$
f(x) = f(y) \text{ et } f(y) = f(z) \implies f(x) = f(z) \implies x \mathcal{R} z
$$
donc elle est transitive

- Soient $x,y ∈ E / x \mathcal{R} y$
$$
f(x) = f(y) \implies f(y) = f(x) \implies y \mathcal{R} x
$$ 
et elle est bien symmétrique.

donc $\mathcal{R}$ est une relation d'équivalence.

On pose:
$$
\overline{f} : E/\mathcal{R} \to F \\
\overline{x} \mapsto f(x)
$$

- Vérifions que $\overline{f}$ est bien définie, c.a.d que pour chaque valeur de $x,y ∈ \overline{x}$  alors $f(x) = f(y)$ et cela est vrai par la définition de la classe d'équivalence.

- Vérifions la surjectivité de $\overline{f}$

soit $y ∈ F$, on sait que $f$ est surjective donc:
$$
∃ x ∈ E / y = f(x)
$$

donc $y = \overline{f}(\overline{x})$

donc $\overline{f}$ est surjective.

- Vérifions l'injectivité
Soient $\overline{x},\overline{y} ∈ E/\mathcal{R}$ tel que $\overline{f}(\overline{x}) = \overline{f}(\overline{y})$
on a:
$$
f(x) = f(y) \iff x \mathcal{R} y \iff \overline{x} = \overline{y}
$$

On a lors $\overline{f}$ une application bijective.
Ainsi $|E/\mathcal{R}| = |F|$ or d'après le lemme, $|E/\mathcal{R}| \le |E|$
donc:
$$
|F| \le |E|
$$

### Utilisation des ensembles finis pour montrer la bijectivité d'une application

#### Théorème

Soit $f : E \to F$

supposons $|E|=|F| < +\infty$

Alors (LASSE "Les assertions suivantes sont équivalents)
1. $f$ est bijective
2. $f$ est injective
3. $f$ est surjective
4. $f$ est inversible a gauche (i.e. $∃ g:F \to E / g \circ f = \text{Id}_E$ )
5. $f$ est inversible a droite

#### Preuve

$1 \implies 2,3,4,5$

Montrons donc que $2,3,4,5 \implies 1$

##### 2 $\implies$ 1

$f^{|\text{Im}(f)}$ est surjective (et injective par $(2)$) donc bijective

donc $|E|= |\text{Im(f)}|$ or $|E| = |F|$ donc $|\text{Im}(f)| = |F|$

or $\text{Im}(f) ⊂ F$ donc $\text{Im}(f) = F$ et $f$ est surjective. (donc bijective)

##### 3 $\implies$ 1

Par l'absurde, suppososn que $f$ soit non-injective
$$
∃ x,y ∈ E / x \neq y \land f(x) = f(y)
$$

F = $f(E) = f(E\backslash \{y\})$ car $f(x) = f(y)$

donc $f_{|E\backslash \{y\}}$ est surjective, donc $|E\backslash\{y\}| \ge |F|$ 

Or $|E\backslash\{y\}| = |E| -1$ donc on a:
$$
|E| - 1 \ge |F|
$$ 

ce qui est absurde car $|E| = |F|$

##### 4 $\implies$ 1
si $(4)$ alors $(2)$ donc $4 \implies 2 \implies 1$

##### 5 $\implies$ 1
si $(5)$ alors $(3)$ donc $5 \implies 3 \implies 1$

