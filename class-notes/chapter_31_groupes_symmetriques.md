# Chapitre 31: Groupe Symmétrique

## Définitions et Premières Propriétés

### Rappels

Si $E$ est un ensemble non vide l;ensemble des bijections de $E$ dans $E$ s'appelle ensemble des permutations noté $S(E)$,

est un groupe pour la loi $\circ$.

En particulier si $E$ est fini de cardinal $n  ∈\mathbb{N}^{*}$, $E$ est en bijection avec $[1,n]$ et on vérifie que le groupe $(S(E), \circ)$ est alors isométrique a $(S([1,n]), \circ)$ noté $(S_n, \circ)$

#### Théorème

$(S_n, \circ)$ est un groupe fini de cardinal $n!$ appelé groupe Symmétrique d'ordre $n$.


On adopte l'écriture suivante dans ce chapitre:

si $σ  ∈S_n$ on représente $σ$ sous la forme:
$$
σ = 
\begin{pmatrix}
    1 & 2 & \cdots & n \\
    σ (1) & σ (2) & \cdots & σ (n)
\end{pmatrix}
$$

#### Exemple

$$
σ =
\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\
    6 & 3 & 2 & 4 & 1 & 5
\end{pmatrix}
$$

Donc
$$
σ ^{-1} =
\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\
    5 & 3 & 2 & 4 & 6 & 1
\end{pmatrix}
$$


$$
σ ^2 =
\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\
    5 & 2 & 3 & 4 & 6 & 1
\end{pmatrix}
$$

#### Remarque
On utilise aussi la notation multiplicative pour la composition.

$$
σ ^{0} - \text{id},  ∀k  ∈ ∈ \mathbb{N}, σ ^{k} = σ \circ σ ^{k-1}, σ ^{-k} = ( σ ^{-1})^{k}
$$

#### Théorème

$(S_n, \circ)$ est abélien si et seulement si $n  ∈\{1,2\}$.

#### Preuve

Si $n = 1$ c'est évident car il n'y a que l'identité: $S_1 = \{\text{id}_{\{1\}}\}$

Si $n = 2$ il n'y a que 2 permutations,  $S_2 = \{ \text{id}_{\{1,2\}}, σ\}$ ou
$$
σ =
\begin{pmatrix} 1 & 2 \\
2 & 1
\end{pmatrix}
$$

Or si $n \ge 3$ on considère

$$
τ =
\begin{pmatrix}
    1 & 2 & 3 & \cdots & n \\
    2 & 1 & 3 & \cdots & n
\end{pmatrix}
$$
et
$$
σ =
\begin{pmatrix}
    1 & 2 & 3 & 4 & \cdots & n \\
    3 & 2 & 1 & 4 & \cdots & n
\end{pmatrix}
$$

$$
τ σ =
\begin{pmatrix}
    1 & \cdots  \\
    3 & \cdots 
\end{pmatrix}
$$
$$
σ τ =
\begin{pmatrix}
    1 & \cdots  \\
    2 & \cdots 
\end{pmatrix}
$$

Donc ils ne commuttent pas.

#### Définition *support d'une permutation*

Soit $σ  ∈S_n$ On appelle supoort de $σ$ noté $\text{supp}( σ )$
l'ensemble:
$$
\text{supp} σ = \{i  ∈[1,n] / σ (i) \neq i\}
$$

#### Exemples

1. Pour $σ  ∈S_n, \text{supp} σ = \varnothing \iff σ = \text{id}$

2. Si
$$
σ =
\begin{pmatrix}
    1 & 2  &3 & 4 & 5 & 6 \\
    6 & 3 & 2 & 4 & 1 & 5
\end{pmatrix}
$$

alors $\text{supp} (σ) = \{1, 2, 3, 5, 6\} = \text{supp} (σ ^{-1})$
et $\text{supp} (σ ^2) = \{1, 5, 6\}$

#### Remarque

Comme $∀i  ∈[1,n]$,

$$
σ (i) = i \implies  ∀k  ∈\mathbb{Z}, σ ^{k}(i) = i
$$

par contrapośee:
$$
\text{supp}( σ ^{k} ) ⊂ \text{supp} ( σ )
$$

#### Théorème

