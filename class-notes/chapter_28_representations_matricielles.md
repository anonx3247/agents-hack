# Chapitre 28: Représentations Matricielles

## Retour sur les matrices

### Noyau et image d'une matrice

#### Définition *noyau et image d'une matrice*

Soit $A  ∈M_{n,p}(\mathbb{K})$

On appelle noyeau de $A$,
$$
\text{ker}(A) = \{X  ∈M_{p,1}(\mathbb{K}) / AX = 0_{n,1}\}
$$

Et image de $A$,
$$
\text{im}(A) = \{AX / X ∈M_{n,1}(\mathbb{K})\}
$$


### Théorème d'inversibilité

#### Théorème "Théorème d'Inversibilité"

Soit $A  ∈M_n(\mathbb{K})$

LASSE

1. $A$ est inversible
2. $A$ est inversible a droite
3. $\text{im}(A) = M_{n,1}(\mathbb{K})$
4. $A$ est inversible a gauche
5. $\text{ker}(A) = \{0_{n,1}\}$

#### Preuve

1 $\implies$ 2

1 $\implies$ 4

2 $\implies$ 3

Car $\text{im}(A)  ⊂M_{n,1}(\mathbb{K})$
Soit $Y  ∈M_{n,1}(\mathbb{K}), Y = T_n \times Y = A \times C \times Y = A(CY)  ∈\text{im}(A)$

4 $\implies$ 5

$\{0\}  ⊂\text{ker}(A)$

Soit $X ∈ \text{Ker}(A), X = I_n \times X = B \times A \times X = B(AX) = B(0) = 0$

3 $\implies$ 1

On pose $φ : M_n(\mathbb{K}) \to M_n(\mathbb{K})$:
$$
M \mapsto MA
$$

$φ$ est linéaire

Soit $M  ∈\text{ker}(φ )$

Donc $MA = 0$

Soit $X  ∈M_{n,1}(\mathbb{K})$

comme $\text{im}(A) = M_{n,1}(\mathbb{K}), X  ∈\text{im}(A)$

Et $∃ Y  / X = AY$

$$
MX = MAY
$$
$$
= 0_{n,1}Y
$$
$$
= 0_{n} X
$$

et $MX = 0_nX$

Donc $∀ X  ∈M_{n,1}(\mathbb{K}), MX = 0_nX$

Et par l'identification matricielle, $M = 0_n$

Ainsi $φ$ est injective, et $\text{dim}(M_n(\mathbb{K})) = n^2$ donc par le théorème d'isomorphismes, $φ$ est un automorphisme.

Ainsi $I_n  ∈\text{im}(φ )$

donc il existe $B  ∈M_n(\mathbb{K}) / I_n = φ (B) = BA$

On pose $ψ : M_n(\mathbb{K}) \to M_n(\mathbb{K})$

$$
ψ : M \mapsto AM
$$

$ψ$ est linéaire

Soit $M  ∈\text{ker}(ψ )$

Donc $AM = 0_n$ et $M  =I_n M$

Donc $M = BAM = B(AM) = B0 = 0$

Ainsi $\text{ker}( ψ ) = \{0\}$ et $ψ$ est injective,

de même elle est un automorphisme, Ainsi $I_n$ possède un antécédent, $C$ par $ψ$.

Ainsi $ψ (C) = AC$

$$
B = B I_n = BAC = I_n C = C
$$

Ainsi $A$ est inversible.

5 $\implies$ 1

Similaire a ce qui précède en considérant d'abords $ψ$ et en suite $φ$ (A essayer a faire)

### Retour sur l'inversibilité des matrices triangulaires

#### Théorème

Soit $A = (a_{i,j})  ∈T_n^{+}(\mathbb{K})$

$A  ∈GL_n(\mathbb{K}) \iff  ∀1 \le i \le n, a_{i,i} \neq 0$

#### Preuve

$\impliedby$ idem que dans le chapitre sur les matrices

$\implies$

On pose $φ : T_n^{+}(\mathbb{K}) \to T_n^{+}(\mathbb{K})$
$$
M \mapsto AM
$$

$φ$ est bien définie car $T_n^{+}$ est stable par produit

$φ$ est linéaire

Montrons que $φ$ est injective

Soit $M  ∈\text{ker}( φ )$

Ainsi $AM = 0_n$

$$
A^{-1} A M = A^{-1}0_n 
$$
$$
M = A^{-1} 0_n = 0_n
$$

$φ$ est injective et $\text{dim}(T_n^{+}(\mathbb{K})) = \frac{n(n+1)}{2} < +\infty$ donc $φ$ est un automorphisme.

Ainsi $I_n$ possède un antécédent noté $B  ∈T_n^{+}(K)$

Ainsi $φ (B) = I_n = BA \iff B = A^{-1}$

On note $A^{-1} = (b_{i,j})$ et

$∀ 1 \le i \le n, a_{i,i} b_{i,i} = 1 \iff a_{i,i} \neq 0$

#### Exercice

Montrer que si $A$ est inversible et centro-symmétrique,
alors $A^{-1}$ est aussi centro-symmétrique.

## Représentations Matricielles

### Matrices colonnes des composantes d'un vecteur

#### Rappel

Soit $E$ un $\mathbb{K}-$ev de dimension finie $n  ∈\mathbb{N}^{*}$ muni d
une base $\mathcal{B} = (e_1, \cdots, e_n)$

$$
∀ x  ∈E, ∃ ! ( λ _1, \cdots, λ _n)  ∈\mathbb{K}^{n} / x = \sum_{i=1}^{n} λ _i e_i
$$

#### Définition *Matrice des composantes d'un vecteur*

On appelle matrice des composantes d'un vecteur $x$ dans la base $\mathcal{B}$ la matrice colonne des composantes du vecteur $x$ dans la base $\mathcal{B}$.

On note:

$$
\text{Mat}_{\mathcal{B}}(x) =
\begin{pmatrix}
λ 1 \\ \vdots \\ λ _n
\end{pmatrix}
$$