Soient $σ _1, σ _2  ∈S_n$
Si $\text{supp}( σ _1) ∩ \text{supp} ( σ _2) = \varnothing$ alors

1. Elles commuttent
2. $∀ k  ∈\mathbb{Z}, (σ _1 σ _2)^{k} = σ _1 ^{k} σ _2 ^{k}$
3. $\text{supp} ( σ _1 σ _2) = \text{supp} ( σ _1) ∪ \text{supp} ( σ _2)$

#### Preuve

1. Si $i ∉ \text{supp} ( σ _1 ) , \text{supp} ( σ _2)$  alors
$$
(σ _1 σ _2 )(i) = i = ( σ _2 σ _1 ) (i)
$$

Si $i  ∈\text{supp} ( σ _1)$ alors $i ∉ \text{supp} ( σ _2)$ donc
Par injectivité on a que $σ_1(i) \neq i \iff σ _1 (i)  ∉\text{supp} ( σ _2)$

$$
(σ _1 σ _2) (i) = σ _2 (i) = (σ _2 σ _1)(i)
$$


Or $σ _1, σ _2$ jouent des roles symmétriques donc quitte a les échanger on a la propriété dans tous les cas ou l'intersection des supports et vide.

2. On procède par récurrence sur $k$

3. Par les lois de Morgan on démontre que $\overline{\text{supp}( σ _1 σ _2)} = \overline{\text{supp}( σ _1)} ∩ \overline{\text{supp}( σ _2)}$

    1. si $i ∈ \overline{\text{supp} ( σ _1)} ∩ \overline{\text{supp} ( σ _2)}$

alors $σ _1(i) = i  = σ _2(i) \implies σ _1 σ _2 (i) = i  ∈ \overline{\text{supp} ( σ _1 σ _2)}$

Désormais on suppose $n \ge 2$.

#### Définitions

1. Soient $p  ∈[2,n]$ et $a_1, \cdots, a_p$ $p$ entiers distincts dans $[1,n]$

On pose $∀ i ∈ [1, p-1], c(a_i) = a_{i+1}, c(a_p) = a_1$ et $∀x  ∈[1,p] \backslash \{a_1, \cdots, a_p\}, c(x) = x$

$$
c =
\begin{pmatrix}
    1 & \cdots & a_1 & \cdots & a_p & \cdots & n \\
    1 & \cdots & a_2 & \cdots & a_1 & \cdots & n
\end{pmatrix}
$$

$c$ est un cycle de longeur $p$ ou $p-$cycle, on le noteras $c=\begin{pmatrix} a_1 & a_2 & \cdots & a_p\end{pmatrix}$

2. Un 2-cycle s'appelle une transposition.

#### Exemples

1. Dans $S_7$ le 5-cycle
$$
c =
\begin{pmatrix}
    1 & 3 & 4 & 7 & 6
\end{pmatrix}
$$

représente la permutation:
$$
\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 \\
    3 & 2 & 4 & 7 & 5 & 1 & 6
\end{pmatrix}
$$

on a aussi $c = \begin{pmatrix} 4 & 7 & 6 & 1 & 3 \end{pmatrix}$

(il y a $5$ écritures possibles)

2. Dans $S_4$ la transposition $τ = (2 \text{ } 4)$ représente la permutation:

$$
\begin{pmatrix}
    1 & 2 & 3 & 4 \\
    1 & 4 & 3 & 2
\end{pmatrix}
$$

#### Remarque

1. Si $i \neq j$, la transposition $(i \text{ }j)$ s'écrit aussi $(j\text{ }i)$ Mais on privilégieras l'écriture $(i \text{ } j)$ si $i < j$
2. toute transposition est une involution avec $τ ^2 = \text{id}$

#### Théorème

Soit $c$ un $p-$cycle de $S_n$ avec $c = \begin{pmatrix} a_1 & \cdots & a_p\end{pmatrix}$

1. $\text{supp} (c) = \{a_1, \cdots, a_p\}$

2. $c^{-1} = \begin{pmatrix} a_p & a_{p-1} & \cdots & a_1\end{pmatrix}$
3. $c^{p} = \text{id} \iff c^{-1} = c^{p-1}$

#### Preuve

1. Immédiat