#### Remarque

Les composantes se $x$ dépendent de la base

#### Théorème

L'application $\text{Mat}_{\mathcal{B}}$:
$$
x \mapsto \text{Mat}_{\mathcal{B}}(x)
$$

est un isomorphisme.

#### Preuve

Soient $x, y  ∈E$ et $μ  ∈\mathbb{K}$

$$
∃ ( a_1, \cdots, a_n) / x = \sum a_i e_i
$$
$$
∃ ( b_1, \cdots, b_n) / y = \sum b_i e_i
$$

Alors $x + μ y = \sum (a_i + μ b_i)$

Donc $\text{Mat}_{\mathcal{B}}( x + μ y) =$


$$
\begin{pmatrix}
    a_1 + μ b_1 \\
    \vdots \\
    a_n + μ b_n
\end{pmatrix} =
$$

$$
\begin{pmatrix}
    a_1 \\
    \vdots \\
    a_n
\end{pmatrix}
+
μ 
\begin{pmatrix}
    b_1 \\
    \vdots \\
    b_n
\end{pmatrix}
$$
$$
= \text{Mat}_{\mathcal{B}}(x) + μ \text{Mat}_{\mathcal{B}}(y)
$$


donc $\text{Mat}_{\mathcal{B}}$ est linéaire.

Elle est injective donc un automorphisme.

### Matrices composantes d'une famille de vecteurs

Soit $\mathcal{F} = (x_1, \cdots, x_p)$ dans un ev $E$ de base $e_1, \cdots, e_n)$

On note $C_j$ la $j-$eme colonne formée des composantes du vecteur $x_j$

#### Définition *Matrice des composantes dans la base*

On appelle matrice des composantes dans une base de'une famille

La matrice de $M_{n,p}(\mathbb{K})$ dont les colonnes sont les $C_1, \cdots, C_p)$

Ici $C_i = \text{Mat}(x_i)$

### Matrice d'une application linéaire

Soient $E, F$ des ev de dimension respectives $p,n$ muni des bases $\mathcal{E} = (e_1, \cdots, ep)$ et $\mathcal{F} = (f_1, \cdots, f_n)$

#### Définition *Matrice d'une application linéaire*

On appelle matrice représentative dans les bases $\mathcal{E}, \mathcal{F}$ d'une application linéaire $u  ∈\mathcal{L}(E,F)$

la matrice des composantes dans la base $\mathcal{F}$ de la famille de vecteurs $u(e_1), \cdots, u(e_p)$ On note:

$$
\text{Mat}_{\mathcal{E}, \mathcal{F}} (u) = \text{Mat}_{\mathcal{F}} (u(e_1), \cdots, u(e_p))
$$

#### Exemple

$u : \mathbb{R}^3 \to \mathbb{R}^{4}$

$$
u : (x,y,z) \mapsto (x+y, x+z, y+z, x - y - z)
$$

Dans les bases canoniques:

$$
\text{Mat}(u) =
\begin{pmatrix}
    1 & 1 & 0 \\
    1 & 0 & 1 \\
    0 & 1 & 1 \\
    1 & -1 & -1
\end{pmatrix}
$$

### Matrices d'un endomorphisme

Soit $E$ un ev de dimension finie $n  ∈\mathbb{N}^{*}$ muni d'une base $B = (e_1, \cdots, e_n)$

#### Définition *Matrice représentative d'un endomorphisme*

On appelle matrice représentative d'un endomorphisme $u  ∈\mathcal{L}(E)$ dans la base $B$ la matrice dans la base $B$ au départ et a l'arivée de l'application linéaire $u$

$$
\text{Mat}_B(u)
$$

#### Exemples

$$
\text{Mat}_B(\text{id}) = I_n
$$

Pour l'endomorphisme $u  ∈\mathcal{L}(M_2(\mathbb{R}))$ 
$$
u : M \mapsto M^{\top} + 4M
$$

Avec la base $B$ canonique.

$$
\text{Mat}(u) =
\begin{pmatrix}
    5 & 0 & 0 & 0 \\
    0 & 4 & 1 & 0 \\
    0 & 1 & 4 & 0 \\
    0 & 0 & 0 & 5
\end{pmatrix}
$$

## Application du calcul matriciel aux applications linéaires

On considère $E,F$ deux $\mathbb{K}-$ev munis de bases $\mathcal{E} = (e_1, \cdots, e_p)$ et $\mathcal{F} = (f_1, \cdots, f_n)$.

Pour $x  ∈E, y  ∈F, X = \text{Mat}_{\mathcal{E}}(x), Y = \text{Mat}_{\mathcal{F}}(y)$

#### Théorème

"Pourquoi le produit matricielle a-t-il été défini ainsi?"

Soit $u  ∈\mathcal{L}(E,F)$ on note $A = \text{Mat}_{\mathcal{E}, \mathcal{F}}(u)$

$$
 ∀x ∈E,  ∀y  ∈F, (y = u(x) \iff Y = AX
$$

De plus $A$ est l;unique matrice vériviant cette propriété.

On a donc:
$$
\text{Mat}_{\mathcal{F}}(u(x)) = \text{Mat}_{\mathcal{E}, \mathcal{F}}(u) \times \text{Mat}_{\mathcal{E}(x)}
$$

#### Preuve

Unicité:

Soit $A, A'$ deux candidates solutions du problème.

Soit $X$ une matrice colonne de taille $p$

comme $\text{Mat}$ est un isomorphisme, alors $∃ x  ∈E / X = \text{Mat}(x)$

On pose $Y = \text{Mat}(u(x))$

Ainsi $Y = AX = A'X$ et par identification matricielle, $A = A'$

Convenance:

Soient $x ∈E, y  ∈F$

$x = \sum _{j=1}^{p} x_j e_j$ et $y = \sum_{i=1}^{n} y_i f_i$

$$
u(x) = \sum_{j=1}^{p} x_ju(e_j)
$$

$$
A = (a_{i,j})
$$

$$
u(e_j) = \sum_{i=1}^{n} a_{i,j} f_i
$$

$$
u(x) = \sum_{j=1}^{p} x_j \sum_{i=1}^{n} a_{i,j} f_i 
$$

$$
= \sum_{i=1}^{n} \left(\sum_{j=1}^{p} x_j a_{i,j}\right) f_i
$$

$$
y = u(x) \iff \sum_{i=1}^{n} y_i f_i = \sum_{i=1}^{n} \left( \sum_{j=1}^{p} x_j a_{i,j} \right) f_i
$$

Par identification (car $(f_i)$ est libre) on a:
$$
y_i = \sum_{j=1}^{p} x_j a_{i,j}
$$

$$
\iff Y_i = (AX)_i
$$
$$
Y = AX
$$

#### Exercice

Soit $u$ un endomorphisme de $E$ un ev muni d'une base $\mathcal{B} = (e_1, \cdots e_3)$

tel que $\text{Mat}_{\mathcal{B}}(u) =$

$$
\begin{pmatrix}
    1 & 1 & 2 \\
    1 & -1 & 0 \\
    1 & 0 & 1
\end{pmatrix}
$$

1. Donner $u(x)$ pour $x  ∈E$
2. calculer $\text{ker}(u)$
3. calculer $\text{im}(u)$

### L'isomorphisme de représentation matricielle

Soient $E,F$ des ev de bases $\mathcal{B} = (e_1, \cdots, e_p)$ et $\mathcal{C} = (f_1, \cdots, f_n)$

#### Théorème

L'application $φ : \mathcal{L}(E,F) \to M_{n,p}(\mathbb{K})$

$$
u \mapsto \text{Mat}_{\mathcal{B}, \mathcal{C}}(u)
$$

#### Preuve

Soient $u,v  ∈\mathcal{L}(E,F)$ et $λ  ∈\mathbb{K}$

$$
 ∀x  ∈E, (λ u + v) (x) = λ u(x) + v(x)
$$

$$
\text{Mat}(( λ u + v)(x)) = λ \text{Mat}(u(x)) + \text{Mat}(v(x))
$$

$$
 =(λ \text{Mat}(u) + \text{Mat}(v)) \times \text{Mat}(x)
$$

Ainsi
$$
\text{Mat}( λ u + v) \times \text{Mat}(x) = ( λ \text{Mat}(u) + \text{Mat}(v)) \times \text{Mat}(x)
$$

Par identification matricielle, et le fait que $\text{Mat}$ est un isomorphisme pour les vecteurs, il est surjectif et donc l'égalité est vraie pour toutes les matrices colonnes.

Puis
$$
\text{Mat}( λ u + v) = ( λ \text{Mat}(u) + \text{Mat}(v))
$$

Soit $u ∈ \text{ker}( φ )$

$\text{Mat}(u) = 0$

Donc $\text{Mat}(u(x)) = \text{Mat}(u) \times \text{Mat}(x) = 0$

Et $u(x) = 0$ car $u(x) ∈\text{ker}(\text{Mat})$ et elle est un isomorphisme et donc $\text{ker} = \{0\}$

$\text{dim}(\mathcal{L}(E,F)) = \text{dim}(M_{n,p}(\mathbb{K}))$

Donc par le théorème d'isomorphismes, $\text{Mat}$ en est un pour les applications linéaires.

#### Remarques

Soit $A  ∈M_{n,p}(\mathbb{K})$

On muni $\mathbb{K}^{p}, \mathbb{K}^{n}$ de leurs bases canoniques, notées $B_p, B_n$

Alors $A$ admet par $φ$ un unique antécédent,

c'est a dire

$$
∃ ! u  ∈\mathcal{L}(\mathbb{K}^{p}, \mathbb{K}^{n}) / \text{Mat}_{B_p, B_n} (u) = A
$$

$u$ s'appelle l'application linéaire canoniquement associée a $A$.

Soit $A  ∈M_n(\mathbb{K})$

On muni $\mathbb{K}^{n}$ de sa base canonique, notées $B$

Alors $A$ admet par $φ$ un unique antécédent,

c'est a dire

$$
∃ ! u  ∈\mathcal{L}(\mathbb{K}^{n}) / \text{Mat}_{B} (u) = A
$$

$u$ s'appelle l'endomorphisme canoniquement associée a $A$.

### Composition d'applications linéaires

Soient $E,F,G$ trois ev muni de bases $\mathcal{E}, \mathcal{F}, \mathcal{G}$

#### Théorème

Soient $u  ∈\mathcal{L}(E,F), v ∈ \mathcal{L}(F,G)$

Alors $\text{Mat}(v \circ u) = \text{Mat}(v) \times \text{Mat}(u)$

#### Preuve

Soit $x  ∈E$

$$
v \circ u (x) = v(u(x))
$$

$$
\text{Mat}(v \circ u) \times \text{Mat}(x) = \text{Mat}(v(u(x)) \times \text{Mat}(x)
$$

$$
= \text{Mat}(v) \times \text{Mat}(u) \times \text{Mat}(x)
$$

De manière analogue, avec le lemme d'indentification matricielle, et la surjectivité de $\text{Mat}$ on peut identifier:
$$
\text{Mat}(v \circ u)
$$
a
$$
\text{Mat}(v) \times \text{Mat}(u)
$$

#### Corollaire

L'application $\text{Mat}$ pour les endomorphismes

est un isomorphisme d'anneaux (et d'algèbres) pour les lois $\circ \to \times$

#### Corollaire

$∀n  ∈\mathbb{N}, ∀u  ∈\mathcal{L}(E), \text{Mat}(u^{n}) = \text{Mat}^{n}(u)$

#### Exemple

Soit $u in \mathcal{L}(E)$ et $B$ une base de $E$.

Notons $A = \text{Mat}(u)$

$u$ est nilpotente si et seulement si, $A$  l'est.

$u$ est une projection vectorielle si et seulement si, $A$ est idempotente.

$u$ est une symmétrie vectorielle si et seulement si, $A^2 = \text{Id}$

### Isomorphisme et matrice inversible

#### Théorème

Soient $E,F$ deux ev de même dimension $n  ∈\mathbb{N}$ , et $u  ∈\mathcal{L}(E,F)$

$$
u  ∈\text{isom}(E,F) \iff \text{Mat}(u)  ∈GL_n(\mathbb{K})
$$

#### Preuve

$\implies$  $u \circ u^{-1} = \text{id}_F$

Donc $\text{Mat}(\text{id}_F) = I_n$

$$
= \text{Mat}(u) \times \text{Mat}(u^{-1})
$$

et $\text{Mat}(u)$ est inversible

$\impliedby$

$\text{Mat}(u)  ∈GL_n(\mathbb{K}), ∃ B / \text{Mat}(u) \times B = I_n$

or $\text{Mat}$ est un isomorphisme donc $∃ v ∈\mathcal{L}(E,F) / \text{Mat}(v) = B$

Ainsi $u \circ v = \text{id} \iff  v = u^{-1}$

Par le théorème d'isomorphismes, $u$ en est un

#### Corollaire

Soit $E$ un ev de dimension $n$

Soit $u  ∈\mathcal{L}(E)$

$$
u  ∈GL(E) \iff \text{Mat}(u) ∈GL_n(\mathbb{K})
$$

Et dans ce cas, $\text{Mat}(u^{-1}) = \text{Mat}^{-1}(u)$

#### Exercice Bonus

Considérons l'application $\top$

A quoi est égal la matrice de $\top$ dans une base adaptée a la supplémentarité de $S_n$ et $A_n$ dans $M_n$

### Tableau des correspondances

$E, F / \text{dim}(E) = p, \text{dim}(F) = n$ 

| Espaces Vectoriels     | Matrices                       |
|------------------------|--------------------------------|
| vecteur                | matrice colonne                |
| $x  ∈E$                | $X  ∈M_{p,1}(\mathbb{K})$      |
| 0                      | 0                              |
| $λ x + μ y$            | $λ X + μ Y$                    |
| application linéaire   | matrice réctangulaire          |
| $u  ∈\mathcal{L}(E,F)$ | $A ∈M_{n,p}(\mathbb{K})$       |
| $y = u(x)$             | $Y = AX$                       |
| $λ u + μ v$            | $λ A + μ B$                    |
| $v \circ u$            | $BA$                           |
| isomorphisme           | $A$ est inversible             |
| endomorphisme          | matrice carée                  |
| $u  ∈\mathcal{L}(E)$   | $A  ∈M_n(\mathbb{K})$          |
| $\text{id}$            | $I_p$                          |
| $u^{m}$                | $A^{m}$                        |
| $u  ∈GL(E), u^{-1}$    | $A  ∈GL_p(\mathbb{K}), A^{-1}$ |
| forme linéaire         | matrice ligne                  |
| $φ ∈E^{*}$             | $L  ∈M_{1,p}(\mathbb{K})$      |
| $φ (x)$                | $LX$                           |


### Différentes représentations d'un endomorphisme

Soient $E$ de dimension $n$, et $F,G$ deux sev de $E$ supplémentaires de dimensions $r$ et $n-r$

#### Matrice d'une homothétie vectorielle

#### Théorème

Dans toute base $B$ de $E$, la matrice de l'homothétie vectorielle de rapport $λ$ est $λ I_n$

#### Preuve

$$
\text{Mat}(λ \text{Id}) = λ \text{Mat}(Id) = λ I_n
$$

#### Matrice d'une projection vectorielle

#### Théorème

La matrice de la projection vecotirlle $p$ sur $F$ parallellement a $G$ dans une base adaptée a la supplémentarité $E = F \oplus G$ est
$$
\left(
\begin{matrix}
\text{id} & 0 \\
0 & 0
\end{matrix}
\right)
$$

#### Preuve

$p_{|F} = \text{id}, p_{|G} = 0$

$$
\text{Mat}(p) = \left(
\begin{matrix}
\text{id} & 0 \\
0  & 0
\end{matrix}
\right)
$$

#### Matrice d'une symmétrie vectorielle

#### Théorème

La matrice d'une symmétrie vectorielle $s$ par rapport a $F$ parallellement a $G$, dans une base $B$ adaptée a la supplémentarité $E = F \oplus G$ est

$$
\left(
\begin{matrix}
I_r & 0 \\
0 & -I_{n-r}
\end{matrix}
\right)
$$

## Formules de changement de bases

### Matrice de passage

#### Définition *Matrice de passage*

Soit $E$ un $\mathbb{K}-$ev de dimension $n$ muni de deux bases $\mathcal{B} = (e_1, \cdots, e_n)$ et $\mathcal{B}' = (e_1', \cdots, e_n')$

On appelle matrice de passage de la base $\mathcal{B}$ a $\mathcal{B'}$ est la matrice $\text{Mat}_{\mathcal{B}}(\mathcal{B}')$

#### Propriété

Si $P$ définie la matrice de passage de la base $\mathcal{B}$ a $\mathcal{B}'$ alors

- $P = \text{Mat}_{\mathcal{B}',\mathcal{B}}(\text{id})$
- $P$ est inversible et $P^{-1}$ est la matrice de passage de la base $\mathcal{B}'$ a $\mathcal{B}$

#### Preuve

- $\text{Mat}_{\mathcal{B'}, \mathcal{B}}(\text{id}) = \text{Mat}_{\mathcal{B}}(\text{id}(\mathcal{B'})) = \text{Mat}_{\mathcal{B}}(\mathcal{B'}) = P$
- On note $Q$ la matrice de la base base $\mathcal{B}'$ a $\mathcal{B}$
- $QP = \text{Mat}_{\mathcal{B'},\mathcal{B}}(\text{id}) \times \text{Mat}_{\mathcal{B}, \mathcal{B'}}(\text{id}) = \text{Mat}(\text{id} \circ \text{id}) = I_n$

Par le théorème d'inversibilité, $P$ est inversible et $P^{-1 = Q}$

#### Exemples

Dans $\mathbb{R}^3$ de base canonique $B$, on pose:

$$
ε_1 = e_1 + e_2, ε _2 = e_2 + e_3, ε _3 = e_1 + e_2 + e_3
$$

$$
P =
\begin{pmatrix}
1 & 0 & 1 \\
1 & 1 & 1 \\
0 & 1 & 1
\end{pmatrix}
$$

Quelle est la matrice de passage de $(e_1, e_2, e_3) \to ( ε _1, ε _2, ε _3)$

Soient $L_0, L_1, L_2$ les polynomes d'interpolation de lagrange associés a $0, 1, 2$ dans $\mathbb{R}_2[X]$

Quelle est la matrice de passage de la base canonique a $(L_0, L_1, L_2)$

$$
P =
\begin{pmatrix}
    1 & 0 & 0 \\
    -\frac{3}{2} & 2 & -\frac{1}{2}\\
    \frac{1}{2} & -1 & \frac{1}{2}
\end{pmatrix}
$$

### Nouvelles composantes d'un vecteur

#### Théorème

Soit $E$ un $\mathbb{K}-$ev de dimension $n$, $B,B'$ deux bases de $E$.

Soit $x ∈ E$ et $X$ sa representation dans $B$ et $X'$ dans $B'$

On note $P$ la matrice de passage de $B$ a $B'$

$$
X = PX'
$$

#### Preuve

$X = \text{Mat}_B(x) = \text{Mat}_B(\text{id}(x))$

$= \text{Mat}_{B,B'}(\text{id}) \times \text{Mat}_{B'}(x)$

$= P X'$

### Nouvelles représentations d'une application linéaire

#### Théorème

Soient $E,F$ deux ev, de dimension $p,n$, muni de bases:
$$
\mathcal{E}, \mathcal{E'}
$$
pour $E$
et
$$
\mathcal{F}, \mathcal{F'}
$$
pour $F$

Soit $u ∈ \mathcal{L}(E,F)$

On note
- $A = \text{Mat}_{\mathcal{E}, \mathcal{F}}(u)$
- $A' = \text{Mat}_{\mathcal{E'}, \mathcal{F'}}(u)$
- $P$ la matrice de passage de $\mathcal{E}$ a $\mathcal{E'}$
- $Q$ la matrice de passage de $\mathcal{F}$ a $F'$

On a:
$$
A' = Q^{-1}AP
$$

#### Preuve

Soient $x  ∈E, y  ∈F$

$$
Y' = A'X' \iff u = u(x)
$$
$$
Y = QY', X = PX'
$$
$$
Q^{-1}Y = A' P^{-1}X
$$
$$
Y = Q A' P^{-1}X \iff y = u(x)
$$
$$
Y = AX
$$

Donc comme les matrices des vecteurs images sont uniques,
on peut identifier $QA'P^{-1}$ a $A$

Donc

$$
QA'P^{-1} = A \iff A' = Q^{-1}AP
$$

### Nouvelles représentations d'un endomorphisme

#### Théorème

Soient $B, B'$ deux bases de $E$, un $\mathbb{K}-$ev  de dimension $n$,

soit $u  ∈\mathcal{L}(E)$

On note $A = \text{Mat}_B(u), A' = \text{Mat}_{B'}(u)$

et $P$ la matrice de passage de $B$ a $B'$

$$
A' = P^{-1} A P
$$

### Application : la trace

#### Trace d'une matrice carée

#### Définition *trace*

Soit $A  ∈M_n(\mathbb{K}), A = (a_{i,j})$

On appelle trace de $A$ le scalaire défini par

$$
\text{tr}(A) = \sum_{i=1}^{n} a_{i,i}
$$

#### Exemples

- $\text{tr}(0) = 0$
- $\text{tr}(I_n) = n$
- $\text{tr}(E_{i,j}) = δ _{i,j}$


#### Propriétés

- $\text{tr}  ∈M_n(\mathbb{K})^{*}$
- $∀ A  ∈M_n(\mathbb{K}), \text{tr}(A^{\top}) = \text{tr}(A)$


Soient $A = (a_{i,j}), B = (b_{i,j})  ∈M_n(\mathbb{K})$

- $\text{tr}( λ A + B) = λ \text{tr}(A) + \text{tr}(B)$
- les coefficients diagonaux d'une matrice sont invariants par la transposée

#### Exercice

Déterminer la dimension de l'ensemble des matrices de trace nulle.

Réponse $n^2-1$

car $H = \text{ker}(\text{tr})$ avec $\text{tr}$ une forme linéaire non-nulle.

Determiner une base de $H$

Réponse
$$
B = (E_{i,j})_{i \neq j} ∪ (E_{i,i} - E_{n,n})_{1 \le i \le n-1}
$$

Question très très difficile que vaut:

$$
\text{Vect}(\{M / M ∈M_n(\mathbb{K}), ∃ p  ∈\mathbb{N} / M^{p}  =0\})
$$

Réponse
$$
H
$$

#### Théorème
$$
 ∀A ∈M_{n,p}(\mathbb{K}),  ∀B  ∈M_{p,n}(\mathbb{K})
$$

$$
\text{tr}(AB) = \text{tr}(BA)
$$

#### Preuve

On note $A = (A_{i,j}), B = (b_{i,j})$

$$
\text{tr}(AB) = \sum_{i=1}^{n} (AB)_{i,i}
$$
$$
\text{tr}(AB) = \sum_{i=1}^{n} \sum_{j=1}^{p} a_{i,j} b_{j,i}
$$
$$
\text{tr}(AB) = \sum_{j=1}^{p} \sum_{i=1}^{n} b_{j,i}a_{i,j}
$$
$$
\text{tr}(AB) = \text{tr}(BA)
$$

#### Exercice
- Réciproqument, si $φ  ∈M_n(\mathbb{K})^{*}$ vérifiant:
$$
 ∀A, B  ∈M_n(\mathbb{K}), φ (AB) = φ (BA)
$$
alors $φ = λ \text{tr} / λ  ∈\mathbb{K}$

- "Petit théorème de Fermat pour les matrices"
$$
 ∀p  ∈\mathbb{P},  ∀A  ∈M_n(\mathbb{Z})
$$
$$
\text{tr}(A^{p}) \equiv \text{tr}(A) [p]
$$

#### Trace d'un endomorphisme

Soit $f  ∈\mathcal{L}(E)$ avec $E$ un $\mathbb{K}-$ev de dimension finie.

Soit $A = \text{Mat}(f)$ dans la base $B$ 

#### Définition *trace d'un endomorphisme*

On pose 
$\text{tr}(f) = \text{tr}(A)$

Afin de légitimer cette définition, il faut vérifier que $\text{tr}(f)$ ne dépend pas de la base choisie.

Soit $B'$ une autre base de $E$ notons $A' = \text{Mat}(f)$ dans la base $B'$

Soit $P$ la matrice de passage de $B$ a $B'$.

On a $A' = P^{-1}AP$

donc $\text{tr}(A') = \text{tr}(P^{-1}AP) = \text{tr}(PP^{-1}A) = \text{tr}(A)$ (car les matrices commuttent dan la trace)

#### Propriétés


- $\text{tr}  ∈\mathcal{L}(E)^{*}$
- $∀ f  ∈\mathcal{L}(E), \text{tr}(f^{\top}) = \text{tr}(f)$
- $∀ f, g  ∈\mathcal{L}(E), \text{tr}(f \circ g) = \text{tr}(g \circ f)$

#### Exercice

Donner la trace de $f: \mathbb{R}_3[X] \to \mathbb{R}_3[X]$

$f : P \mapsto P'$

## Rang d'une matrice

### Définition

#### Définition *rang d'une matrice*

Soit $A = (a_{i,j})  ∈M_{n,p}(\mathbb{K})$

Les colonnes $C_1, \cdots, C_p$ de $A$ sont des vecteurs

de $M_{n,1}(\mathbb{K})$ on peut donc considérér le rang de cette famille de vecteurs

$$
\text{rg}(A) = \text{rg}(C_1, \cdots, C_p)
$$

### Propriétés rassurantes de rang d'une matrice

#### Théorème

Soit $E$ un ev et $F = (x_1, \cdots, x_p)$ une famille de $E$ muni d'une base $B$ 

On note $A = \text{Mat}_B(F)$

$$
\text{rg}(A) = \text{rg}(F)
$$

#### Preuve

Soit $φ x \mapsto \text{Mat}_B(x)$ qui est un isomorphisme

$$
\text{rg}(F) = \text{dim}(\text{Vect}(x_1, \cdots, x_p))
$$
$$
\text{rg}(F) = \text{dim}(\text{Vect}( φ (x_1), \cdots, φ (x_p))
$$
$$
\text{rg}(F) = \text{dim}( φ (\text{Vect}(F)))
$$

On peut enlever $φ$ car c'est un isomorphisme donc $\text{dim}( φ (\text{Vect}(F))) = \text{dim}(\text{Vect}(F))$

#### Propriétés

Soit $E,F$ des ev, $u  ∈\mathcal{L}(E,F)$

et $(e_1, \cdots, e_p)$ et $(b_1, \cdots, b_n)$

On a
$$
\text{rg}(u) = \text{rg}(\text{Mat}(u))
$$

#### Preuve

$$
\text{rg}(u) = \text{rg}(u(e_1), \cdots, u(e_p))
$$

#### Remarque

Tout calcul de rang se ramène au calcul de rang d'une matrice.

### Propriétés du rang d'une matrice

#### Propriétés

- $∀ A  ∈M_{n,p}(\mathbb{K}), \text{rg}(A) \le \text{min}(n,p)$
- $∀A  ∈M_{n,p}(\mathbb{K}),  ∀B  ∈M_{p,q}(\mathbb{K}), \text{rg}(AB) \le \text{min}(\text{rg}(A), \text{rg}(B))$
- $∀A  ∈M_{n,p}(\mathbb{K}), B  ∈GL_n(\mathbb{K}), \text{rg}(AB) = \text{rg}(BA) = \text{rg}(A)$
- On ne modifie pas le rang d'une matrice en la multipliant par une matrice inversible.
- $∀ A  ∈M_n(\mathbb{K}), A ∈ GL_n(\mathbb{K}) \iff \text{rg}(A) = n$
- $\text{rg}(A) = 0 \iff A = 0$

### Caractérisation théorique du rang

#### Définition

Soit $0 \le r \le \text{min}(n,p)$

La matrice $J_r$ est la matrice de taille $n,p$ définie par la formule suivante:

$$
\begin{pmatrix}
    I_r & 0_{r,p-r} \\
    0_{n-r,r} & 0_{n-r,p-r}
\end{pmatrix}
$$

Sinon si l'on note $J_r = (a_{i,j})$ on a: 
$$
∀ 1 \le i \le n, 1 \le j \le p, a_{i,j} = \begin{cases}
1 \text{ si } i = j \le r \\
0 \text{ sinon}
\end{cases}
$$

#### Exemples

Si $r=n=p$ alors $J_r = I_r$

Si $r=n \le p$ alors
$$
J_r =
\begin{pmatrix}
    I_n & 0_{n,p-n}
\end{pmatrix}
$$

Si $r=p\le n$ alors
$$
J_r =
\begin{pmatrix}
    I_p \\
    0_{n-p,p}
\end{pmatrix}
$$

#### Propriété

$$
\text{rg}(J_r) = r
$$

#### Preuve

Soit $(e_1, \cdots, e_n)$ la base canonique de $\mathbb{K}^{n}$

Soit $\mathcal{F} = (e_1, \cdots, e_r, 0, \cdots, 0)$

Alors $\text{Mat}(\mathcal{F}) = J_r$

or $\text{rg}(J_r) = \text{rg}(\mathcal{F}) = \text{rg}(e_1, \cdots, e_r) = r$


#### Théorème "Caractérisation théorique du rang"

Soit $0 \le r \le \text{min}(n,p)$ et $A  ∈M_{n,p}(\mathbb{K})$

$$
\text{rg}(A) = r \iff ∃ Q  ∈GL_n, P  ∈GL_p / A = QJ_rP
$$

#### Preuve

" $\impliedby$ ":

$$
\text{rg}(A) = \text{rg}(QJ_rP) = \text{rg}(J_r) = r
$$

" $\implies$ ":

On suppose que $\text{rg}(A) = r$

Soit $u  ∈\mathcal{L}(\mathbb{K}^{p}, \mathbb{K}^{n})$ l'application linéaire canoniquement associée a $A$.

On note $B_n$ la base canonique de $\mathbb{K}^{n}$ et $B_p$ celle de $\mathbb{K}^{p}$

$$
A = \text{Mat}_{B_p, B_n}(u)
$$

$$
\text{rg}(u) = r
$$

par le théorème du rang, ainsi:
$$
\text{dim}(\text{ker}(u)) = p - r
$$

Soit $S$ un supplémentaire de $\text{ker}(u)$

Soit $B' = (e_1', \cdots, e_r', e_{r+1}', \cdots, e_p')$ une base adaptée a sa supplémentarité.

Pour $1 \le i \le r$ on pose:
$$
f_i' = u(e_i')
$$

Montrons que $(f_i')$ est libre:
$$
\sum λ _i f_i' = 0
$$
$$
\sum λ _i u(e_i') = 0
$$
$$
u \left( \sum λ _i e_i '\right) = 0
$$
$$
\sum λ _i e_i'  ∈\text{ker}(u)
$$

Or $e_1', \cdots, e_r'  ∈S$ donc

$$
\sum λ _i e_i' = 0
$$

et cette famille est libre comme sous-famille d'une base, donc
$(f_1', \cdots, f_r')$ est libre et se complète en une base $F = (f_1, \cdots, f_n)$


$$
\text{Mat}_{B',F} (u) =
\begin{pmatrix}
    \text{Mat}_F(u(e_1')) & \cdots & \text{Mat}_F(u(e_r')) & \cdots & \text{Mat}_F(u(e_{r+1}')) & \cdots & \text{Mat}_F(u(e_n'))
\end{pmatrix}
$$

$$
\text{Mat}_{B',F} (u) =
\begin{pmatrix}
    \text{Mat}_F(f_1') & \cdots & \text{Mat}_F(f_r') & \cdots & \text{Mat}_F(0) & \cdots & \text{Mat}_F(0)
\end{pmatrix}
$$

$$
\text{Mat}_{B',F} (u) = J_r
$$

On note $P_1$ la matrice de passage de $B_p$ dans $B'$ et $Q_1$ de $B_n$ dans $B_n'$

$$
J_r = Q_1^{-1}A P_1
$$


Donc $P = P_1^{-1}$ et $Q = Q_1$ conviennent.

#### Corollaire

Soit $u  ∈\mathcal{L}(E,F)$

On note $n = \text{dim}(F), p = \text{dim}(E)$

Soit $0 \le r \le \text{min}(n,p)$

$$
\text{rg}(u) = r \iff ∃ B \text{ base de } E, ∃ C \text{ base de } F / \text{Mat}_{B,C}(u) = J_r
$$

#### Corollaire

$$
 ∀A  ∈M_{n,p}(\mathbb{K}), \text{rg}(A^{\top}) = \text{rg}(A)
$$

#### Preuve

On note $r = \text{rg}(A)$

Donc

$$
∃ P, Q  / A = Q J_r P
$$

$$
A^{\top} = P^{\top} J_r^{\top} Q^{\top}
$$

$$
\text{rg}(A^{\top}) = \text{rg}(J_r^{\top}) = r
$$

#### Corollaire

Soit $A  ∈M_{n,p}(\mathbb{K})$ Notons $L_1, \cdots, L_n$ les lignes de $A$.

$$
\text{rg}(A) = \text{rg}(L_1, \cdots, L_n)
$$

#### Preuve

Les lignes de $A$ sont les colonnes de $A^{\top}$

## Matrices équivalentes et matrices semblables

### Matrices équivalentes

#### Définition

Soient $A,B  ∈M_{n,p}(\mathbb{K})$

On dit que $A$ est équivalente a $B$ et on note:
$$
A \sim B
$$

si

$$
∃ P ∈GL_p(\mathbb{K}), ∃ Q  ∈GL_n(\mathbb{K}) / B = QAP
$$

#### Propriétés

- $\sim$ est une relation d'équivalence

- il y a $\text{min}(n,p)+1$  classes d'équivalences

#### Preuve

- $\sim$ est reflexive car $∀ A \sim A$ car $A = I_n A I_p$
- $\sim$ est symmétrique car $∀ A \sim B, B = QAP, A = Q^{-1}BP^{-1}$
- $\sim$ est transitive car $∀A \sim B \sim C$ on a $B = QAP, C = RBN$ donc $C = RQAPN, A \sim C$.

#### Remarques

Deux matrices sont équivalentes, et donc dans la même classe d'équivalence si et seulement si elles ont le même rang

Il s'agit donc de compter le nombre de matrices $J_r$ il y en a $\text{min}(n,p) + 1$

#### Définition *Matrices semblables*

Deux matrices $A,B ∈ M_n(\mathbb{K})$  sont dites emblables si
$$
∃ P  ∈GL_n(\mathbb{K}) / B = P^{-1}AP
$$

(Il n'y a pas de notation commune, nous utiliseront la notation $\approx$ pour signifier que $A,B$ sont semblables.

$$
A \approx B
$$

#### Propriétés

- $\approx$ est une relation d'équivalence
- $\approx$ possède une infinité de classes d'équivalences
- $A \approx B \implies A \sim B$, la réciproque étant fausse.
- $A \approx B \implies \text{rg}(A) = \text{rg}(B), \text{tr}(A) = \text{tr}(B)$ la réciproque étant fausse.

#### Preuve

On prend $A \approx B, B = P^{-1}AP$

donc $\text{tr}(B) = \text{tr}(P^{-1}AP) = \text{tr}(P^{-1}PA) = \text{tr}(A)$

La seule matrice semblable a $I_n$ est elle même, et $∀P  ∈GL_n(\mathbb{K}), P^{-1} I_n P = I_n$

Ainsi

$$
A = 
\begin{pmatrix}
    μ & 0 \\
    0 & 0
\end{pmatrix}
,B =
\begin{pmatrix}
    μ' & 0 \\
    0 & 0
\end{pmatrix}
\implies
\text{tr}(A) \neq \text{tr}(B)
$$

Donc notre relation $\approx$ possède une infinité de classes d'équivalences.

## Le pivot de Gauss pour calculer le rang d'une matrice

### Rappels

- Effectuer une opération élementaire sur une ligne revient a multiplier cette matrice a gauche par une matrice inversible.
- Effectuer une opération élementaire sur une colonne revient a multiplier cette matrice a droite par une matrice inversible


### Lien avec l'image et le noyeau d'une matrice

#### Théorème

Soit $A  ∈M_{n,p}(\mathbb{K})$

On ne modifie pas $\text{ker}(A)$ en effectuant des opérations élementaires sur les lignes de $A$.

On ne modifie pas $\text{im}(A)$ en effectuant des opérations élementaires sur les colonnes de $A$.

#### Preuve

Soit $B  ∈GL_n(\mathbb{K})$

On souhaite prouver que $\text{ker}(BA) = \text{ker}(A)$

$$
X ∈\text{ker}(A) \iff AX = 0 \iff BAX \iff 0 \iff X  ∈\text{ker}(BA)
$$

Et la double implication est vérifié pour $BAX$ car $B$ est inversible.

Soit $B  ∈GL_p(\mathbb{K})$

Il s'agit de montrer que $\text{im}(AB) = \text{im}(A)$

" $⊂$ ": Soit $Y  ∈\text{im}(AB)$

$$
∃ X ∈ M_{p,1}(\mathbb{K}) / Y = (AB)X = A(BX)  ∈\text{im}(A)
$$

" $\supset$ ": 
Soit $Y  ∈\text{im}(A)$
$$
∃ X ∈M_{n,1}(\mathbb{K}) / Y = AX = AB(B^{-1}X) ∈ \text{im}(AB)
$$

### Le pivot de Gauss pour calculer le rang d'une matrice.

#### Théorème

Le rang d'une matrice $A$ n'est pas modifié lorsqu'on opère sur les lignes et les colonnes de $A$ via les opérations élementaires.

#### Preuve

Le rang ne change pas par multiplication avec une matrice inversible.

On peut donc calculer le rang de $A$ de manière algorithmique via le pivot de Gauss.

#### Voici le principe

Soit $A = (a_{i,j}) ∈ M_{n,p}(\mathbb{K})$

- On repère un coéfficien non-nul sur la premierre colonne non-nul. Disions en ligne $i$. (Si il n'apparait pas on peut échanger des colonnes)
- On effectue $L_1 \leftrightarrow L_i$
- On effectue pour $2 \le i \le n$ l'opération:
$$
Li \leftarrow L_i - \frac{a_{i,1}}{a_{1,1}} L_1
$$

On obtient alors une matrice de la forme:
$$
\begin{pmatrix}
    p_1 & *\cdots* \\
    0 &  \\
    \vdots &  \\
    0 & *
\end{pmatrix}
$$

Avec $p_1 \neq 0$ qui est le premier pivot

- On répete sur la matrice $*$
- On continue tant que cela est possible
- a terme on obtient:

$$
\begin{pmatrix}
    p_1 &  & * & *\\
     & \ddots & & \\
    0 & & p_r & \\
    & 0_{n-r,r} & & 0_{n-r,p-r}
\end{pmatrix}
$$

Cette matrice est de rang $r$ et on a $\text{rg}(A) = r$

Pour aller plus loin et trouver $J_r$:

- On éffectue pour $1 \le i \le r$
$$
L_i \leftarrow \frac{1}{p_i} L_i
$$

On obtient alors:
$$
\begin{pmatrix}
    1 &  & * & *\\
     & \ddots & & \\
    0 & & 1 & \\
    & 0_{n-r,r} & & 0_{n-r,p-r}
\end{pmatrix}
$$

En opérant sur les colonnes et les lignes on aboutie a:
$$
\begin{pmatrix}
    I_r & 0_{r,p-r} \\
    0_{n-r,r} & 0_{n-r,p-r}
\end{pmatrix}
$$

#### Remarque

Ce procédé permet de calculer $P,Q$ de la caractérsation théorique du rang.

On vient de prouver qu'il existe des matrices inversibles $L_1, \cdots, L_q$ et $C_1, \cdots, C_p$ inversibles telles que

$$
\prod _{i=0}^{q-1} L_{q-i} A \prod_{i=1}^{p} C_i = J_r
$$


$$
\underbrace{\prod _{i=0}^{q-1} L_{q-i} I_n}_{\text{noté } Q} A \underbrace{I_p\prod_{i=1}^{p} C_i}_{\text{noté } P} = J_r
$$

Avec $Q$ obtenue en opérant les opérations $L_i$ sur $I_n$ et $P$ en opérant les $C_i$ sur $I_p$

#### Exercice

Écrire `rg(A)` et `caracterisation_theorique_rang(A)`

avec

```
rg(A) -> int
```

```
caracterisation_theorique_rang(A) -> ([ [float] ], [ [float] ])
```