2. Comme $∀i  ∈[1,p], c(a_i) = a_{i+1} \implies c^{-1}(a_{i+1}) = a_i$ ( par convention $a_{p+1} = a_1$.

Ainsi $∀i ∈[1,p], c^{-1}(a_i) = a_{i-1}$ d'ou (2).

3. Par récurrence on a

$$
∀ k  ∈[1,p-1], c^{k}(a_1) = a_{k+1}, c^{p}(a_1) = c(a_p) = a_1
$$

$$
 ∀k  ∈[2,p], c^{p}(a_k) = c^{p} (c^{k-1} (a_1)) = c^{p+k-1} (a_1) = c^{k-1} ( c^{p} (a_1)) = c^{k-1} (a_1) = a_{k-1 + 1}= a_k
$$

De plus $∀ x  ∈\overline{\text{supp}}(c), c(x) = x \implies c^{p}(x) = x$

Ainsi $c^{p}_{|\text{supp}} = \text{id}$ et $∀k, c^{k}_{|\overline{\text{supp}}} = \text{id}$

Ainsi

$$
c^{p} = \text{id}
$$

De plus $c^{p} = c^{p-1} c = c c ^{p-1}= \text{id} \iff c^{-1} = c^{p-1}$ par le théorème de la bijection.

## Décomposition d'une permutation

#### Théorème

Toute permutation est produit de transpositions

$$
∀ σ  ∈S_n, ∃ τ _1, \cdots, τ _p  ∈S_n / ∃ (a_1, b_1), \cdots, (a_p, b_p) ∈\mathbb{K}^2 /  ∀i ∈[1,p], τ _i = (a_i \text{ } b_i)
$$
$$
σ = \prod_{k=1}^{p} τ _k
$$

#### Preuve

On raisonne par récurrence sur $n ∈ \mathbb{N}$ et $n \ge 2$

##### Initialisation

Si $n =2$, $S_2 = \{\text{id}, τ = (1 \text{ } 2)\}$

or $\text{id} = τ \times τ, τ = τ$ donc toute permutation de $S_2$ est produit de transpositions.

##### Hérédité

On suppose le résultat vrai pour un rang $n \ge 2$ fixé

Soit $σ  ∈S_{n+1}$

1er cas:

si $σ (n+1) = n+1$, $σ$ induit une permutation de $[1,n]$ qui se décompose donc par hypothèse en produit de transpositions.

2e cas:

si $σ (n+1) \neq n+1$ on pose $τ = (σ (n+1) \text{ } n+1)$

et $τ σ (n+1) = n+1$ et on revient au cas précédent, donc il existe $τ _1, \cdots, τ _m$, $m$ transpositions telles que

$$
σ ' = \prod_{k=1}^{m} τ _k = τ σ 
$$

D'ou $σ = τ ^{-1} σ ^{-1} = τ σ ^{-1} = τ \times  \prod_{k=1}^{m} τ _k$

Cas particulier:

si $c = (a_1 \text{ } \cdots \text{ } a_p)$on vérifie facilement que

$c = (a_1 \text{ } a_2)(a_2\text{ }a_3)\cdots(a_{p-1} \text{ } a_p)$

Donc tout $p-$cycle peut se décomposer en un produit de $p-1$ transpositions.

#### Théorème

Toute permutation s'écrit comme produit de cycles a supports disjoints et cette décomposition est unique a l'ordre des facteurs près. Et ces facteurs commuttent deux-a-deux.

#### Preuve

(non-exigible, voir polycopié)

#### Exemple

Soit $σ  ∈S_{10}$

$$
σ =
\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
    3 & 2 & 1 & 7 & 6 & 10 & 4 & 9 & 5 & 8
\end{pmatrix}
$$

$$
σ = \begin{pmatrix}1 &  3\end{pmatrix}\begin{pmatrix}4 & 7\end{pmatrix}\begin{pmatrix}5 &  6 & 10 &  8 &  9\end{pmatrix}
$$

#### Remarque

Soit $σ  ∈S_n / σ = c_1 c_2 \cdots c_m$ avec les $c_i$ des cycles a supports disjoints.

Comme les $c_i$ commuttent,

$$
 ∀k  ∈\mathbb{Z}, σ ^{k} = \prod_{i=1}^{m} c_i^{k}
$$

## Signature d'une permutation et groupes alterné

#### Définition *inversion*

Soit $σ  ∈S_n$ et un couple $(i,j) / 0 \le i < j \le n$

On dit que $σ$ réalise une inversion sur $(i\text{   }j)$ si $σ (i) > σ (j)$

On note $I( σ )$ le nombre de couples pour lesquels $σ$ réalise une inversion.

$$
I ( σ ) = \text{card }\{(i,j) ∈[1,n] / i < j \text{ et } σ ( i ) > σ (j)\}
$$

#### Exemples

1. Dans $S_4$ 
$$
σ =
\begin{pmatrix}
    1 & 2 & 3 & 4 \\
    2 & 4 & 3 & 1
\end{pmatrix}
$$

$I ( σ ) = \text{card } \{(1,4), (2,3), (2,4), (3,4)\} = 4$

2. Dans $S_n$

$$
σ' =
\begin{pmatrix}
    1 & 2 & \cdots & n \\
    n & n-1 & \cdots & 1
\end{pmatrix}
$$

On remarque que compter le combre d'inversions de $σ$ revient a dénombrer pour chaque terme de la seconde ligne, les entiers qui le suivent et lui sont inférieurs.

Ainsi

$$
I ( σ ) = n-1 + n-2 + \cdots + 1 = \frac{n(n-1)}{2}
$$

#### Définition *signature*

Si $σ  ∈S_n$ on appelle signature de $σ$ le nombre $ε ( σ )$ défini par: 
$$
ε ( σ ) = (-1)^{I ( σ )}
$$

#### Exemple

La signature du $σ$ de l'exemple précédent, $ε ( σ ) = (-1)^{4} = 1$

et $ε ( σ ' ) = (-1)^{\frac{n(n-1)}{2}}$

#### Théorème

La signature d'une transposition vaut -1.

#### Preuve

Soient $i,j  ∈[1,n] / 1 \le i < j \le n, τ  ∈S_n / τ = (i \text{   } j)$
$$
τ =
\begin{pmatrix}
    1 & \cdots & i & \cdots & j & \cdots & n \\
    1 & \cdots & j & \cdots & i & \cdots & n
\end{pmatrix}
$$

$$
I( τ ) = 0_{1} + 0_{2} + \cdots + 0_{i-1} + (j-i)_{j} + 1_{i+1} + \cdots + 1_{j-1} + 0_{i} + \cdots + 0_{n}
$$

$$
I ( τ ) = (j - i) + (j-1) - (i+1) + 1 = 2(j-i) + 1
$$

Donc $ε ( τ ) = (-1)^{I( τ ) } = (-1)^{2(j-i) + 1} = (-1)^{1} = -1$

#### Théorème

$$
 ∀σ , σ ' ∈S_n, ε ( σ σ ') = ε ( σ ) \times ε ( σ ')
$$

Ainsi $ε$ est un morphisme du groupe $(S_n, \circ)$ dans $(\mathbb{Z}^{*}, \times )$

#### Preuve

On pose

$$
A = \{ (i,j) ∈[1,n]^2 / i < j\}
$$

$$
A_1 = \{ (i,j)  ∈A / σ '(i) < σ '(j) \text{ et } σ σ ' (i) < σ σ ' (j)\}
$$

$$
A_2 = \{ (i,j)  ∈A / σ '(i) < σ '(j) \text{ et } σ σ ' (i) > σ σ ' (j)\}
$$
$$
A_3 = \{ (i,j)  ∈A / σ '(i) > σ '(j) \text{ et } σ σ ' (i) < σ σ ' (j)\}
$$

$$
A_4 = \{ (i,j)  ∈A / σ '(i) > σ '(j) \text{ et } σ σ ' (i) > σ σ ' (j)\}
$$

On pose $∀ k  ∈[1,4], n_k = |A_k|$

Il est clair que $A = \bigcup_{k=1}^{4} A_k$ et

$$
 ∀k, l  ∈\{1,2,3,4\}, k \neq l \implies A_k ∩ A_l = \varnothing 
$$

On a:

$$
I ( σ ') = n_3 + n_4, I ( σ σ ') = n_2 + n_4
$$

Soit $f : A_2 \to A$

$$
f : (i,j) \mapsto ( σ '(i), σ '(j))
$$

et $g : A_3 \to A$

$$
g : (i,j) \mapsto ( σ '(j), σ '(i))
$$

Comme $σ '$ est bijective, $f,g$ sont injectives,

Donc $|f(A_2)| = |A_2| = n_2$ et $|g(A_3)| = |A_3| = n_3$

Or $f(A_2) = \{ (k,l)  ∈A / ∃ (i,j)  ∈A_2, (k,l) = ( σ '(i), σ '(j))\}$

$$
f = \{ (k,l)  ∈A / ∃ (i,j)  ∈A / k = σ '(i), l = σ ' (j) \text{ et } σ (k) > σ (l)\}
$$

$$
= \{ (k,l)  ∈A  / σ^{-1'}(k) < σ^{-1'}(l) \text{ et } σ (k) > σ (l)\}
$$

De même
$$
g(A_3) = \{ (k,l)  ∈A / σ^{-1'} (k) > σ^{-1'}(l) \text{ et } σ (k) > σ (l) \}
$$

et $I ( σ ) = n_2  + n_3$ 

Donc

$$
ε ( σ σ ') = (-1)^{ n_2 + n_4} = (-1)^{n_2+ n_4 + 2n_3} = ε ( σ ) \times ε ( σ ')
$$

#### Corollaire

L'application signature est l'unique morphisme de groupe $(S_n, \circ)$ sur $(\mathbb{Z}^{*}, \times)$ pour lequel toutes les transpositions ont pour image $-1$.

#### Preuve

Par les théorèmes précédents, $ε$ est un morphisme du groupe $(S_n, \circ)$ sur le groupe $(\mathbb{Z}^{*}, \times )$ tel que pour toute transposition $ τ,ε ( τ ) = -1$.

De plus si $φ$ vérifie ces propriétés, si $σ  ∈S_n$, $σ = τ _1 \cdots τ _m$ avec les $τ _i$ des transpositions. Donc $φ ( σ ) =(-1)^{m} = ε ( σ )$.

Donc $φ = ε$ et l'unicité.

#### Corollaire

Si $c$ est un $p-$cycle, alors $ε (c) = (-1)^{p-1}$

#### Preuve

Si $c = (a_1 \text{   } a_p)$ on a $c = \prod_{k=1}^{p-1} (a_k \text{ } a_{k+1})$

Donc
$$
ε ( c) = ε \left( \prod_{k=1}^{p-1} ( a_k \text{ } a_{k+1})\right)
$$

$$
ε ( c) = \prod_{k=1}^{p-1} ε ( a_k \text{ } a_{k+1})
$$

$$
ε (c) = (-1)^{p-1}
$$

#### Remarques

1. Si $σ  ∈S_n$, en décomposant $σ$ en produit de cycles a supports disjoints, ou en produit de transpositions, on peut déduire sa signature.

2. La décomposition d'une permutation en produit de transpositions n'est pas unique, mais la parité qui la forme est inchangée.


#### Définition *parité*

On dit que $σ ∈S_n$ est paire si sa signature vaut 1, sinon elle est impaire.

L'ensemble des permutations paires de $S_n$ se note $\mathcal{A}_n$

#### Théorème

$\mathcal{A}_n$ est un sous-groupe de $(S_n, \circ)$ de cardinal $\frac{n!}{2}$ que l'on appelle le groupe alterné d'ordre $n$.

#### Preuve

$ε : (S_n, \circ) \to (\mathbb{Z}^{*}, \times )$ est un morphisme de groupes.

Par théorème, $\ker ε = \{ σ  ∈S_n / ε ( σ ) = 1\} = \mathcal{A}_n$ est un sous-groupe de $S_n$.

De plus si $τ$ est une transposition, l'application:

$$
φ : \mathcal{A}_n \to \mathcal{I}_n
$$

$$
φ : σ \mapsto τ σ 
$$

ou $\mathcal{I}_n = \{ σ  ∈S_n / ε ( σ ) = -1\}$

Est bijective, donc $|\mathcal{A}_n| = |\mathcal{I}_n|$ et $S_n = \mathcal{A}_n ∪\mathcal{I}_n$

Donc $|S_n| = 2|\mathcal{A}_n| \implies |\mathcal{A}_n| = \frac{n!}{2}$ 
